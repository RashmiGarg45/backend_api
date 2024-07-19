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
    path("watcho/v2", views.WatchoOrderIdsMiningAPIV2.as_view(), name="cru_watcho"),
    path("damnray", views.DamnRayMiningAPI.as_view(), name="cru_damnray"),
    path("pepperfry", views.PepperfryMiningAPI.as_view(), name="cru_damnray"),
    path("mumzworld", views.MumzworldAPI.as_view(), name="cru_mumzworld"),
    path("tripsygames", views.TripsygamesAPI.as_view(), name="cru_tripsygames"),
    path("lazurit", views.LazuritAPI.as_view(), name='cru_lazurit'),
    path("gomcd", views.GomcdAPI.as_view(), name='cru_gomcd'),
    path("bharatmatrimony", views.BharatmatrimonyAPI.as_view(), name='cru_bharatmatrimony'),
    path("samsclub", views.SamsclubAPI.as_view(), name='cru_samsclub'),
    path("weworld", views.WeWorldAPI.as_view(), name='cru_weworld'),
    path("fantoss", views.FantossMiningAPI.as_view(), name='cru_fantoss'),
    path("okeyvip", views.OkeyvipMiningAPI.as_view(), name='cru_okeyvip'),
    path("sephora", views.SephoraMiningAPI.as_view(), name='cru_sephora'),
    path("puma", views.PumaMiningAPI.as_view(), name='cru_puma'),
    path("timoclub", views.TimoclubMiningAPI.as_view(), name='cru_timoclub'),
    path("email", views.EmailIdMiningAPI.as_view(), name='cru_email'),
    path("revenuedata", views.RevenueHelperAPI.as_view(), name='cru_revenuedata'),
    path("phonepestock", views.stock3Api.as_view(), name='phonepestock'),
    path("health", views.ServerHealth.as_view(), name='health'),
    path("fireEvent/player6", views.Player6API.as_view(), name='fireEvent_player6'),
    path("generic_functions", views.GenericScriptFunctions.as_view(), name="generic_functions"),
    path("generic_unusedId_functions", views.GenericUnusedIdScriptFunctions.as_view(), name="generic_unusedId_functions"),
    path("idsimulated", views.SimulatedIdFunction.as_view(), name="idsimulated"),
    path("apps_for_simulation", views.AppsForSimulation.as_view(), name="apps_idsimulated"),
    path("restart_id_service", helper_apis.RestartAPIService.as_view(), name="restart_id_service"),

    
]