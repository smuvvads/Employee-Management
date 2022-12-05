### Create Employee Table Command
    
    CREATE TABLE `employees` (
      `emp_id` int NOT NULL AUTO_INCREMENT,
      `first_name` varchar(145) DEFAULT NULL,
      `last_name` varchar(145) DEFAULT NULL,
      `personal_email_id` varchar(145) DEFAULT NULL,
      `company_email_id` varchar(145) DEFAULT NULL,
      `phone_number` varchar(20) DEFAULT NULL,
      `gendar` varchar(45) DEFAULT NULL,
      `hire_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
      `is_active` tinyint DEFAULT NULL,
      `created_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
      PRIMARY KEY (`emp_id`)
    ) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

### Employee Salaries Table

    CREATE TABLE `salaries` (
      `sal_id` int NOT NULL AUTO_INCREMENT,
      `emp_id` int NOT NULL,
      `salary` int DEFAULT NULL,
      `from_date` datetime DEFAULT NULL,
      `to_date` datetime DEFAULT NULL,
      PRIMARY KEY (`sal_id`),
      KEY `emp_id` (`emp_id`),
      CONSTRAINT `salaries_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `employees` (`emp_id`) ON DELETE CASCADE
    ) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

### Employee Deparments Table

    CREATE TABLE `deparments` (
      `dep_no` int NOT NULL AUTO_INCREMENT,
      `dep_name` varchar(145) DEFAULT NULL,
      `location` varchar(145) DEFAULT NULL,
      `is_active` tinyint DEFAULT NULL,
      PRIMARY KEY (`dep_no`)
    ) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


### Employee Deparments Releation Table

    CREATE TABLE `dept_emp` (
      `id` int NOT NULL AUTO_INCREMENT,
      `emp_id` int NOT NULL,
      `dept_no` int DEFAULT NULL,
      `from_date` datetime DEFAULT CURRENT_TIMESTAMP,
      `to_date` datetime DEFAULT CURRENT_TIMESTAMP,
      `is_active` tinyint DEFAULT NULL,
      PRIMARY KEY (`id`),
      CONSTRAINT `dept_emp_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `employees` (`emp_id`) ON DELETE CASCADE,
      CONSTRAINT `dept_emp_ibfk_2` FOREIGN KEY (`dept_no`) REFERENCES `deparments` (`dep_no`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


### Employee Leaves

     CREATE TABLE `employee_leave` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `emp_id` int  NOT NULL,
      `start` date DEFAULT NULL,
      `end` date DEFAULT NULL,
      `reason` char(100) DEFAULT NULL,
      `status` char(50) DEFAULT NULL,
      PRIMARY KEY (`id`),
      CONSTRAINT `employee_leave_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `employees` (`emp_id`) ON DELETE CASCADE
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;