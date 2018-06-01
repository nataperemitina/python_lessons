from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField
from wtforms.validators import InputRequired, Length, Email, Optional


class CustomerForm(FlaskForm):
    email = StringField('E-Mail',
                        validators=[
                            InputRequired(),
                            Length(min=3),
                            Email()
                        ])
    phone = StringField('Phone',
                        validators=[
                            Optional(),
                            Length(min=2, max=15)
                        ])
    name = StringField('Name',
                       validators=[
                           Optional(),
                           Length(min=2)
                       ])
