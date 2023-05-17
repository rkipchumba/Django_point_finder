### Django_API_point_finder

1. Django application with an API that receives a set of points on a grid as semicolon separated values. And then it finds the points that are closest to each other. Store the received set of points and the closest points on a DB.
2. also added an admin interface for viewing the stored points and implemented unit tests for the API endpoint

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

python 3.7

### PROJECT SETUP

# clone the repository

git clone https://github.com/rkipchumba/Django_point_finder.git

# cd into the directory

cd Django_point_finder

# In the terminal create the development database

python manage.py makemigrations
python manage.py migrate

# In the terminal Create Superuser for Admin Interface

python manage.py createsuperuser

- Follow the prompts to create a superuser account for accessing the admin interface

# Run the Development Serve

python manage.py runserver

The server should start running at http://127.0.0.1:8000/

# Access the Admin Interface

1. Open your web browser and navigate to http://127.0.0.1:8000/admin/.
2. Enter the superuser credentials you created earlier.
3. You should now have access to the admin interface where you can view and manage the stored points.

### Unit Tests

## run the following command to execute the unit tests

python manage.py test

You should see the test results indicating whether the API endpoint behaves as expected.
