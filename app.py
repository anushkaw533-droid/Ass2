from flask import Flask
app=Flask(__name__)
@app.route('/')
def home():
    return """
<h1>welcome to flask application</h1>
<p>this is the home page.</p>"""
@app.route('/about')
def about():
    return """
<h1>about us</h1>
<p>this application is developed using flask framework.</p>"""
@app.route('/contact')
def contact():
    return """
<h1>contact us</h1>
<p>email:info@example.com</p>
<p>phone:9021707434</p>"""
if __name__=="__main__":
 app.run(debug=True)

VSC:=================================

1. Create a Flask application with the following static routes:
i) / 
ii) /about
iii) /contact
Display an appropriate message on each webpage.
  
  from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Home Page"

@app.route('/about')
def about():
    return "This is About Page"

@app.route('/contact')
def contact():
    return "This is Contact Page"

if __name__ == '__main__':
    app.run(debug=True)
=====================================================================

2. Create a dynamic URL route using an integer parameter:
/student/<int:roll_no>/<name> The route should accept the student’s roll number
and name through the URL and display the student details in a structured format.

  from flask import Flask

app = Flask(__name__)

@app.route('/student/<int:roll_no>/<name>')
def student(roll_no, name):
    return f"""
    <h2>Student Details</h2>
    <p><b>Roll Number:</b> {roll_no}</p>
    <p><b>Name:</b> {name}</p>
    """

if __name__ == '__main__':
    app.run(debug=True)

===================================================================================
3. Create a Flask application that stores an employee’s details (Employee ID, Name, Department, Basic Salary) 
in predefined variables, calculates HRA (20%), DA (12%), TA (8%), PF (10%), Gross Salary and Net Salary,
and displays a salary slip on the home page. gross_salary = basic_salary + hra + da + ta net_salary = gross_salary - pf

from flask import Flask

app = Flask(__name__)

# Employee details
employee_id = 101
name = "Payal"
department = "IT"
basic_salary = 30000

# Calculate salary components
hra = basic_salary * 20 / 100
da = basic_salary * 12 / 100
ta = basic_salary * 8 / 100
pf = basic_salary * 10 / 100

gross_salary = basic_salary + hra + da + ta
net_salary = gross_salary - pf

@app.route('/')
def home():
    return f"""
    <h2>Employee Salary Slip</h2>
    <p>Employee ID: {employee_id}</p>
    <p>Name: {name}</p>
    <p>Department: {department}</p>
    <p>Basic Salary: ₹{basic_salary}</p>
    <p>HRA (20%): ₹{hra}</p>
    <p>DA (12%): ₹{da}</p>
    <p>TA (8%): ₹{ta}</p>
    <p>PF (10%): ₹{pf}</p>
    <p>Gross Salary: ₹{gross_salary}</p>
    <p>Net Salary: ₹{net_salary}</p>
    """

if __name__ == '__main__':
    app.run(debug=True)

=================================================================================
==================================================================================


4. Create a Flask application to develop a dynamic product information page using URL routing.
Create a dynamic URL route /product/<product_name>/<int:price>/<category> that accepts product details through the URL
and displays the product name, price, category, discount amount(10%), GST (18%), 
and final price after calculation on the webpage. Test the application by accessing the URL 
with different product values through the browser and verify the output.

  
from flask import Flask

app = Flask(__name__)

@app.route('/product/<product_name>/<int:price>/<category>')
def product(product_name, price, category):

    discount = price * 10 / 100
    price_after_discount = price - discount

    gst = price_after_discount * 18 / 100
    final_price = price_after_discount + gst

    return f"""
    <h2>Product Information</h2>
    <p><b>Product Name:</b> {product_name}</p>
    <p><b>Price:</b> ₹{price}</p>
    <p><b>Category:</b> {category}</p>
    <p><b>Discount (10%):</b> ₹{discount}</p>
    <p><b>GST (18%):</b> ₹{gst}</p>
    <p><b>Final Price:</b> ₹{final_price}</p>
    """

if __name__ == '__main__':
    app.run(debug=True)

===============================================================================
===============================================================================
5. Create a Flask application with the following files: ● base.html ● home.html ● employees.html ● department.html Create employee data
and use Jinja2 loops to display the records. Use conditional statements to categorize employees
as Fresher, Experienced, or Senior based on experience. 
Use template inheritance and create a CSS file in static/css. Verify the application in the browser.

app.py ->...........
from flask import Flask, render_template

app = Flask(__name__)

