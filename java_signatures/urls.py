from django.urls import path
from java_signatures import views

urlpatterns = [
    path("", views.get_signtaure, name="get_signtaure"),
]