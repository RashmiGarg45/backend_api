from django.urls import path
from java_signatures import views

urlpatterns = [
    path("get_signature/", views.get_signtaure, name="get_signtaure"),
    path("get_tatapalette_orders/", views.get_tatapalette_orders, name="get_tatapalette_orders"),
    path("get_available_orders_count/", views.get_available_orders_count, name="get_available_orders_count")
]