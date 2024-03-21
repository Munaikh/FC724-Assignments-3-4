# Importing the required libraries
from flask import Flask, redirect, render_template, url_for
from form import Questionnaire

# Creating an instance of the Flask class
app = Flask(__name__)

# Setting a random secret key for the application (required for displaying the form)
# without this, the form will not be displayed and an error will be thrown
# RuntimeError: A secret key is required to use CSRF.
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
        # Writing the data to a file
        try:
            with open("data.txt", "a") as file:
                # Writing the data to the file
                file.write(
                    str(form.data)
                )

        # Handling exceptions
        except Exception as e:
            print(e)

        # Redirecting the user to the home page after form submission
        return redirect(url_for("home"))
    return render_template("dataCollection.html", form=form) # passing the form object to the tampalet


# Running the application (Server)
if __name__ == "__main__":
    app.run()
