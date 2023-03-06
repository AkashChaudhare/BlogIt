# BlogIt

A blogging app styled with bootstrap with user authentication and password reset functionality

## Clone the repository

## Open terminal 
Go to project directory

## Create virtual environment
Run the following commands
```
pip install virtual env
virtualenv venv_name
```

## Activate virtual environment
```
venv_name\scripts\Activate
```

## Install all dependancies
```
pip install -r requirements.txt
```

## Prepare database
```
python manage.py makemigrations
python manage.py migrate
```

## Create a superuser to access admin panel
```
python manage.py createsuperuser
```
enter required details

## Start project
```
python manage.py runserver
```
