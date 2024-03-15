# Importing necessary libraries
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.choices import RadioField
from wtforms.fields.numeric import DecimalField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired


class Questionnaire(FlaskForm):
    """A class that inherits from FlaskForm and contains the fields for the questionnaire form."""

    # createing variables to contain the fields for the form
    # Required name field
    name = StringField("Name", validators=[DataRequired()])

    # Required student number field
    student_number = StringField("Student Number", validators=[DataRequired()])

    # Required email field
    email = StringField("Email", validators=[DataRequired()])

    # Required GPA field
    gpa = DecimalField("What is your current GPA?", validators=[DataRequired()])

    # Required teaching satisfaction field
    teaching_satisfaction = RadioField(
        "How satisfied are you with the quality of teaching at GIC?",
        choices=[
            ("satisfied", "Satisfied"),
            ("neutral", "Neutral"),
            ("unsatisfied", "Unsatisfied"),
        ],
        validators=[DataRequired()],
    )

    # Teaching improvement areas field
    teaching_improvement_areas = TextAreaField(
        "What are the areas where you think GIC can improve its teaching methods?"
    )

    # Required overall experience field
    overall_experience = RadioField(
        "How would you rate your overall experience at GIC?",
        choices=[
            ("excellent", "Excellent"),
            ("good", "Good"),
            ("average", "Average"),
            ("poor", "Poor"),
        ],
        validators=[DataRequired()],
    )

    # Experience improvement areas field
    experience_improvement_areas = TextAreaField(
        "What are the areas where you think GIC can improve its overall academic experience?"
    )

    # Submit button
    submit = SubmitField("Submit")
