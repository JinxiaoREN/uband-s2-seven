from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    # return 'Hello World!'
    return render_template('SKY.html')

@app.route('/a13376')
def a13376():
    # return 'Hello World!'
    return render_template('a13376.html')

if __name__ == '__main__':
    app.run()