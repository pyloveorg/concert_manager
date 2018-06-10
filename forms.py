from flask_wtf import FlaskForm, Form
from wtforms import StringField, TextAreaField, SubmitField, validators, ValidationError


class ContactForm(Form):
  name = StringField("Imię",  [validators.DataRequired("Proszę wpisać imię.")])
  email = StringField("Email",  [validators.DataRequired("Proszę wpisać adres email."), validators.Email()])
  subject = StringField("Temat",  [validators.DataRequired("Proszę wpisać temat.")])
  message = TextAreaField("Wiadomość",  [validators.DataRequired("Proszę wpisac wiadomość.")])
  submit = SubmitField("Wyślij")


class SendMail(Form):
  tak = SubmitField("TAK", [validators.DataRequired()])
  nie = SubmitField("NIE", [validators.DataRequired()])
  message = TextAreaField("Wiadomość", [validators.DataRequired("Proszę wpisac wiadomość.")])




