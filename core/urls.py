from django.urls import path
from core import views

urlpatterns = [
    path('',views.main,name='main'),
    path('login/',views.logi, name='login')
]
