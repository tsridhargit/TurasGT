
# Job Portal
This is a simple implementation of a job board website, developed using **Django** web framework and **Django Rest Framework (DRF)**.


</br>

## Run the project with Docker
To get started with this project using Docker, **clone the repository** and run this command:
```
docker compose up
```
sample **.env** files are in `.envs` directory.

</br>

## Run the project without Docker
To get started with this project without using Docker, **clone the repository** and follow these steps:

* Create a virtual environment and activate it
```
python3.10 -m venv venv
source venv/bin/activate
```

* Install the required packages
```
pip install -r requirements.txt
```

* Run `psql` and execute these commands:
```sql
CREATE DATABASE <database_name>;
CREATE USER <database_user>;
GRANT ALL PRIVILEGES ON DATABASE <database_name> TO <database_user>;
ALTER USER <database_user> WITH PASSWORD '<database_password>';
```

* Create a `````.env````` file in project root and add these configs
```python
SECRET_KEY='your_secret_key_generated_by_djecrety.ir'
DEBUG='debug status'
ALLOWED_HOSTS='*'

POSTGRES_DB='<database_name>'
POSTGRES_USER='<database_user>'
POSTGRES_PASSWORD='<database_password>'
POSTGRES_HOST='localhost'
POSTGRES_PORT=5432

EMAIL_HOST_USER='<your_email_host_user>'
EMAIL_HOST_PASSWORD='<your_email_host_password>'
```

* Run database migrations
```
python manage.py migrate
```

if you see this error message:
```
django.db.utils.ProgrammingError: permission denied to create extension "citext"
HINT:  Must be superuser to create this extension.
```
Just enter this command to your database shell:
```postgresql
ALTER ROLE jobnet SUPERUSER;
```

*  Start the development server
```
python manage.py runserver
```
