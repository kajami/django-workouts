from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse 
from workoutList import fbconf
import csv
import pyrebase

#initializes firebase
firebaseConfig = fbconf.firebaseConfig
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

def createCsv(request):
  workouts = db.child('treenit').get()
  workoutList = workouts.val()
  response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="workouts.csv"'},
  )
  writer = csv.writer(response)
  for key, value in workoutList.items():
    writer.writerow([value])

  return response

@login_required
def home(request):
    workouts = db.child('treenit').get()
    workoutsList = workouts.val()
    context = workoutsList
    return render(request, 'workoutApp/home.html', {'data': context})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, ("Login successful."))
            return redirect('/workouts/')
        else:
            messages.error(request, ("Login error, try again."))
            return redirect('/')
    else:
        return render(request, 'workoutApp/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, ("You were logged out."))
    return redirect('/')
    
@login_required
def create_workout(request):
    if request.method == "POST":
      date = request.POST['date']
      type = request.POST['type']
      workoutLength = request.POST['workoutLength']
      workout1 =  request.POST['workout1']
      workout2 =  request.POST['workout2']
      workout3 =  request.POST['workout3']
      workout4 =  request.POST['workout4']
      workout5 =  request.POST['workout5']
      workout6 =  request.POST['workout6']
      workout7 =  request.POST['workout7']
      workout8 =  request.POST['workout8']
      workout9 =  request.POST['workout9']
      workout10 =  request.POST['workout10']
      workout11 =  request.POST['workout11']
      workout12 =  request.POST['workout12']

      data = {
        'date': date,
        'type': type,
        'workoutLength': workoutLength,
        'workout1': workout1,
        'workout2': workout2,
        'workout3': workout3,
        'workout4': workout4,
        'workout5': workout5,
        'workout6': workout6,
        'workout7': workout7,
        'workout8': workout8,
        'workout9': workout9,
        'workout10': workout10,
        'workout11': workout11,
        'workout12': workout12,        
        }
      db.child('treenit').push(data)
      messages.success(request, ("New workout created!"))
      return redirect('/workouts/')
    else:
      return render(request, 'workoutApp/workout_create.html')

def remove(request):
    if request.method == "POST":
      id = request.POST['id']
      db.child("treenit").child(id).remove()
      messages.success(request, ("Workout deleted!"))
    return redirect('/workouts/')