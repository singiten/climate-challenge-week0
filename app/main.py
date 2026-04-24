import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import load_all_data, filter_data, get_variable_label
import os

# Page configuration
st.set_page_config(
    page_title="Climate Dashboard - COP32",
    page_icon="🌍",
    layout="wide"
)

# Title
st.title("🌍 EthioClimate Analytics Dashboard")
st.subheader("Historical Climate Data for COP32 Preparation (2015-2026)")

# Show current directory for debugging (remove after deployment works)
with st.expander("🔧 Debug Info (click to expand)"):
    st.write(f"Current directory: {os.getcwd()}")
    st.write(f"Files in current directory: {os.listdir('.') if os.path.exists('.') else 'N/A'}")
    if os.path.exists('data'):
        st.write(f"Files in data/: {os.listdir('data')}")
    else:
        st.write("data/ folder not found")

# Load data
with st.spinner("Loading climate data..."):
    df = load_all_data()

if df.empty:
    st.error("No data loaded. Please ensure clean CSV files exist in the data/ folder.")
    st.stop()

# Sidebar filters
st.sidebar.header("🔍 Filter Controls")

# Country selector
all_countries = df['Country'].unique().tolist()
selected_countries = st.sidebar.multiselect(
    "Select Countries",
    all_countries,
    default=all_countries
)

# Year range slider
min_year = int(df['Year'].min())
max_year = int(df['Year'].max())
year_range = st.sidebar.slider(
    "Select Year Range",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year)
)

# Variable selector
variable = st.sidebar.selectbox(
    "Select Variable",
    options=['T2M', 'PRECTOTCORR', 'RH2M', 'WS2M'],
    format_func=get_variable_label
)

# Filter data
filtered_df = filter_data(df, selected_countries, year_range)

if filtered_df.empty:
    st.warning("No data available for selected filters.")
    st.stop()

# Display metrics
st.subheader("📊 Key Metrics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Countries", len(selected_countries))

with col2:
    st.metric("Years", f"{year_range[0]} - {year_range[1]}")

with col3:
    avg_temp = filtered_df['T2M'].mean()
    st.metric("Avg Temperature", f"{avg_temp:.1f}°C")

with col4:
    total_precip = filtered_df['PRECTOTCORR'].sum()
    st.metric("Total Precipitation", f"{total_precip:.0f} mm")

st.divider()

# Temperature Trend Chart
st.subheader("📈 Temperature Trend")

temp_data = filtered_df.groupby(['Year', 'Country'])['T2M'].mean().reset_index()

fig1, ax1 = plt.subplots(figsize=(12, 6))

for country in selected_countries:
    country_data = temp_data[temp_data['Country'] == country]
    if not country_data.empty:
        ax1.plot(country_data['Year'], country_data['T2M'], marker='o', label=country, linewidth=2)

ax1.set_xlabel('Year')
ax1.set_ylabel('Temperature (°C)')
ax1.set_title('Average Temperature by Country')
ax1.legend()
ax1.grid(True, alpha=0.3)

st.pyplot(fig1)

st.divider()

# Precipitation Distribution
st.subheader("☔ Precipitation Distribution")

fig2, ax2 = plt.subplots(figsize=(12, 6))

# Filter out zeros for better visualization
precip_data = filtered_df[filtered_df['PRECTOTCORR'] > 0]

if not precip_data.empty:
    sns.boxplot(x='Country', y='PRECTOTCORR', data=precip_data, ax=ax2)
    ax2.set_xlabel('Country')
    ax2.set_ylabel('Precipitation (mm/day)')
    ax2.set_title('Distribution of Daily Precipitation by Country')
    ax2.set_yscale('log')
else:
    ax2.text(0.5, 0.5, 'No precipitation data available', ha='center', transform=ax2.transAxes)

st.pyplot(fig2)

st.divider()

# Variable Comparison Chart
st.subheader(f"📊 {get_variable_label(variable)} by Country")

fig3, ax3 = plt.subplots(figsize=(12, 6))

if variable == 'PRECTOTCORR':
    # For precipitation, show boxplot
    plot_data = filtered_df[filtered_df[variable] > 0]
    if not plot_data.empty:
        sns.boxplot(x='Country', y=variable, data=plot_data, ax=ax3)
        ax3.set_yscale('log')
    else:
        ax3.text(0.5, 0.5, 'No precipitation data available', ha='center', transform=ax3.transAxes)
else:
    # For other variables, show bar chart with mean
    var_data = filtered_df.groupby('Country')[variable].mean().reset_index()
    ax3.bar(var_data['Country'], var_data[variable])
    ax3.set_ylabel(get_variable_label(variable))

ax3.set_xlabel('Country')
ax3.set_title(f'{get_variable_label(variable)} Comparison')

st.pyplot(fig3)

st.divider()

# Data Table (expandable)
with st.expander("📋 View Raw Data"):
    st.dataframe(filtered_df, use_container_width=True)

# Footer
st.divider()
st.markdown(
    """
    <div style="text-align: center; color: gray;">
    <p>Data Source: NASA POWER (Prediction of Worldwide Energy Resources)</p>
    <p>Prepared for: EthioClimate Analytics | COP32 Preparation</p>
    </div>
    """,
    unsafe_allow_html=True
)