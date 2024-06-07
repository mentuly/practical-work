from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddBookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    submit = SubmitField('Add Book')

class SearchBookForm(FlaskForm):
    title = StringField('Title')
    author = StringField('Author')
    submit = SubmitField('Search Book')