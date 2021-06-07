SELECT * FROM departments
PRAGMA table_info(employees);

SELECT employees.first_name, employees.last_name, employees.department_id, departments.depart_name
FROM employees
LEFT JOIN departments ON employees.department_id = departments.department_id;

SELECT employees.first_name, employees.last_name, departments.depart_name, locations.city, locations.state_province
FROM employees
LEFT JOIN departments ON employees.department_id = departments.department_id
LEFT JOIN locations ON departments.location_id = locations.location_id;

SELECT employees.first_name, employees.last_name, employees.department_id, departments.depart_name
FROM employees
LEFT JOIN departments ON employees.department_id = departments.department_id
WHERE employees.department_id in (80, 40);

SELECT departments.depart_name, employees.first_name, employees.last_name
FROM departments
LEFT JOIN employees ON employees.department_id = departments.department_id

SELECT employees.first_name
FROM employees
LEFT JOIN departments ON employees.department_id = departments.department_id;

SELECT employees.first_name AS "Employee", manager.first_name AS "Manager"
FROM employees
JOIN employees manager ON employees.manager_id = manager.employee_id;

SELECT jobs.job_title, employees.first_name ||' '|| employees.last_name AS "employee", max_salary - salary AS "difference"
FROM employees
JOIN jobs ON jobs.job_id = employees.job_id;

SELECT jobs.job_title, avg(salary) AS "average_salary"
FROM employees
JOIN jobs ON jobs.job_id = employees.job_id
GROUP BY 1;

SELECT employees.first_name ||' '|| employees.last_name AS "employee",  salary
FROM employees
JOIN departments ON employees.department_id = departments.department_id
JOIN locations ON locations.location_id = departments.location_id
WHERE  city = 'London';

SELECT departments.depart_name, count(employees.employee_id) as employees
FROM departments
JOIN employees ON employees.department_id = departments.department_id
GROUP BY 1;
