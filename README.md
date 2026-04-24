# Climate Challenge Week 0 - EthioClimate Analytics

Author:Singiten Beshada  
Program:10 Academy - KAIM 9  
Date: April 2026  



Project Overview

This project analyzes historical climate data (2015-2026) for five African countries (Ethiopia, Kenya, Sudan, Tanzania, Nigeria) using NASA POWER satellite data. The analysis supports Ethiopia's preparation for hosting COP32 in Addis Ababa (2027) by providing evidence-backed insights on climate trends, vulnerabilities, and policy recommendations.



 Repository Structure
climate-challenge-week0/
├── .github/workflows/
│ └── ci.yml # GitHub Actions CI workflow
├── app/
│ ├── init.py
│ ├── main.py # Streamlit dashboard (bonus)
│ └── utils.py # Dashboard utilities
├── data/ # Cleaned CSV files (gitignored)
├── notebooks/
│ ├── ethiopia_eda.ipynb # EDA for Ethiopia
│ ├── kenya_eda.ipynb # EDA for Kenya
│ ├── sudan_eda.ipynb # EDA for Sudan
│ ├── tanzania_eda.ipynb # EDA for Tanzania
│ ├── nigeria_eda.ipynb # EDA for Nigeria
│ └── compare_countries.ipynb # Cross-country comparison
├── src/ # Source code (future use)
├── tests/ # Unit tests (future use)
├── scripts/ # Utility scripts
├── .gitignore
├── requirements.txt
└── README.md
Install Dependencies

pip install -r requirements.txt
Download Data
Download the CSV files from NASA POWER dataset and place them in the data/ folder:

ethiopia.csv

kenya.csv

sudan.csv

tanzania.csv

nigeria.csv
Run EDA Notebooks
jupyter notebook
Run Cross-Country Comparison
Open notebooks/compare_countries.ipynb and run all cells.
Streamlit Dashboard (Bonus)
Run Locally
streamlit run app/main.py
Then open http://localhost:8501 in your browser.
Dashboard Features
Country multi-select filter
Year range slider (2015-2026)
Variable selector (Temperature, Precipitation, Humidity, Wind Speed)
Temperature trend line chart
Precipitation distribution boxplot
Key metrics display
Raw data table view
CI/CD Pipeline
GitHub Actions runs on every push to main branch:
Checks out the code
Sets up Python 3.10
Installs dependencies from requirements.txt
Verifies Python version
COP32 Recommendations
Increased adaptation finance for Sudan and Nigeria
Regional early warning systems for extreme heat and drought

Investment in climate-resilient agriculture

Loss and damage compensation for vulnerable countries

Technology transfer for drought monitoring
Technologies Used
Python 3.14
Pandas, NumPy, Matplotlib, Seaborn, Scipy Streamlit
Git & GitHub
GitHub Actions
Contact
Singiten Beshada
GitHub: github.com/singiten