# Global Superstore: Sales Performance & Profitability Analysis

## Capstone Project 2 — Data Analytics (Python + Tableau)

### Sector: Retail & E-Commerce
### Problem Statement
> *How can a global retail company optimize profitability across markets, product categories, and shipping strategies by identifying key revenue drivers, loss-making segments, and regional performance disparities?*

---

## Project Overview

This project performs an **end-to-end data analytics pipeline** on the Global Superstore dataset (51,290 transactions across 147 countries, 2011–2014). We clean the raw data using Python, conduct exploratory and statistical analysis, build an interactive Tableau dashboard, and deliver actionable business recommendations.

### Key Objectives
1. **Identify** the most and least profitable product categories and sub-categories across global markets
2. **Analyze** shipping cost efficiency and delivery performance by ship mode
3. **Evaluate** regional and country-level sales patterns and profit margins
4. **Uncover** the impact of discounts on profitability
5. **Recommend** data-backed strategies to improve operational efficiency and revenue

---

## Repository Structure

```
├── data/
│   ├── raw/                          # Original, unedited dataset from Kaggle
│   │   └── superstore_raw.csv
│   └── processed/                    # Cleaned dataset after ETL pipeline
│       └── superstore_cleaned.csv
├── notebooks/
│   ├── 01_extraction.ipynb           # Initial data extraction and profiling
│   ├── 02_cleaning.ipynb             # Python ETL/cleaning pipeline
│   ├── 03_eda.ipynb                  # Exploratory Data Analysis
│   ├── 04_statistical_analysis.ipynb # Statistical tests & modelling
│   └── 05_final_load_prep.ipynb      # KPI computation & Tableau-ready export
├── scripts/
│   └── etl_pipeline.py               # Standalone ETL pipeline Python script
├── tableau/
│   ├── screenshots/                  # Dashboard screenshots
│   └── dashboard_links.md           # Tableau Public URL
├── reports/
│   ├── Project_Report.pdf            # Detailed final project report
│   └── Presentation.pdf              # Presentation slides
├── docs/
│   └── data_dictionary.md           # Full data dictionary
└── README.md                        # This file
```

---

## Dataset

| Property | Detail |
|----------|--------|
| **Source** | [Kaggle — Global Superstore](https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting) |
| **Format** | CSV (Tabular, row-level transaction records) |
| **Rows** | 51,290 |
| **Columns** | 27 (raw) |
| **Time Span** | 2011 – 2014 |
| **Coverage** | 147 countries, 7 global markets |
| **Quality Issues** | Missing values, inconsistent date formats, non-English column headers (记录数), redundant columns, mixed encoding |

---

## Tools & Technologies

| Tool | Purpose |
|------|---------|
| **Python 3.x** | ETL pipeline, data cleaning, analysis |
| **Pandas / NumPy** | Data manipulation and computation |
| **Matplotlib / Seaborn** | Python-based visualizations |
| **SciPy / Statsmodels** | Statistical tests (ANOVA, chi-square, correlation, regression) |
| **Jupyter Notebook** | Reproducible analysis environment |
| **Tableau Public** | Interactive dashboard & storytelling |
| **GitHub** | Version control & collaboration |

---

## ETL Pipeline Summary

1. **Data Profiling** — Assessed data types, missing values, duplicates, and quality issues
2. **Column Standardization** — Cleaned dates, ensured numeric stability
3. **Date Parsing** — Converted `Order.Date` and `Ship.Date` to proper datetime
4. **Missing Value Treatment** — Imputed/dropped based on column significance
5. **Feature Engineering** — Created `Month`, `Month_Name`, `Day`, `Shipping_Days`, and `Profit_Margin_%` columns
6. **Validation** — Ensured referential integrity and business logic constraints
7. **Export** — Saved cleaned dataset to `data/processed/superstore_cleaned.csv`

---

## Key Insights (Preview)

- **Technology** category drives the highest revenue but has volatile profit margins
- **Tables** sub-category is consistently the biggest loss-maker across all markets
- **Same Day** shipping has the highest cost-to-sales ratio but lowest usage
- **Central Africa** region shows highest average profit margins despite lower sales volumes
- **Discounts above 30%** are strongly correlated with negative profitability

---

## Team Members & Contributions

| Name | Role | Responsibilities |
|------|------|-----------------|
| Harshit Singh | Data Engineer (ETL Lead) | Data profiling, cleaning pipeline, GitHub setup |
| Devansh Saini | Data Analyst (EDA Lead) | Exploratory analysis, trend identification |
| Yash Lahase | Statistician | Statistical tests, regression, hypothesis testing |
| Sudip Kumar Prasad | Visualization Lead | Tableau dashboard design & publishing |
| Garv Gogna | Report & Recommendations Lead | Final report, business recommendations, presentation |

---

## Links

- **Tableau Dashboard**: See [tableau/dashboard_links.md](tableau/dashboard_links.md)
- **Data Dictionary**: See [docs/data_dictionary.md](docs/data_dictionary.md)
- **Project Report**: See final report PDF in `reports/`

---

## License

This project is for academic purposes as part of the Data Visualization & Analytics Capstone 2 program.
