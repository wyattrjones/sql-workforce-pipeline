# Enterprise SQL Workforce & Attrition Pipeline

An end-to-end automated data engineering and analytics pipeline built to simulate, clean, store, and analyze human resources data. Designed to uncover high-impact cost drivers, department turnover rates, and compensation risks.

---

## 🚀 Project Architecture & Tech Stack
* **Language:** Python 3.x
* **Data Processing:** Pandas, NumPy
* **Database:** SQLite (Relational Data Store)
* **Analysis:** Advanced SQL (Aggregations, Window Logic, Case Statements)

---

## 📂 Repository Structure
```text
sql-workforce-pipeline/
│
├── data/
│   └── cleaned_workforce.db      # Generated SQLite database (loaded via ETL)
│
├── scripts/
│   ├── 01_etl_pipeline.py        # Python extraction, simulation, cleaning, and loading script
│   └── 02_analysis_queries.sql   # Advanced SQL queries for workforce risk and cost metrics
│
└── README.md                     # Project documentation
