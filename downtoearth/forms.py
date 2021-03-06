from flask.ext.wtf import Form, TextField, TextAreaField, SelectField, DecimalField, IntegerField, DateField, RecaptchaField, BooleanField, TextAreaField, HiddenField
from flask_security.forms import RegisterForm, LoginForm
from flask.ext.wtf import Required, Regexp, Length, Email, URL, EqualTo, NumberRange, Recaptcha
from downtoearth import config, models

class AddItemForm(Form):
    store_name = SelectField(choices=models.list_restaurants_select())
    item_name = TextField()
    item_url = TextField()
    item_price = DecimalField()

