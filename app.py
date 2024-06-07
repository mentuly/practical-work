from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'

class AddBookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    submit = SubmitField('Add Book')

class SearchBookForm(FlaskForm):
    title = StringField('Title')
    author = StringField('Author')
    submit = SubmitField('Search Book')

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    form = AddBookForm()
    if form.validate_on_submit():
        flash(f"Book '{form.title.data}' by {form.author.data} added!", 'success')
        return redirect(url_for('add_book'))
    return render_template('add_book.html', form=form)

@app.route('/search', methods=['GET', 'POST'])
def search_book():
    form = SearchBookForm()
    if form.validate_on_submit():
        flash(f"Searching for books by '{form.author.data}' with title '{form.title.data}'", 'info')
        return redirect(url_for('search_book'))
    return render_template('search_book.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)