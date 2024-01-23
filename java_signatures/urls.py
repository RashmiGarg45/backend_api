from django.urls import path
from java_signatures import views

urlpatterns = [
    path("get_signature/", views.get_signtaure, name="get_signtaure"),
    path("get_tatapalette_orders/", views.get_tatapalette_orders, name="get_tatapalette_orders"),
    path("get_available_orders_count/", views.get_available_orders_count, name="get_available_orders_count"),
    path("add_install_count/", views.add_install_count, name="add_install_count"),
    path("update_event_count/", views.update_event_count, name="update_event_count"),
    path("event_allowed/", views.is_event_allowed, name="is_event_allowed"),
    path("get_univest_orders/", views.get_univest_orders, name="get_univest_orders"),
    path("get_univest_orders_count/", views.get_univest_orders_count, name="get_univest_orders_count"),
    path("get_zalora_orders/", views.get_zalora_orders, name="get_zalora_orders"),
    path("get_zalora_orders_count/", views.get_zalora_orders_count, name="get_zalora_orders_count"),
    path("update_zalora_orderid_status/", views.update_zalora_orderid_status, name="update_zalora_orderid_status"),
    path("ragazzo_signature/", views.ragazzo_signature, name="ragazzo_signature"),
    path("get_samco_user_data/", views.get_samco_user_data, name="get_samco_user_data"),
    path("get_samco_users_count/", views.get_samco_users_count, name="get_samco_users_count"),
]