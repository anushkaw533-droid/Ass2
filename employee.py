from flask import Flask
app=Flask(__name__)
@app.route('/employee/<int:emp_id>/<name>/<department>')
def employee(emp_id,name,department):
    return f"""
<h1>employee profile</h1>
<b>employee id:</b>{emp_id}<br><br>
<b>name:</b>{name}<br><br>
<b>department:</b>{department}<br><br>
"""
if __name__=="__main__":
    app.run(debug=True)