employees = [
    {"id": 1, "name": "Payal", "department": "IT", "experience": 1},
    {"id": 2, "name": "Rahul", "department": "HR", "experience": 3},
    {"id": 3, "name": "Sneha", "department": "Finance", "experience": 7}
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/employees')
def employee_list():
    return render_template('employees.html', employees=employees)

@app.route('/department')
def department():
    return render_template('department.html')

if __name__ == '__main__':
    app.run(debug=True)

templates/base.html->..........
<!DOCTYPE html>
<html>
<head>
    <title>Employee Management</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>

    <h1>Employee Management System</h1>

    <nav>
        <a href="/">Home</a>
        <a href="/employees">Employees</a>
        <a href="/department">Department</a>
    </nav>

    {% block content %}
    {% endblock %}

</body>
</html>

templates/home.html->...................
{% extends 'base.html' %}

{% block content %}

<h2>Home Page</h2>
<p>Welcome to Employee Management System</p>

{% endblock %}

templates/employees.html->................
{% extends 'base.html' %}

{% block content %}

<h2>Employee List</h2>

{% for emp in employees %}

<p>
    ID: {{ emp.id }} <br>
    Name: {{ emp.name }} <br>
    Department: {{ emp.department }} <br>
    Experience: {{ emp.experience }} years <br>

    {% if emp.experience < 2 %}
        Category: Fresher
    {% elif emp.experience < 5 %}
        Category: Experienced
    {% else %}
        Category: Senior
    {% endif %}
</p>

<hr>

{% endfor %}

{% endblock %}

template department.html->.................
      {% extends 'base.html' %}

{% block content %}

<h2>Department Page</h2>

<p>IT Department</p>
<p>HR Department</p>
<p>Finance Department</p>

{% endblock %}

static/css/style.css->...............    
      body {
    font-family: Arial;
    margin: 30px;
}

h1 {
    text-align: center;
}

nav {
    text-align: center;
    margin: 20px;
}

nav a {
    margin: 15px;
    text-decoration: none;
}

================================================================================================================
      =====================================================================================
      
      6. Display Student Information using Jinja2 ,Create a Flask application with the following templates: base.html, home.html, student html .
Create student data containing name, roll number, and course in app.py. 
Pass the data to student.html using Jinja2 variables and display the student information. 
Use template inheritance and create a CSS file in the static/CSS folder. Verify the output in the browser.

1. app.py......................
from flask import Flask, render_template

app = Flask(__name__)

student = {
    "name": "Payal",
    "roll_no": 101,
    "course": "B.Sc. Computer Science"
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/student')
def student_info():
    return render_template('student.html', student=student)

if __name__ == '__main__':
    app.run(debug=True)

2. templates/base.html.......................................
<!DOCTYPE html>
<html>
<head>
    <title>Student Information</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>

    <h1>Student Information System</h1>

    <nav>
        <a href="/">Home</a>
        <a href="/student">Student</a>
    </nav>

    {% block content %}
    {% endblock %}

</body>
</html>

3. templates/home.html......................................
{% extends 'base.html' %}

{% block content %}

<h2>Home Page</h2>
<p>Welcome to Student Information System</p>

{% endblock %}

4. templates/student.html..........................................
{% extends 'base.html' %}

{% block content %}

<h2>Student Details</h2>

<p>Name: {{ student.name }}</p>
<p>Roll Number: {{ student.roll_no }}</p>
<p>Course: {{ student.course }}</p>

{% endblock %}

5. static/css/style.css.........................................
body {
    font-family: Arial;
    margin: 30px;
}

h1 {
    text-align: center;
}

nav {
    text-align: center;
    margin: 20px;
}

nav a {
    margin: 15px;
    text-decoration: none;
}

=====================================================================================================
7. Display HTML Template using Flask ,Create a Flask application with the following structure: templates/home.
html Create a home.html template and display a ‘ welcome’ message using the render_template() function.
Verify the output in the browser.

project/
│
├── app.py
│
└── templates/
    └── home.html

  
1️⃣ app.py.............................
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
  
2️⃣ templates/home.html.............................
<!DOCTYPE html>
<html>
<head>
    <title>Home Page</title>
</head>
<body>

    <h1>Welcome to Flask Application</h1>

</body>
</html>

===========================================================================================
========================================================

8. Display Course List using Jinja2 Loop, Create a Flask application with the following templates: base.html, home.html,
courses.html, Create a list of five courses in app.py. Use a Jinja2 for loop to display the courses in courses.html.
Use templateinheritance and create a CSS file in the static/CSS folder. Verify the output in the browser.

project/
│
├── app.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   └── courses.html
│
└── static/
    └── css/
        └── style.css

  
1️⃣ app.py................................
from flask import Flask, render_template

app = Flask(__name__)

courses = [
    "Python",
    "Java",
    "Web Technology",
    "Data Science",
    "Database Management"
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/courses')
def course_list():
    return render_template('courses.html', courses=courses)

if __name__ == '__main__':
    app.run(debug=True)


2️⃣ templates/base.html.............................
<!DOCTYPE html>
<html>
<head>
    <title>Course List</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>

    <h1>Course Management System</h1>

    <nav>
        <a href="/">Home</a>
        <a href="/courses">Courses</a>
    </nav>

    {% block content %}
    {% endblock %}

</body>
</html>

3️⃣ templates/home.html........................
{% extends 'base.html' %}

{% block content %}

<h2>Home Page</h2>
<p>Welcome to Course Management System</p>

{% endblock %}

4️⃣ templates/courses.html.........................


{% extends 'base.html' %}

{% block content %}

<h2>Available Courses</h2>

<ul>
    {% for course in courses %}
        <li>{{ course }}</li>
    {% endfor %}
</ul>

{% endblock %}

  
5️⃣ static/css/style.css...............................

body {
    font-family: Arial;
    margin: 30px;
}

h1 {
    text-align: center;
}

nav {
    text-align: center;
    margin: 20px;
}

nav a {
    margin: 15px;
    text-decoration: none;
}

li {
    margin: 10px;
}
======================================================================================================
=====================================================================

9. Student Result using Jinja2 Conditional Statements ,Create a Flask application with the following templates:base.html,home.html,result.html .
Create student name and percentage in app.py. Use Jinja2 conditional statements to display the result as Distinction, First Class, Second Class, Pass,
or Fail according to the percentage. Use template inheritance and create a CSS file in the static/CSS folder. Verify the output in the browser.


project/
│
├── app.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   └── result.html
│
└── static/
    └── css/
        └── style.css

  
1️⃣ app.py...............................
  
from flask import Flask, render_template

app = Flask(__name__)

student_name = "Payal"
percentage = 78

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result')
def result():
    return render_template(
        'result.html',
        name=student_name,
        percentage=percentage
    )

if __name__ == '__main__':
    app.run(debug=True)
  
2️⃣ templates/base.html..................................

<!DOCTYPE html>
<html>
<head>
    <title>Student Result</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>

    <h1>Student Result System</h1>

    <nav>
        <a href="/">Home</a>
        <a href="/result">Result</a>
    </nav>

    {% block content %}
    {% endblock %}

</body>
</html>

3️⃣ templates/home.html....................................................

{% extends 'base.html' %}

{% block content %}

<h2>Home Page</h2>
<p>Welcome to Student Result System</p>

{% endblock %}

4️⃣ templates/result.html.........................................

{% extends 'base.html' %}

{% block content %}

<h2>Student Result</h2>

<p>Name: {{ name }}</p>
<p>Percentage: {{ percentage }}%</p>

{% if percentage >= 75 %}
    <p>Result: Distinction</p>

{% elif percentage >= 60 %}
    <p>Result: First Class</p>

{% elif percentage >= 50 %}
    <p>Result: Second Class</p>

{% elif percentage >= 40 %}
    <p>Result: Pass</p>

{% else %}
    <p>Result: Fail</p>
{% endif %}

{% endblock %}

5️⃣ static/css/style.css.........................................

body {
    font-family: Arial;
    margin: 30px;
}

h1 {
    text-align: center;
}

nav {
    text-align: center;
    margin: 20px;
}

nav a {
    margin: 15px;
    text-decoration: none;
}

====================================================================================
======================================================================

10. Apply CSS Styling using Static Folder . Create a Flask application with the following structure: templates/home.
html and static/CSS/style.css .Create a home.html template and apply CSS styling using the style.css file in the static/CSS folder. 
Apply simple styling to the heading, paragraph, background, and text alignment. Verify the output in the browser.

project/
│
├── app.py
│
├── templates/
│   └── home.html
│
└── static/
    └── CSS/
        └── style.css
  
1️⃣ app.py.............................
  
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
  
2️⃣ templates/home.html............................

<!DOCTYPE html>
<html>
<head>
    <title>Home Page</title>

    <link rel="stylesheet"
          href="{{ url_for('static', filename='CSS/style.css') }}">
</head>

<body>

    <h1>Welcome to Flask</h1>

    <p>This is a Flask application with CSS styling.</p>

</body>
</html>

3️⃣ static/CSS/style.css................................

body {
    background-color: lightblue;
    text-align: center;
}

h1 {
    color: blue;
    font-size: 35px;
}

p {
    color: black;
    font-size: 20px;
}

=================================================================================
===============================