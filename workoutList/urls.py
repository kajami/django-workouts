from django.contrib import admin
from django.urls import path
from workoutApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
    path('workouts/', views.home, name='home'),
    path('create/', views.create_workout, name='create_workout'),
    path('workouts/remove', views.remove, name='remove'),
    path('workouts/createCsv', views.createCsv, name='createCsv'),
]