# How to use
After install, open a terminal and activate the virtual ennviroment, move to the project path and type:
python manage.py runserver

The main path will be 'http://localhost:8000/'.

You have a documentation for the api on 'http://localhost:8000/swagger/'. Here you will see the end-poinst for the rest api.

# Install

## Clone this repository
If  you don't have git you can install it with:
apt install git

Open a terminal and move to the folder where you want to work. Then clone the repository using:
git clone https://github.com/LuisG93/test_crud.git

## Virtual enviroment
Install virtualenv.
sudo apt-get install python-virtualenv virtualenv

Create a virtualenv for the project.
virtualenv envname --python=python3

Activate the virtual ennviroment.
source envpath/envname/bin/activate

## Install python libraries
You can install the libraries with this instructions.
pip install -r requirements

## Initialize the database
Install postgres
sudo apt install postgres

Login as postgres user
sudo su - postgres

Start postgres in terminal
psql

Create a user for manage the database
CREATE ROLE luis LOGIN PASSWORD 'luis9325';

Create the database
CREATE DATABASE test OWNER luis;

## Migrations
When  you run this project for first time, you need to create the tables on the database. So you need to apply some migrations using Django.
Open a terminal and activate the virtual ennviroment, move to the project path and type:
python manage.py makemigrations
python manage.py migrate

## Create a superuser
Open a terminal and activate the virtual ennviroment, move to the project path and type:
python manage.py createsuperuser
