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


current sql
![image](https://user-images.githubusercontent.com/48971142/163459557-af80267d-075e-4219-8177-34fa8d887b9a.png)

the main differecnce are the: events_usertbl, events_usertbl_groups, events_usertbl_user_permissions.

1. events_usertbl its a copy of auth user with the additions of the usertbl we currently have
  ![image](https://user-images.githubusercontent.com/48971142/163459851-1adf76fa-9257-4a20-b422-84ff0354f70b.png)
2. events_usertbl_groups is a straight copy of auth_user_groups
3. events_usertbl_user_permissions is a straight copy of auth_user_permissions

there is most likely a better way to do this is what i found to work

the settings.py is already changed to suppor the custom user model
we can now login using the login_user page, these users can be created buy createsuperuser command to test this, also the admin page will show the user list for further testing
