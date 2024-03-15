from flask import Flask, flash, redirect, url_for
from flask import render_template

from form import Questionnaire

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e9e8e8ab1b6ad27c85e0636305cac3c3cfd96aba4438dcf0fe3c1ed4061a7b2f'

@app.route('/')
def home():  # put application's code here
    return render_template('index.html')


@app.route('/information')
def information():
    return render_template('information.html')


@app.route('/dataCollection', methods=['GET', 'POST'])
def data_collection():
    form = Questionnaire()
    if form.is_submitted():
        # Handle form data
        name = form.name.data
        student_number = form.student_number.data
        email = form.email.data
        gpa = form.gpa.data
        teaching_satisfaction = form.teaching_satisfaction.data
        teaching_improvement_areas = form.teaching_improvement_areas.data
        overall_experience = form.overall_experience.data
        experience_improvement_areas = form.experience_improvement_areas.data

        try:
            with open('data.txt', 'a') as file:
                file.write(f'{name}, {student_number}, {email}, {gpa}, {teaching_satisfaction}, {teaching_improvement_areas}, {overall_experience}, {experience_improvement_areas}\n')
        except Exception as e:
            print(e)

        flash('Thank you for your feedback!', 'success')
        return redirect(url_for('data_collection'))
    return render_template('dataCollection.html', form=form)


if __name__ == '__main__':
    app.run()
