from django.urls import path
from Authentication import views
urlpatterns = [
    path('',views.login,name='login'),
    path('check',views.check,name='check'),
    path('registration',views.registration,name='registration'),
]
