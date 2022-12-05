### Employee Data

    INSERT INTO `employees` VALUES (1,'Jhon','C','jhon@gmail.com',NULL,'4545464666',NULL,'2022-12-04 17:57:55',NULL,'2022-12-04 17:57:55');
    INSERT INTO `employees` VALUES (2,'Smit','D','smit@gmail.com',NULL,'123456',NULL,'2022-12-04 17:58:20',NULL,'2022-12-04 17:58:20');
    INSERT INTO `employees` VALUES (3,'David','miller','david@gmail.com',NULL,'234567898',NULL,'2022-12-04 17:59:54',NULL,'2022-12-04 17:59:54');
    INSERT INTO `employees` VALUES (4,'sanju','s','sanju@gmail.com',NULL,'345632122',NULL,'2022-12-04 18:00:25',NULL,'2022-12-04 18:00:25');
    INSERT INTO `employees` VALUES (5,'ricky','p','ricky@gmail.com',NULL,'34567890',NULL,'2022-12-04 18:01:10',NULL,'2022-12-04 18:01:10');

### Employee Salaries

    INSERT INTO `salaries` VALUES (1,1,50000,'2022-12-04 17:57:56','2022-12-04 17:57:56');
    INSERT INTO `salaries` VALUES (2,2,500000,'2022-12-04 17:58:20','2022-12-04 17:58:20');
    INSERT INTO `salaries` VALUES (3,3,50000,'2022-12-04 17:59:54','2022-12-04 17:59:54');
    INSERT INTO `salaries` VALUES (4,4,500000,'2022-12-04 18:00:26','2022-12-04 18:00:26');
    INSERT INTO `salaries` VALUES (5,5,100000,'2022-12-04 18:01:11','2022-12-04 18:01:11');

### Employee Departments

    INSERT INTO `deparments` VALUES (1,'Admin','New York',1);
    INSERT INTO `deparments` VALUES (2,'IT','Dallas',1);
    INSERT INTO `deparments` VALUES (3,'Financial','Chicago',1);
    INSERT INTO `deparments` VALUES (4,'Engeering','Boston',1);

### Employee Releation 
    
    INSERT INTO `dept_emp` VALUES (1,1,1,'2022-12-04 17:57:56','2022-12-04 17:57:56',1);
    INSERT INTO `dept_emp` VALUES (2,2,2,'2022-12-04 17:58:20','2022-12-04 17:58:20',1);
    INSERT INTO `dept_emp` VALUES (3,3,3,'2022-12-04 17:59:54','2022-12-04 17:59:54',1);
    INSERT INTO `dept_emp` VALUES (4,4,4,'2022-12-04 18:00:26','2022-12-04 18:00:26',1);
    INSERT INTO `dept_emp` VALUES (5,5,3,'2022-12-04 18:01:11','2022-12-04 18:01:11',1);

### Employee Leaves

    INSERT INTO `employee_leave` (`emp_id`, `start`, `end`, `reason`, `status`) VALUES
    (2, '2022-04-07', '2022-04-08', 'Sick Leave', 'Approved'),
    (2, '2022-04-07', '2022-04-08', 'Urgent Family Cause', 'Approved'),
    (3, '2022-04-08', '2022-04-08', 'Concert Tour', 'Approved'),
    (5, '2022-04-14', '2022-04-30', 'Want to see GOT', 'Pending'),
    (5, '2022-04-26', '2022-04-30', 'Launching Tesla Model Y', 'Pending');