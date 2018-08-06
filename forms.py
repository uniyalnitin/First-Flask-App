from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class SearchForm(FlaskForm):
	what = StringField('What', validators=[DataRequired()])
	where = StringField('Where', validators=[DataRequired()])
	submit = SubmitField('find jobs')