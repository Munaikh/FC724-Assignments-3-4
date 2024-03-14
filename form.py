from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.choices import RadioField
from wtforms.fields.numeric import DecimalField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired


class Questionnaire(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    student_number = StringField('Student Number', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    gpa = DecimalField('What is your current GPA?', validators=[DataRequired()])
    teaching_satisfaction = RadioField('How satisfied are you with the quality of teaching at GIC?',
                                       choices=[('satisfied', 'Satisfied'), ('neutral', 'Neutral'),
                                                ('unsatisfied', 'Unsatisfied')],
                                       validators=[DataRequired()])
    teaching_improvement_areas = TextAreaField(
        'What are the areas where you think GIC can improve its teaching methods?')
    overall_experience = RadioField('How would you rate your overall experience at GIC?',
                                    choices=[('excellent', 'Excellent'), ('good', 'Good'), ('average', 'Average'),
                                             ('poor', 'Poor')],
                                    validators=[DataRequired()])
    experience_improvement_areas = TextAreaField(
        'What are the areas where you think GIC can improve its overall academic experience?')
    submit = SubmitField('Submit')
