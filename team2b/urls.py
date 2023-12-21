from django.urls import path
from team2b import views

urlpatterns = [
    path("indigo", views.Indigo.as_view(), name="cru_pnr"),
    path("igp", views.IGP.as_view(), name="cru_igp"),
    
]