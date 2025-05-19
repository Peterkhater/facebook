from django.urls import path
from core import views

urlpatterns = [
    path('',views.logi, name='login')
]
