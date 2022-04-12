from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:year>/<str:month>/', views.home, name="home"),
    path('add_event', views.add_event,name='add_event'),
    path('add_university', views.add_university, name='add_university'),
    path('add_rso', views.add_rso, name='add_rso'),
    path('add_review', views.add_review, name = 'add_review')
]
