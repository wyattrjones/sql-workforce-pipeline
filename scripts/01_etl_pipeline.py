import sqlite3
import pandas as pd
import numpy as np

def generate_raw_data():
    """Simulates a raw, slightly messy HRIS export dataset."""
    np.random.seed(42)
    n_records = 500
    
    departments = ['Human Resources', 'Engineering', 'Sales', 'Operations', 'Finance']
    performance_ratings = ['Low', 'Meets Expectations', 'Exceeds Expectations', None] # Simulated missing value
    
    data = {
        'employee_id': [f'EMP-{1000 + i}' for i in range(n_records)],
        'department': np.random.choice(departments, n_records, p=[0.15, 0.3, 0.25, 0.2, 0.1]),
        'hire_date': pd.date_range(start='2018-01-01', end='2025-12-31', periods=n_records),
        'salary': np.random.randint(45000, 130000, n_records),
        'overtime_hours': np.random.choice([0, 5, 10, 15, 20, np.nan], n_records, p=[0.4, 0.2, 0.15, 0.1, 0.1, 0.05]), # Missing values simulated
        'performance_rating': np.random.choice(performance_ratings, n_records, p=[0.1, 0.6, 0.2, 0.1]),
        'attrition': np.random.choice([0, 1], n_records, p=[0.78, 0.22]) # 22% turnover rate
    }
    
    df = pd.DataFrame(data)
    return df

def run_etl():
    print("--- STEP 1: Extracting (Generating Raw Workforce Data) ---")
    raw_df = generate_raw_data()
    print(f"Generated {len(raw_df)} raw employee records.")
    
    print("\n--- STEP 2: Transforming (Cleaning Data) ---")
    # Fill missing overtime hours with 0 (assuming no logged overtime)
    raw_df['overtime_hours'] = raw_df['overtime_hours'].fillna(0)
    
    # Fill missing performance ratings with 'Not Rated'
    raw_df['performance_rating'] = raw_df['performance_rating'].fillna('Not Rated')
    
    # Ensure proper data types
    raw_df['salary'] = raw_df['salary'].astype(float)
    raw_df['attrition'] = raw_df['attrition'].astype(int)
    
    # Calculate tenure in years based on current date mock (2026)
    reference_date = pd.to_datetime('2026-01-01')
    raw_df['tenure_years'] = ((reference_date - raw_df['hire_date']).dt.days / 365.25).round(1)
    
    print("Data cleaning and transformations complete.")
    
    print("\n--- STEP 3: Loading into SQLite Database ---")
    # Creates/connects to a SQLite database inside the data folder
    conn = sqlite3.connect('../data/cleaned_workforce.db')
    
    # Load cleaned dataframe into a SQL table named 'workforce_analytics'
    raw_df.to_sql('workforce_analytics', conn, if_exists='replace', index=False)
    
    conn.close()
    print("Success! Cleaned data successfully loaded into 'data/cleaned_workforce.db'.")

if __name__ == '__main__':
    run_etl()
