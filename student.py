from flask import Flask
app=Flask(__name__)
@app.route('/student/<name>')
def student(name):
    return f"""
    <h1>student details</h1>
    <hr>
    <h2>Student details :{name}</h2>
"""
if __name__=="__main__":
    app.run(debug=True)

