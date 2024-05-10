from flask import Flask, flash, render_template
from flask_wtf import FlaskForm 
from flask_wtf.recaptcha import RecaptchaField
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['RECAPTCHA_USE_SSL'] = False
app.config['RECAPTCHA_PUBLIC_KEY'] = os.environ.get('RECAPTCHA_PUBLIC_KEY')
app.config['RECAPTCHA_PRIVATE_KEY'] = os.environ.get('RECAPTCHA_PRIVATE_KEY')
app.config['RECAPTCHA_OPTIONS'] = {'theme': 'black'}
print("s_key",app.config['SECRET_KEY'])
# app.secret_key = 'FCx20gm4Lp'

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField('Send')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():

        name = form.name.data
        email = form.email.data
        message = form.message.data
        
        print(f"Name: {name}, Email: {email}, Message: {message}")

        flash(f"Name: {name}, Email: {email}, Message: {message}")
        # return 'Thank you for your message!'
    return render_template('contact.html', form=form)

if __name__ == '__main__':
    app.run(debug=True) 