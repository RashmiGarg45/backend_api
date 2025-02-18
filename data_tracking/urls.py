from django.urls import path
from data_tracking import views
from data_tracking import report_view

urlpatterns = [
    path("report6/statistics", report_view.Report6Stats.as_view(), name="r6_stats"),    
    path("sheet/report6", report_view.Report6UpdateOnSheet.as_view(), name="r6_stats"),    
    path("chatbot/notify/bt_not_running_past_2_months", report_view.ChatBotNotRunLastTwoMonthLevel2.as_view(), name="bot"),  
    path("sheetUpdate/watcho", report_view.WatchoUpdateSheet.as_view(), name="bot"),    
    path("<str:package_name>/<path:path>", views.tracking, name="tracking"),    
]