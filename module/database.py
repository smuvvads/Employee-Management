import pymysql


class Database:
    def connect(self):
        return pymysql.connect(host="localhost", user="root", password="g453u794", database="employeemanagement",
                               charset='utf8mb4')

    def insert(self, data):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute(
                "INSERT INTO employees(first_name,last_name,personal_email_id, phone_number) VALUES(%s, %s, %s, %s)",
                (data['first_name'], data['last_name'], data['personal_email_id'], data['phone_number'],))
            con.commit()

            return cursor.lastrowid
        except:
            con.rollback()
            return None
        finally:
            con.close()

    def insert_dept_emp(self, data):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute(
                "INSERT INTO dept_emp(emp_id, dept_no, from_date, to_date, is_active) VALUES(%s, %s, %s, %s, %s)",
                (data['emp_no'], data['dept_no'], data['from_date'], data['to_date'], data['is_active']))
            con.commit()
            return cursor.lastrowid
        except:
            con.rollback()
            return None
        finally:
            con.close()

    def insert_salary_emp(self, data):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute(
                "INSERT INTO salaries(emp_id,salary,from_date, to_date) VALUES(%s, %s, %s, %s)",
                (data['emp_id'], data['salary'], data['from_date'], data['to_date'],))
            con.commit()
            return cursor.lastrowid
        except:
            con.rollback()
            return None
        finally:
            con.close()

    def emp_detail_update(self, id, data):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute(
                "UPDATE employees set first_name = %s, last_name = %s, personal_email_id = %s, phone_number=%s where emp_id = %s",
                (data['first_name'], data['last_name'], data['personal_email_id'], data['phone_number'], id,))
            con.commit()

            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def emp_slaray_update(self, id, data):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute("UPDATE salaries set salary = %s where emp_id = %s",
                           (data['salary'], id,))
            con.commit()

            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def emp_dept_update(self, id, data):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute("UPDATE dept_emp set dept_no = %s where emp_id = %s",
                           (data['dept_no'], id,))
            con.commit()

            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def delete(self, id):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            # cursor.execute("DELETE FROM salaries where emp_id = %s", (id,))
            # cursor.execute("DELETE FROM dept_emp where emp_id = %s", (id,))
            cursor.execute("DELETE FROM employees where emp_id = %s", (id,))
            con.commit()
            return True
        except Exception:
            con.rollback()
            raise str(Exception)
        finally:
            con.close()

    def get_all_employees(self, id=None):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                sql = "SELECT * FROM employees AS e JOIN salaries AS s ON e.emp_id = s.emp_id" \
                      " JOIN dept_emp as de ON e.emp_id = de.emp_id" \
                      " JOIN deparments as d ON de.dept_no= d.dep_no order by e.emp_id DESC"
                print(sql)
                cursor.execute(sql)
            else:
                cursor.execute(
                    "SELECT * FROM employees where emp_id = %s order by emp_id DESC", (id,))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def get_deparments_list(self):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute("SELECT * FROM deparments")
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def get_all_employee_details_by_id(self, id):
        con = Database.connect(self)
        cursor = con.cursor()
        try:
            sql = "SELECT * FROM employees AS e JOIN salaries AS s ON e.emp_id = s.emp_id" \
                  " JOIN dept_emp as de ON e.emp_id = de.emp_id" \
                  " JOIN deparments as d ON de.dept_no= d.dep_no WHERE e.emp_id = %s"
            cursor.execute(sql, (id,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()
