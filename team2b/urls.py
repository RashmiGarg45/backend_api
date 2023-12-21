from django.urls import path
from team2b import views

urlpatterns = [
    path("insertid/", views.OfferViewApi.as_view(), name="insert_id"),
]