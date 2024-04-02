#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:name_to_print>')
def print_string(name_to_print):
    print(name_to_print)
    return f'{name_to_print}'

@app.route('/count/<int:number>')
def count(number):
    # numbers = '\n'.join(str(i) for i in range(number))
    numbers = f""
    for i in range(number):
        numbers += f"{i}\n"
    return numbers

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == "+":
        output = num1 + num2
    elif operation == "-":
        output = num1 - num2
    elif operation == "*":
        output = num1 * num2
    elif operation == "div":
        output = num1 / num2
    elif operation == "%":
        output = num1 % num2
    else:
        return "Input a valid operator!"
    return f'{output}'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
