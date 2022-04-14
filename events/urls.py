from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:year>/<str:month>/', views.home, name="home"),
    path('add_event', views.add_event,name='add_event'),
    path('add_university', views.add_university, name='add_university'),
    path('add_rso', views.add_rso, name='add_rso'),
    path('add_review', views.add_review, name = 'add_review'),
    path('rso_list', views.rso_list, name = 'rso_list'),
    path('view_rso/<curr_rso>', views.view_rso, name = 'view_rso'),
    path('events_list', views.events_list, name = 'events_list'),
    path('view_event/<curr_event>', views.view_event, name = 'view_event'),
    path('universities_list', views.universities_list, name = 'universities_list'),
    path('view_university/<curr_uni>', views.view_university, name = 'view_university'),
    path('login_user', views.login_user, name="login_user"),
]
