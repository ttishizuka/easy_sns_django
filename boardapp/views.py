from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .models import BoardModel
# Create your views here.
def signupfunc(request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    try:
        user = User.objects.create_user(username, '', password)
        return render(request, 'signup.html', {})
    except IntegrityError:
        return render(request, 'signup.html', {'error':'このユーザーは既に登録されています。'})
  return render(request, 'signup.html')

def loginfunc(request):
    if request.method == "POST":
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(request, username=username, password=password)
      if user is not None:
          login(request, user)
          return render(request, 'login.html', {'context':'logged in'})
      else:
          # Return an 'invalid login' error message.
          return render(request, 'login.html', {'context':'not logged in'})
    return render(request, 'login.html', {'context':'get method'})

def listfunc(request):
    object_list = BoardModel.objects.all()
    return render(request, 'list.html', {'object_list':object_list})
