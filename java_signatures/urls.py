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
    path("get_flappdeals_orders_count/", views.get_flappdeals_orders_count, name="get_flappdeals_orders_count"),
    path("get_flappdeals_orderId/", views.get_flappdeals_orderId, name="get_flappdeals_orderId"),
    path("get_practo_orders_count/", views.get_practo_orders_count, name="get_practo_orders_count"),
    path("get_practo_orderId/", views.get_practo_orderId, name="get_practo_orderId"),
    path("get_tamasha_users_count/", views.get_tamasha_users_count, name="get_tamasha_users_count"),
    path("get_tamasha_userId/", views.get_tamasha_userId, name="get_tamasha_userId"),
    path("get_cleartrip_ids_count/", views.get_cleartrip_ids_count, name="get_cleartrip_ids_count"),
    path("get_cleartrip_id/", views.get_cleartrip_id, name="get_cleartrip_id"),
    path("get_sololearn_users_count/", views.get_sololearn_users_count, name="get_sololearn_users_count"),
    path("get_sololearn_userId/", views.get_sololearn_userId, name="get_sololearn_userId"),
    path("get_petbook_orders_count/", views.get_petbook_orders_count, name="get_petbook_orders_count"),
    path("get_petbook_orderId/", views.get_petbook_orderId, name="get_petbook_orderId"),
    path("get_elelive_users_count/", views.get_elelive_users_count, name="get_elelive_users_count"),
    path("get_elelive_userId/", views.get_elelive_userId, name="get_elelive_userId"),
    path("get_ladygentleman_order/", views.get_ladygentleman_order, name="get_ladygentleman_order"),
    path("get_ladygentleman_order_count/", views.get_ladygentleman_order_count, name="get_ladygentleman_order_count"),
    path("get_styli_order/", views.get_styli_order, name="get_styli_order"),
    path("get_styli_order_count/", views.get_styli_order_count, name="get_styli_order_count"),
    path("get_pocket52_users_count/", views.get_pocket52_users_count, name="get_pocket52_users_count"),
    path("get_pocket52_userId/", views.get_pocket52_userId, name="get_pocket52_userId"),
    path("get_smytten_orders_count/", views.get_smytten_orders_count, name="get_smytten_orders_count"),
    path("get_smytten_orderId/", views.get_smytten_orderId, name="get_smytten_orderId"),
    path("get_lenskart_orders_count/", views.get_lenskart_orders_count, name="get_lenskart_orders_count"),
    path("get_lenskart_orderId/", views.get_lenskart_orderId, name="get_lenskart_orderId"),
    path("get_myteam11_userId_count/", views.get_myteam11_userId_count, name="get_myteam11_userId_count"),
    path("get_myteam11_userId/", views.get_myteam11_userId, name="get_myteam11_userId"),
    path("get_gamezy_users_count/", views.get_gamezy_users_count, name="get_gamezy_users_count"),
    path("get_gamezy_userId/", views.get_gamezy_userId, name="get_gamezy_userId"),
    path("get_galaxychat_userData/", views.get_galaxychat_userData, name="get_galaxychat_userData"),
    path("get_galaxychat_users_count/", views.get_galaxychat_users_count, name="get_galaxychat_users_count"),
    path("get_derma_orderData/", views.get_derma_orderData, name="get_derma_orderData"),
    path("get_derma_orders_count/", views.get_derma_orders_count, name="get_derma_orders_count"),
]