#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


@app.route('/print/<parameter>')
def print_parameter(parameter):
    print(parameter)
    return parameter


@app.route('/count/<parameter>')
def count(parameter):
    parameter = int(parameter)
    output = ''
    for i in range(parameter):
        output += f"{i}\n"
    return output


@app.route('/math/<num1>/<path:operation>/<num2>')
def math(num1, operation, num2):
    num1 = int(num1)
    num2 = int(num2)

    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == 'div':
        return str(num1 / num2)
    elif operation == '%':
        return str(num1 % num2)



if __name__ == '__main__':
    app.run(port=5555)
