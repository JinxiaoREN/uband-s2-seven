from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    # return 'Hello World!'
    return render_template('SKY.html')

@app.route('/sanlianyin')
def sanlianyin():    
    return render_template('sanlianyin.html')
if __name__ == '__main__':
    app.run(debug=True)