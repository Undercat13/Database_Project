from django.contrib import admin
from .models import Usertbl
from .models import Eventtbl
from .models import University
from .models import Rso
from .models import Review
# Register your models here.
#admin.site.register('django')#somehow add this for the database to show up in the admin

admin.site.register(Usertbl)
admin.site.register(Eventtbl)
admin.site.register(University)
admin.site.register(Rso)
admin.site.register(Review)