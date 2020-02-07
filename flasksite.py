from flask import Flask, render_template, flash, url_for, redirect, request
from forms import InputForm
from ammortization_scehdule import ammortization
import os

app = Flask(__name__, static_folder="static", template_folder="templates")

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/', methods=['GET', 'POST'])
@app.route('/home')
def hello():
    form = InputForm()
    if form.validate_on_submit():
        principle = int(request.form['principle'])
        interestRateYear = float(request.form['interestRateYear'])
        periodYears = int(request.form['periodYears'])
        flash('Thanks for the information!')
        # return periodYears and principle and interestRateYear
        # return test(principle, interestRateYear, periodYears)
        return ammortization(principle, interestRateYear, periodYears)
        # return redirect(url_for('schedule'))
    return render_template('home.html', title='Input', form=form)

@app.route('/schedule', methods=['GET','POST'])
def schedule():
    return principle
    # return render_template('schedule.html')


@app.route('/about')
def about():
    # return 'hellllloooooo'
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
