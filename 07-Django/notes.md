# Create project
- django-admin startproject [projectname]

# Project Componentes
- __init__.py
- manage.py: perform users operations
- setting.py: settings of the applications, e.g. timezone, database
- urls.py: routes with urls and files. Asociate url with functions
- wsgi.py: common way to deploy to website
- project_name/

# Apps
Django projects can contain multiple apps. 
Create an app with python manage.py startapp [AppName]

# Migrations
It's de module to help maintain the interactions between database and models.
- Create a file with the changes for DB: python manage.py makemigrations
- Check the migrations changes as DB engine: python manage.py sqlmigrate flights 0001
- Execute migrations to DB: python manage.py migrate

You can add rows to db from the app shell.
```
python manage.py shell
from [appname].models import [classname]
row = [Classname](column1 = "nombre", column2 = "otra columna", columnX = 532)
row.save()
[Classname].objects.all()
[Classname].objects.get(pk=X)
```

You can also add rows to ManyToMany tables. For example, if you have flights and passangers (with a columns many to many) you can add flights for the passangers in the intermediate table like this:
```
f = Flight.object.get(pk=1)
p = Passanger.object.get(pk=1)
p.flights.add(f)
```

# Admin
Before adding the super user you have to makemigrations and migrate to let the app contain users model.
```
python manage.py createsuperuser
```
This will allow /admin built-in application.