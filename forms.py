from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, TextField, SubmitField, FloatField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    principle = IntegerField('Principle', validators=[DataRequired()])
    interestRateYear = FloatField('Interest rate per year', validators=[DataRequired()])
    periodYears = IntegerField('Loan period in years', validators=[DataRequired()])
    submit = SubmitField('Submit')