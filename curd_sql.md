# CRUD OPERATIONS QUERIES
### Employees
    
    SELECT * FROM employees;  /* Display all employees*/
    
    SELECT * FROM employees WHERE emp_id =1 /* Display employee details by employee id */
    
    UPDATE employees SET
    `first_name` = <{first_name: }>,
    `last_name` = <{last_name: }>,
    `personal_email_id` = <{personal_email_id: }>,
    `company_email_id` = <{company_email_id: }>,
    `phone_number` = <{phone_number: }>,
    `gendar` = <{gendar: }>,
    `hire_date` = <{hire_date: CURRENT_TIMESTAMP}>,
    `is_active` = <{is_active: }>,
    `created_date` = <{created_date: CURRENT_TIMESTAMP}>
    WHERE `emp_id` = <{expr}>;  /* Update Employee details */
    
    
    /* Delete employee data and salaries detail, 
        demparment releation as well 
        beacuse of foregin key contraint of emp_id */

    DELETE FROM employees WHERE emp_id =<id>

    TRUNCATE table employees /* This step will do only after salaries, dep_emp tables truncate*/

### Deparments
    
    SELECT * FROM deparments;
    
    SELECT * FROM deparments WHERE id =<id>;

    UPDATE deparments SET
        `dep_name` = <{dep_name: }>,
        `location` = <{location: }>,
        `is_active` = <{is_active: }>
        WHERE `dep_no` = <{expr}>;
    
    DELETE FROM deparments WHERE dep_no = <dep_no>
    
    TRUNCATE TABLE deparments


### Employee Salaries
    
    SELECT * FROM salaries;
    
    SELECT * FROM salaries WHERE sal_id =<sal_id>

    UPDATE `salaries`
        SET
        `emp_id` = <{emp_id: }>,
        `salary` = <{salary: }>,
        `from_date` = <{from_date: }>,
        `to_date` = <{to_date: }>
        WHERE `sal_id` = <{expr}>;
    
    TRUNCATE TABLE salaries


### Employee Leaves
    
    SELECT * FROM employee_leave;
    
    SELECT * FROM employee_leave WHERE id =<id>;
    
    SELECT * FROM employee_leave WHERE emp_id =<emp_id>
    
    DELETE FROM employee_leave WHERE emp_id =<emp_id>
    
    UPDATE `employee_leave`
        SET
        `emp_id` = <{emp_id: }>,
        `start` = <{start: }>,
        `end` = <{end: }>,
        `reason` = <{reason: }>,
        `status` = <{status: }>
        WHERE `id` = <{expr}>;
    
    TRUNCATE TABLE employee_leave

    

    