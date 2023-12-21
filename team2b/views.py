from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from team2b.models import CheckEventCount,IndigoScriptOrderIds
# Create your views here.


class OfferViewApi(APIView):
    def get(self, request):
        query = IndigoScriptOrderIds()
        query.campaign_name = request.GET.get('camp_name','indigomoddteam2modd')
        query.id = request.GET.get('id')
        query.type = request.GET.get('id_type','pnr')
        query.used_at = None
        query.extra_details = request.GET.get('other_details','{}')
        query.save()
        return Response({
        })

