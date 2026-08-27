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