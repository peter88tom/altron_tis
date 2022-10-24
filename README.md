#How is the solution  implemented
A customer will fill in their information, then submit. Things that will happen after submitting:
1. Customer information(first_name, last_name, dob, and the uploaded excel file) will be saved to the SQLite database
2. Once the information are saved, the application will READ the data from the uploaded EXCEL file and save the data to the database
3. The application has GET method that return latest 12 customer financial information which then get called by a Javascript function which plots the graph of the financial information.


# How to setup and run this project in your local machine
To get this project up and running you should start by having latest version of Python installed on your computer. Install virtual environment in your computer like this
```
pip install virtualenv
```

Clone or download this repository. Open your terminal and change directory into the cloned directory, run the following command in the base directory of this project to create virtual environment

```
virtualenv env
```

That will create a new folder `env` in your project directory. Activate the virtual environment with this command on mac/linux:

```
source env/bin/active
```

Then install the project dependencies with this command

```
pip install -r requirements.txt
```

Run this command to make migrations, the command will create schemas for this project

```
python manage.py make migrations
```

Run this command to migrate the migrations, the command will create tables for this project

```
python manage.py migrate
```

Now you can run the project with this command

```
python manage.py runserver
```

Using the above command the project will be running on http://localhost:8000

# Tech stacks used to build this solution
- Python - [https://www.python.org/](https://www.python.org/)
- Django Python Framework - [https://www.djangoproject.com/](https://www.djangoproject.com/)
- Chart Js - [https://www.chartjs.org/](https://www.chartjs.org/)
- Bootstrap Frontend framework - [https://getbootstrap.com/](https://getbootstrap.com/)
- JQuery - [https://jquery.com/](https://jquery.com/)
- HTML
- CSS

