# Test

## How to use

After install, open a terminal and activate the virtual ennviroment, move to the project path and type:

```bash
python manage.py runserver
```

The main path will be http://localhost:8000/.

You have a documentation for the api on http://localhost:8000/swagger/. Here you will see the end-poinst for the rest api.

## Install

### Clone this repository

If  you don't have git you can install it with:

```bash
apt install git
```

Open a terminal and move to the folder where you want to work. Then clone the repository using:

```bash
git clone https://github.com/LuisG93/test_crud.git
```

### Virtual enviroment

Install virtualenv.

```bash
sudo apt-get install python-virtualenv virtualenv
```

Create a virtualenv for the project.

```bash
virtualenv envname --python=python3
```

Activate the virtual ennviroment.

```bash
source envpath/envname/bin/activate
```

### Install python libraries

You can install the libraries with this instructions.

```bash
pip install -r requirements
```

### Initialize the database

Install postgres

```bash
sudo apt install postgres
```

Login as postgres user

```bash
sudo su - postgres
```

Start postgres in terminal

```bash
psql
```

Create a user for manage the database

```sql
CREATE ROLE luis LOGIN PASSWORD 'luis9325';
```

Create the database

```sql
CREATE DATABASE test OWNER luis;
```

### Migrations

When  you run this project for first time, you need to create the tables on the database. So you need to apply some migrations using Django.
Open a terminal and activate the virtual ennviroment, move to the project path and type:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create a superuser

Open a terminal and activate the virtual ennviroment, move to the project path and type:

```bash
python manage.py createsuperuser
```
