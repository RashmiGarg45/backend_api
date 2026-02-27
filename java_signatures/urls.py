from django.urls import path
from java_signatures import views

urlpatterns = [
    path("new_get_signature/", views.get_signtaure, name="get_signtaure"),
    path("add_install_count/", views.add_install_count, name="add_install_count"),
    path("update_event_count/", views.update_event_count, name="update_event_count"),
    path("event_allowed/", views.is_event_allowed, name="is_event_allowed"),
    path("new_ragazzo_signature/", views.ragazzo_signature, name="ragazzo_signature"),
    path("put_data/", views.put_data, name="put_data"),
    path("get_event_info/", views.get_event_info, name="get_event_info"),
    path("get_event_data/", views.get_data, name="get_data"),
    path("track_install", views.TrackInstalls.as_view(), name="save_install"),
    path("track_event", views.TrackEvents.as_view(), name="save_event"),
    path("is_event_allowed", views.checkEligibility.as_view(), name="check_eligibility"),
    path("is_eligible", views.EventCount.as_view(), name="check_count"),
    path("camps_running_status", views.camps_running_status.as_view(), name="check_status"),
    path('api/convert/', views.CurrencyConvertAPIView.as_view(), name='currency-convert'),
    path("stats", views.Running_camps_stats.as_view(), name="check_stats"),
    path("compare_stats", views.Compare_event_stats.as_view(), name="compare_stats"),
    path("install_data_health", views.InstallDataHealth.as_view(), name="install_data_health"),
    path("db_health", views.db_health.as_view(), name="db_health"),
    path("health", views.ServerHealth.as_view(), name='health'),
]