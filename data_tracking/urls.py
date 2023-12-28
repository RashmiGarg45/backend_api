from django.urls import path
from data_tracking import views

urlpatterns = [
    path("<str:package_name>/<path:path>", views.tracking, name="tracking"),    
]