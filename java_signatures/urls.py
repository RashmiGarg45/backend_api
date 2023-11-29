from django.urls import path
from java_signatures import views

urlpatterns = [
    path("get_signature/", views.get_signtaure, name="get_signtaure"),
    path("get_tatapalette_orders/", views.get_tatapalette_orders, name="get_tatapalette_orders")
]