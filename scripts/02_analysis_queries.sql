-- ==========================================================
-- WORKFORCE ANALYTICS & ATTRITION DEEP-DIVE
-- Description: Advanced SQL queries to extract cost drivers,
-- department turnover rates, and compensation impact.
-- ==========================================================

-- 1. OVERALL TURNOVER RATE & METRICS
-- Calculates total headcount, active employees, and overall company attrition percentage.
SELECT 
    COUNT(*) AS total_employees,
    SUM(attrition) AS total_departures,
    ROUND(CAST(SUM(attrition) AS REAL) / COUNT(*) * 100, 2) AS company_attrition_rate_pct,
    ROUND(AVG(salary), 2) AS average_company_salary
FROM workforce_analytics;


-- 2. ATTRITION & COMPENSATION BY DEPARTMENT
-- Identifies which departments are bleeding the most talent and their average pay scales.
SELECT 
    department,
    COUNT(*) AS department_headcount,
    SUM(attrition) AS departures,
    ROUND(CAST(SUM(attrition) AS REAL) / COUNT(*) * 100, 2) as dept_attrition_rate_pct,
    ROUND(AVG(salary), 2) AS avg_department_salary,
    ROUND(AVG(overtime_hours), 1) AS avg_overtime_hours
FROM workforce_analytics
GROUP BY department
ORDER BY dept_attrition_rate_pct DESC;


-- 3. PERFORMANCE RATING VS. ATTRITION RISK
-- Analyzes whether high performers are leaving or if turnover is concentrated elsewhere.
SELECT 
    performance_rating,
    COUNT(*) AS employee_count,
    SUM(attrition) AS departures,
    ROUND(CAST(SUM(attrition) AS REAL) / COUNT(*) * 100, 2) AS attrition_rate_pct,
    ROUND(AVG(salary), 2) AS avg_salary
FROM workforce_analytics
GROUP BY performance_rating
ORDER BY avg_salary DESC;


-- 4. TENURE BRACKET ANALYSIS (RISK WINDOW)
-- Identifies which tenure group experiences the highest risk of turnover.
SELECT 
    CASE 
        WHEN tenure_years < 1.0 THEN 'Less than 1 Year'
        WHEN tenure_years BETWEEN 1.0 AND 3.0 THEN '1 to 3 Years'
        WHEN tenure_years BETWEEN 3.1 and 5.0 THEN '3 to 5 Years'
        ELSE '5+ Years'
    END AS tenure_bracket,
    COUNT(*) AS headcount,
    SUM(attrition) as departures,
    ROUND(CAST(SUM(attrition) AS REAL) / COUNT(*) * 100, 2) AS bracket_attrition_rate_pct
FROM workforce_analytics
GROUP BY tenure_bracket
ORDER BY bracket_attrition_rate_pct DESC;
