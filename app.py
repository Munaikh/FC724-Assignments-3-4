# Importing the required libraries
from flask import Flask, redirect, render_template, url_for
from form import Questionnaire

# Creating an instance of the Flask class
app = Flask(__name__)

# Setting a random secret key for the application (required for form submission)
app.config["SECRET_KEY"] = (
    "e9e8e8ab1b6ad27c85e0636305cac3c3cfd96aba4438dcf0fe3c1ed4061a7b2f"
)


# Creating a route for the home page
@app.route("/")
def home():
    """A function that renders the index.html file."""
    return render_template("index.html")


# Creating a route for the information page
@app.route("/information")
def information():
    """A function that renders the information.html file."""
    return render_template("information.html")


# Creating a route for the data collection page and handling the form submission
@app.route("/dataCollection", methods=["GET", "POST"])
def data_collection():
    """A function that handles the data collection form submission.

    Keyword arguments: None
    Return: A rendered template of the dataCollection.html file
    """

    # Creating an instance of the Questionnaire form
    form = Questionnaire()

    # Checking if the form has been submitted
    if form.is_submitted():
        # creating variables to contain the data from the form
        name = form.name.data
        student_number = form.student_number.data
        email = form.email.data
        gpa = form.gpa.data
        teaching_satisfaction = form.teaching_satisfaction.data
        teaching_improvement_areas = form.teaching_improvement_areas.data
        overall_experience = form.overall_experience.data
        experience_improvement_areas = form.experience_improvement_areas.data

        # Writing the data to a file
        try:
            with open("data.txt", "a") as file:
                # Writing the data to the file
                file.write(
                    f"{name}, {student_number}, {email}, {gpa}, {teaching_satisfaction}, {teaching_improvement_areas}, {overall_experience}, {experience_improvement_areas}\n"
                )

        # Handling exceptions
        except Exception as e:
            print(e)

        # Redirecting the user to the home page after form submission
        return redirect(url_for("home"))
    return render_template("dataCollection.html", form=form)


# Running the application (Server)
if __name__ == "__main__":
    app.run()
