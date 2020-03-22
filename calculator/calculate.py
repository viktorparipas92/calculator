from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

import time

from calculator.functions import ackermann, factorial, fibonacci

bp = Blueprint('calculate', __name__)


@bp.route('/', methods=('GET', 'POST'))
def calculate():
    if request.method == 'POST':
        start = time.time()
        input1 = int(request.form['num1'])
        inputs = [input1]
        formula = request.form['formula']
        if formula == 'ack':
            input2 = int(request.form['num2'])
            inputs.append(input2)
            try:
                result = ackermann(input1, input2)
            except RecursionError:
                result = None
        elif formula == 'fact':
            result = factorial(input1)
        else:
            result = fibonacci(input1)

        calculation_ended = time.time()
        calc_time = calculation_ended - start

        return render_template(
            'auth/result.html', result=result, inputs=inputs, formula=formula, calc_time=calc_time)

    return render_template('auth/calculate.html')