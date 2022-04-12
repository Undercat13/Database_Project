# Database_Project
open database hosting server, wamp or xampp ect.
got to tables create table "django" leave blank

open terminal run these commands
python manage.py makemigrations

python manage.py migrate

head back to phpadmin

copy past the sql text into the sql query( make sure django database is selected)
click run

then go back to the terminal and run this 

python manage.py inspectdb > models.py

also copy models.py into events/models.py

The sql querries should now show up in models.py
