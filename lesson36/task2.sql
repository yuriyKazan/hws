SELECT first_name as "First Name", last_name as "Last Name" FROM employees;

SELECT distinct department_id FROM employees;

SELECT * FROM employees ORDER BY first_name DESC;

SELECT first_name, last_name, salary, salary*0.12 as "PF" FROM employees;

SELECT MAX(salary) as "MAX Salary", MIN(salary) as "MIN Salary" FROM employees;

SELECT first_name, last_name, round(salary/12,2) as "Monthly Salary" FROM employees;