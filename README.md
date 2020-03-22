
# README #



### What is this repository for? ###

* This application is a simple web service written in Flask to calculate the result of three mathematical functions on user-defined inputs.
* Version 1.0.0

### How do I get set up? ###

* Running locally on development server
	* Download the repository
	* Create a virtual environment and activate it, more information [here.](https://flask.palletsprojects.com/en/1.1.x/installation/)
	* Inside the virtual environment run "pip install -e" to install the project, see [here.](https://flask.palletsprojects.com/en/1.1.x/tutorial/install/)
	* Set the environment variables FLASK_APP=calculator and FLASK_ENV=development
	* Type "python -m flask run" in the terminal
	* When in doubt refer to [this](https://flask.palletsprojects.com/en/1.1.x/tutorial/) or [this](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) tutorial.
* Dependencies are defined in setup.py (for local installation) and requirements.txt (for cloud deployment)
* To run the tests, type "python -m pytest" in the terminal when inside the virtual environment
* The app is deployed on Google App Engine based on [this tutorial](https://codelabs.developers.google.com/codelabs/cloud-vision-app-engine/) and is available to use [here.](https://ambient-inquiry-271918.appspot.com/) 

### Contribution guidelines ###

* The tests are defined in the folder "tests", one file per every module. When adding new test cases, simply define a function with one or more assertions, pytest runs them automatically.
 ### Known issues or bugs ###

* Ackermann function works only for small inputs
* Large outputs should be wrapped or displayed in a neater format
* Selenium tests to be implemented to test input validation on the front-end

### Who do I talk to? ###

* If you have any questions, don't hesitate to write to: viktorparipas@gmail.com