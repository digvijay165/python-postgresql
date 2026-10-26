-- ============================================================
-- psql_commands.sql
-- Topics covered:
--   - Creating and dropping databases using psql
--   - Creating tables and inserting records using psql
--
-- How to run:
--   Open a terminal and run:  psql -U postgres -f psql_commands.sql
--   Or paste these commands one by one into the psql prompt.
-- ============================================================

-- 1. Create a database directly from psql
DROP DATABASE IF EXISTS psql_demo_db;
CREATE DATABASE psql_demo_db;

-- Switch to the new database (only works interactively in psql, not via -f)
-- \c psql_demo_db

-- 2. Create a table using psql
CREATE TABLE IF NOT EXISTS employees (
    emp_id SERIAL PRIMARY KEY,
    emp_name VARCHAR(100) NOT NULL,
    department VARCHAR(50) NOT NULL,
    salary NUMERIC(10, 2) NOT NULL
);

-- 3. Insert records using psql
INSERT INTO employees (emp_name, department, salary) VALUES
    ('Ananya Rao', 'Engineering', 65000.00),
    ('Karan Mehta', 'Marketing', 48000.00),
    ('Ishita Nair', 'Human Resources', 42000.00);

-- 4. Verify the inserted data
SELECT * FROM employees;

-- 5. (Optional) Drop the database when no longer needed
-- DROP DATABASE psql_demo_db;
