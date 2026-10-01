from flask import Flask, render_template
from payroll import build_payroll_data

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/payroll')
def payroll():
    payroll_data = build_payroll_data()
    
    return render_template('payroll.html', payroll_data = payroll_data)

if __name__ == '__main__':
    app.run()
