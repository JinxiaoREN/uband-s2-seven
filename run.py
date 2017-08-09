from flask import Flask
from flask import render_template
import json
app = Flask(__name__)



@app.route('/')
def index():
	file=open("./static/data/index.json","r+")
	file_text=file.read()
	data=json.loads(file_text)
	return render_template('index.html',data=data)

# @app.route('/helloworld')
# def hello_world():
#     # return 'Hello World!'
#     file=open('test.json','r+')
#     file_text=file.read()
#     print file_text
#     file_text = dict(json.loads(file_text))
#     print file_text['name']
#     return render_template('SKY.html',data=file_text)

# @app.route('/<string:student_number>/detailes')
# def details(student_number):
# 	return render_template(student_number + '.html')

if __name__ == '__main__':
    app.run(debug=True)