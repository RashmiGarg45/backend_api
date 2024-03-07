from django.urls import path
from team2b import views
from team2b import helper_apis

urlpatterns = [
    path("indigo", views.Indigo.as_view(), name="cru_pnr"),
    path("igp", views.IGP.as_view(), name="cru_igp"),
    path("mcdelivery", views.Mcdelivery.as_view(), name="cru_mcdelivery"),
    path("lightinthebox", views.LightInTheBoxAPI.as_view(), name="cru_lightinthebox"),
    path("dominosindo", views.DominosIndo.as_view(), name="cru_dominosindo"),
    path("ostinshop", views.OstinShop.as_view(), name="cru_ostinshop"),
    path("habib", views.HabibOrderIdConstants.as_view(), name="cru_ostinshop"),
    path("watcho", views.WatchoOrderIdsMiningAPI.as_view(), name="cru_watcho"),
    path("damnray", views.DamnRayMiningAPI.as_view(), name="cru_damnray"),
    path("pepperfry", views.PepperfryMiningAPI.as_view(), name="cru_damnray"),
    path("generic_functions", views.GenericScriptFunctions.as_view(), name="generic_functions"),
    path("restart_id_service", helper_apis.RestartAPIService.as_view(), name="restart_id_service"),
    
]