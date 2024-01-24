from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email, EqualTo


class RegistrationForm(FlaskForm):
    
    first_name = StringField('Имя',validators=[DataRequired()])
    second_name = StringField('Фамилия',validators=[DataRequired()])
    email= StringField('email',validators=[DataRequired(),Email()])
    password = PasswordField('password',validators=[DataRequired()])
    