from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    # return 'Hello World!'
    return render_template('SKY.html')

@app.route('/<string:student_number>/detailes')
def details(student_number):
	return render_template(student_number + '.html')

if __name__ == '__main__':
    app.run()