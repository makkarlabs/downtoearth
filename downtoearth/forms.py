from flask.ext.wtf import Form, TextField, TextAreaField, SelectField, DecimalField, IntegerField, DateField, RecaptchaField, BooleanField, TextAreaField, HiddenField
from flask_security.forms import RegisterForm, LoginForm
from flask.ext.wtf import Required, Regexp, Length, Email, URL, EqualTo, NumberRange, Recaptcha
from flask_app import config

class ExtendedRegisterForm(RegisterForm):
    first_name = TextField('First Name', [Required()])
    last_name = TextField('Last Name', [Required()])
    organization = TextField('Organisation', [Required()])
    recaptcha = RecaptchaField([Recaptcha()])


