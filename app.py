from flask import Flask, flash, render_template, redirect, url_for, request, session, jsonify
from module.database import Database
import datetime

app = Flask(__name__)
app.secret_key = "mySc@$1emp"
db = Database()


@app.route('/')
def index():
    response = {}
    response['employees'] = db.get_all_employees(None)
    response['dept'] = db.get_deparments_list()
    return render_template('index.html', data=response)


@app.route('/create', methods=['POST', 'GET'])
def createEmployee():
    if request.method == 'POST' and request.form['save']:
        emp_data = {"first_name": request.form['first_name'],
                    "last_name": request.form['last_name'],
                    "personal_email_id": request.form['personal_email_id'],
                    "phone_number": request.form['phone_number']
                    }
        emp_id = db.insert(emp_data)
        if emp_id:
            dept_emp = {'emp_no': emp_id,
                        "dept_no": request.form['dept_no'],
                        "from_date": datetime.datetime.now(),
                        "to_date": datetime.datetime.now(),
                        "is_active": 1}
            salary_det = {'emp_id': emp_id,
                          "salary": request.form['salary'],
                          "from_date": datetime.datetime.now(),
                          "to_date": datetime.datetime.now()}
            db.insert_dept_emp(dept_emp)
            db.insert_salary_emp(salary_det)
            flash("A new employee has been added")
            return redirect(url_for('index'))
        else:
            flash("A new employee can not be added")
            return redirect(url_for('index'))
    else:
        flash("Please enter proper details")
        return redirect(url_for('index'))


@app.route('/loadempdata', methods=['POST', 'GET'])
def ajax_load_emp_data():
    response = {}
    emp_id = request.form['emp_id']
    response['employees'] = db.get_all_employee_details_by_id(emp_id)
    response['dept'] = db.get_deparments_list()
    return jsonify({'htmlresponse': render_template('emp_load_ajax.html', data=response)})


@app.route('/update', methods=['POST', 'GET'])
def update_emp_data():
    if request.method == 'POST' and request.form['update']:
        emp_data = {"first_name": request.form['first_name'],
                    "last_name": request.form['last_name'],
                    "personal_email_id": request.form['personal_email_id'],
                    "phone_number": request.form['phone_number']
                    }
        emp_id = request.form['emp_id']
        if db.emp_detail_update(emp_id, emp_data):
            dept_emp = {'emp_no': emp_id,
                        "dept_no": request.form['dept_no'],
                        }
            salary_det = {'emp_id': emp_id,
                          "salary": request.form['salary'],
                          }
            db.emp_slaray_update(emp_id, salary_det)
            db.emp_dept_update(emp_id, dept_emp)
            flash("employee detail has been updated")
            return redirect(url_for('index'))
        else:
            flash("employee detail can not be updated")
            return redirect(url_for('index'))
    else:
        flash("Please enter proper details")
        return redirect(url_for('index'))


@app.route('/delete_emp', methods=['POST', 'GET'])
def delete_emp():
    emp_id = request.form['emp_id']
    if db.delete(emp_id):
        return 'Success'
    else:
        return 'Error'


if __name__ == '__main__':
    app.run()
