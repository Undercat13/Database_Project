from django.contrib import admin
from .models import Usertbl
# Register your models here.
#admin.site.register('django')#somehow add this for the database to show up in the admin

admin.site.register(Usertbl)