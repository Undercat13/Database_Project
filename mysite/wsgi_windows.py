
import os
import sys
import site
from django.core.wsgi import get_wsgi_application

# add python site packages, you can use virtualenvs also
site.addsitedir("C:/Program files/python36/Lib/site-packages")

# Add the app's directory to the PYTHONPATH 
sys.path.append('C:/Users/hotsh/OneDrive/Documents/mysite') 
sys.path.append('C:/Users/hotsh/OneDrive/Documents/mysite/mysite')  

os.environ['DJANGO_SETTINGS_MODULE'] = 'my_project.settings' 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_project.settings")  
 
application = get_wsgi_application()