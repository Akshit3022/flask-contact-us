from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email
import os

app = Flask(__name__)

app.config['secret_key'] = os.environ.get('SECRET_KEY')

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send')

# Route for the contact form
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # Process form data (e.g., send email)
        name = form.name.data
        email = form.email.data
        message = form.message.data
        # Here you can handle the form submission, for example, sending an email
        # For demonstration, just print the form data
        print(f"Name: {name}, Email: {email}, Message: {message}")
        return 'Thank you for your message!'
    return render_template('contact.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)