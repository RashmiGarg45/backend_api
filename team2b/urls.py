from django.urls import path
from team2b import views

urlpatterns = [
    path("indigo", views.Indigo.as_view(), name="cru_pnr"),
    path("igp", views.IGP.as_view(), name="cru_igp"),
    path("mcdelivery", views.Mcdelivery.as_view(), name="cru_mcdelivery"),
    path("lightinthebox", views.LightInTheBoxAPI.as_view(), name="cru_lightinthebox"),
    path("dominosindo", views.DominosIndo.as_view(), name="cru_dominosindo"),
    path("ostinshop", views.OstinShop.as_view(), name="cru_ostinshop"),
    path("habib", views.HabibOrderIdConstants.as_view(), name="cru_ostinshop"),
    path("generic_functions", views.GenericScriptFunctions.as_view(), name="generic_functions"),
    
]