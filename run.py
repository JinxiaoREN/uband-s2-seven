from flask import Flask
from flask import render_template
import json
app = Flask(__name__)

def read_json_file(filepath):
	file=open(filepath,"r+")
	file_text=file.read()
	data=json.loads(file_text)
	return data

@app.route('/')
def index():
	# file=open("./static/data/index.json","r+")
	# file_text=file.read()
	# data=json.loads(file_text)
	data=read_json_file('./static/data/index.json')
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

@app.route('/details/<string:student_number>')
def details(student_number):
	data=read_json_file('./static/data/index.json')
	user_data={}
	for item in data:
		if student_number==item['student_number']:
			user_data=item
			break
	return render_template('details.html',data=user_data)

if __name__ == '__main__':
    app.run(debug=True)