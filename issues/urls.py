# Just a file in the specific app that incudes all of the URL's
from . import views
from django.urls import path

urlpatterns = [
    path('', views.issues, name="issues"),
]
