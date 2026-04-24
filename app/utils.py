import pandas as pd
import numpy as np
import streamlit as st
import os

@st.cache_data
def load_all_data():
    """Load all cleaned CSV files from multiple possible paths"""
    countries = ['ethiopia', 'kenya', 'sudan', 'tanzania', 'nigeria']
    df_list = []
    
    for country in countries:
        # Try different possible paths for deployment
        paths_to_try = [
            f'data/{country}_clean.csv',
            f'../data/{country}_clean.csv',
            f'/app/data/{country}_clean.csv',
            f'/mount/src/climate-challenge-week0/data/{country}_clean.csv'
        ]
        
        loaded = False
        for path in paths_to_try:
            if os.path.exists(path):
                try:
                    df = pd.read_csv(path)
                    df['Country'] = country.capitalize()
                    if 'Date' in df.columns:
                        df['Date'] = pd.to_datetime(df['Date'])
                    df['Year'] = df['Date'].dt.year
                    df['Month'] = df['Date'].dt.month
                    df_list.append(df)
                    st.success(f"✓ Loaded {country}")
                    loaded = True
                    break
                except Exception as e:
                    continue
        
        if not loaded:
            st.warning(f"Could not load {country}_clean.csv")
    
    if df_list:
        df_all = pd.concat(df_list, ignore_index=True)
        return df_all
    else:
        return pd.DataFrame()

@st.cache_data
def filter_data(df, countries, year_range):
    """Filter data by country and year range"""
    if df.empty:
        return df
    filtered = df[df['Country'].isin(countries)]
    filtered = filtered[(filtered['Year'] >= year_range[0]) & (filtered['Year'] <= year_range[1])]
    return filtered

def get_variable_label(var):
    """Get readable label for variable"""
    labels = {
        'T2M': 'Temperature (°C)',
        'PRECTOTCORR': 'Precipitation (mm/day)',
        'RH2M': 'Relative Humidity (%)',
        'WS2M': 'Wind Speed (m/s)'
    }
    return labels.get(var, var)