---
# Employee Management System

## Description
This project maintains the employee salaries and leave system. Here we have defined 4 tables in our database. They are namely,
1. Employees
2. Salaries
3. Departments
4. Leaves

Each table holds the employee data and are connected with primary and foreign keys. A detailed view of the tables and the manner they have created is discussed below.

### Tables
TABLE Name:`employees`:
This table is used to store the employee details
Functional dependent on `emp_id`

    Attributes : 
      `emp_id` int NOT NULL AUTO_INCREMENT,
      `first_name` varchar(145) DEFAULT NULL,
      `last_name` varchar(145) DEFAULT NULL,
      `personal_email_id` varchar(145) DEFAULT NULL,
      `company_email_id` varchar(145) DEFAULT NULL,
      `phone_number` varchar(20) DEFAULT NULL,
      `gendar` varchar(45) DEFAULT NULL,
      `hire_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
      `is_active` tinyint DEFAULT NULL,
      `created_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
`emp_id is the primary key`

___
TABLE Name: `salaries`:
This table is used for to store the employee's salaries
Functional dependent on sal_id, and
it has 3 NF on employee table

     Attributes: 
      `sal_id` int NOT NULL AUTO_INCREMENT,
      `emp_id` int NOT NULL,
      `salary` int DEFAULT NULL,
      `from_date` datetime DEFAULT NULL,
      `to_date` datetime DEFAULT NULL,

`sal_id is the primary key, emp_id is the FOREIGN KEY`
___
TABLE Name: `deparments`:
This table is used for to store the departments
Functional dependent on dep_no

    Attributes:
      `dep_no` int NOT NULL AUTO_INCREMENT,
      `dep_name` varchar(145) DEFAULT NULL,
      `location` varchar(145) DEFAULT NULL,
      `is_active` tinyint DEFAULT NULL,
`dep_no is the primary key`
___
TABLE  Name: `employee_leave`:
This table is used for employee's leave
Functional dependent on id, and 
it has 3 NF on employee table

     Attributes : 
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `emp_id` int  NOT NULL,
      `start` date DEFAULT NULL,
      `end` date DEFAULT NULL,
      `reason` char(100) DEFAULT NULL,
      `status` char(50) DEFAULT NULL,

`id is the primary key, emp_id is the foreign key`
___
TABLE Name : `dept_emp`:
This table is used for to store the employee departments, and 
it has 3 NF on employee and departments tables

    Attributes:
      `id` int NOT NULL AUTO_INCREMENT,
      `emp_id` int NOT NULL,
      `dept_no` int DEFAULT NULL,
      `from_date` datetime DEFAULT CURRENT_TIMESTAMP,
      `to_date` datetime DEFAULT CURRENT_TIMESTAMP,
      `is_active` tinyint DEFAULT NULL,
    
`id is the primary key, emp_id, dept_no are the foreign keys`
    
### Sample Data For Employees:
| emp_id | first_name | last_name | personal_email_id | company_email_id | phone_number | gendar |      hire_date      | is_active |    created_date    |
|:------:|:----------:|:---------:|:-----------------:|:----------------:|:------------:|:------:|:-------------------:|:---------:|:------------------:|
|   1    |    Jhon    |     C     |  jhon@gmail.com   |       NULL       |  4545464666  |  NULL  | 2022-12-04 17:57:55 |     1     | 2022-12-04 17:57:55 |


### Sample Data For Employee Salaries:
| sal_id | emp_id | salary |      from_date      |       to_date       | 
|:------:|:------:|:------:|:-------------------:|:-------------------:|
|   1    |   1    | 30000  | 2022-11-04 17:57:55 | 2022-12-04 17:57:55 |

### Sample Data For Departments:
| dep_no | dep_name | location | is_active |
|:------:|:----------:|:--------:|:---------:|
|   1    |    Admin    | New yark |     1     |



### Sample Data For Employees And Departments Relation:
| id | emp_id | dept_no |      from_date      | to_date | is_active |
|:------:|:------:|:-------:|:-------------------:|:----------------:|:---------:|
|   1    |   1    |    1    | 2021-11-04 17:57:55 |       2022-12-04 17:57:55       |     1     | 



### Sample Data For Employees Leaves:
| id | emp_id |   start    |    end     | reason |  status  | 
|:------:|:------:|:----------:|:----------:|:----------------:|:--------:|
|   1    |   1    | 2022-04-07 | 2022-04-08 |       Sick Leave       | Approved |



