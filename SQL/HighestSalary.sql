/*create database practice; */
use practice; 
/*
CREATE table department(
dept_id int PRIMARY KEY,
dept_name varchar(255) NOT NULL
);


INSERT into department values(1, "Computer Science");
INSERT into department values(2, "Electrical");
INSERT into department values(3, "Financial");

INSERT into department values(1, "Computer Science");
*/
/*
CREATE table employee(
e_id int PRIMARY KEY,
e_name varchar(255) NOT NULL,
e_salary int NOT NULL,
dept_id int,
FOREIGN KEY (dept_id)
REFERENCES department(dept_id)
);
*/
/*
SELECT * FROM EMPLOYEE AS E
JOIN DEPARTMENT AS D
ON D.DEPT_ID = E.DEPT_ID;
*/
SELECT E_SALARY FROM EMPLOYEE 
ORDER BY E_SALARY DESC;

SELECT E_SALARY FROM EMPLOYEE 
ORDER BY E_SALARY DESC LIMIT 3, 1;

