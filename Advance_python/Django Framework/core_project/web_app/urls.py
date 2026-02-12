from django.urls import path

from . import views
from web_app.views import employee, add_employee

urlpatterns = [
    path("", views.index, name="index" ),
    path('employee/', employee, name='employee'),
    path('add/', add_employee, name='add_employee'),
]