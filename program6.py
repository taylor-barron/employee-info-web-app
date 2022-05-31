import sqlite3
from bottle import route, run, request, response, template

@route('/', method = "GET")
def index():
    return template('login_page')

@route('/getDepartment', method = ["GET", "POST"])
def getDepartment():
    if request.method == 'GET':
        return template('get_department')
    else:

        try:
            dept = request.forms.get("dept")
            conn = sqlite3.connect("payroll.db")
            cur = conn.cursor()

            sql = '''SELECT pay_data.emp_id, emp_name, wage, hrs_worked FROM employees JOIN pay_data WHERE pay_data.emp_id = employees.emp_id AND employees.department = ?'''
            cur.execute(sql, (dept,))

            rows = cur.fetchall()
            cur.close()
            hrs = 0
            wage = 0

            if rows:
                dataList = []
                for row in rows:
                    eid, name, wage, hrs = row  #unpack tuple
                    if hrs <= 40:
                        payout = wage * hrs
                    else:
                        ot_pay = (hrs - 40) * 1.5 * wage
                        payout = (wage * 40) + ot_pay

                    emp = (eid, name, wage, hrs, payout)
                    dataList.append(emp)
                data = {'rows': dataList, 'dept': dept}
                return template('show_department', data)
            else:
                m = {'msg': 'No results found'}
                return template('error_message', m)

        except:
            m = {'msg': 'Error accessing table'}
            return template('error_message', m)

@route('/editHours', method = ["GET", "POST"])
def editHours():
    if request.method == "GET":
        return template('edit_hours')
    else:
        empID = request.forms.get("emp_id")
        hrsWorked = request.forms.get("hours")

        try:
            conn = sqlite3.connect("payroll.db")
            cur = conn.cursor()
            sql = "UPDATE pay_data SET hrs_worked = ? WHERE emp_id = ?"

            cur.execute(sql, (hrsWorked, empID))
            conn.commit()
            cur.close()

            try:
                # new fetchone after successful edit
                conn = sqlite3.connect("payroll.db")
                cur = conn.cursor()
                sql = "SELECT emp_name, department FROM employees WHERE emp_id = ?"

                cur.execute(sql, (empID,))
                result = cur.fetchone()
                cur.close()
                m = {'eid': empID, 'name': result[0], 'dept': result[1]}
                return template('successful_edit', m)
            except:
                m = {'msg': 'Error reporting changes. Changes made.'}
                return template('error_message', m)
                
        except:
            m = {'msg': 'Error editing data. No changes made.'}
            return template('error_message', m)

run(host='localhost', port=8080, debug=True)