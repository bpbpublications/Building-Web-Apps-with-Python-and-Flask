from flask_wtf import FlaskForm
from wtforms import *
from wtforms import validators, ValidationError
class LoginForm(FlaskForm):
    username=StringField('username', [validators.InputRequired("This field can not be empty"), \
                               validators.Email("Please enter your email address.")])
    password=PasswordField('Enter Password',
                             [validators.InputRequired("This field can not be empty")])
    submit = SubmitField("Submit")
    


class Registration(FlaskForm):
    student=StringField("Name of Student",[validators.Required("Please enter your name.")])
    Gender = RadioField('Gender', choices=[('M','Male'),('F','Female')])
    course= SelectField('Course', choices=[('Flask', 'Python with Flask'), ('Java', 'Advanced Java'), \
                                           ('Cpp', 'C/C++'), ('DS', 'Data Science')])
    mobile=IntegerField('mobile')
    email = StringField("Email",[validators.Required("Please enter your email address."), \
                               validators.Email("Please enter your email address.")])
    submit = SubmitField("Submit")
    
class AdmissionForm(FlaskForm):
    student = StringField("Name", [validators.InputRequired("This field can not be empty")])
    Gender = RadioField('Gender', [validators.DataRequired('Choose Gende')],choices=[('M','Male'),('F','Female')])
    dob = DateField("Date of Birth", format="%d-%m-%Y")
    percent = DecimalField("passing percentage",
                           [validators.NumberRange(min=0, max=100, message="Invalid input")])
    branch= SelectField('Branch', choices=[('IT', 'Information Technology'),
                                           ('CS', 'Computer Engg.'), ('E&T', 'Electronics & Telecom')])
    userID = StringField('User Id', [validators.Length(min=4, max=8, message='ID length betn 4-8 chars')])
                        
    pwd = PasswordField('Enter Password',
                             [validators. EqualTo('confirm', message ='Passwords must match'),
                              validators.InputRequired("This field can not be empty")])
    confirm  = PasswordField('Re-type the password')

    submit = SubmitField('Submit')
    
