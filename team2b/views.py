from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from team2b.models import CheckEventCount,IndigoScriptOrderIds,IgpScriptOrderIds
# Create your views here.
from datetime import datetime,timedelta

class Indigo(APIView):
    def put(self, request):
        query = IndigoScriptOrderIds()
        query.campaign_name = request.GET.get('camp_name','indigomoddteam2modd')
        query.id = request.GET.get('id')
        query.type = request.GET.get('id_type','pnr')
        query.departure_date=datetime.strptime(request.GET.get('departure_date'),'%Y-%m-%d %H:%M:%S')
        query.booking_date=datetime.strptime(request.GET.get('booking_date'),'%Y-%m-%d %H:%M:%S')
        query.used_at = None
        query.extra_details = request.GET.get('other_details','{}')
        query.save()
        return Response({
        })

    def get(self, request):
        query = IndigoScriptOrderIds()
        departure_date=datetime.strptime(request.GET.get('departure_date'),'%Y-%m-%d %H:%M:%S')
        booking_date=datetime.strptime(request.GET.get('booking_date'),'%Y-%m-%d %H:%M:%S')
        query.used_at = None
        query.save()
        return Response({
        })

    def post(self, request):
        query = IndigoScriptOrderIds.objects.filter(id=request.GET.get('id'))
        if query:
            query.used_at = datetime.now()
            query.save()
        return Response({
        })

class IGP(APIView):
    def put(self, request):
        query = IgpScriptOrderIds()
        query.campaign_name = request.GET.get('camp_name','igpmodd')
        query.id = request.GET.get('id')
        query.type = request.GET.get('id_type','order_id')
        if request.GET.get('delivered_date'):
            query.delivered_date=datetime.strptime(request.GET.get('delivered_date'),'%Y-%m-%d %H:%M:%S')
        query.booking_date=datetime.strptime(request.GET.get('booking_date'),'%Y-%m-%d %H:%M:%S')
        query.used_at = None
        query.extra_details = request.GET.get('other_details','{}')
        query.save()
        return Response({
        })

    def get(self, request):
        delivered_date=datetime.strptime(request.GET.get('departure_date'),'%Y-%m-%d %H:%M:%S')
        booking_date=datetime.strptime(request.GET.get('booking_date'),'%Y-%m-%d %H:%M:%S')
        query = IgpScriptOrderIds.objects.filter(id=request.GET.get('id'))
        return Response({
        })

    def post(self, request):
        query = IgpScriptOrderIds.objects.filter(id=request.GET.get('id'))
        if query:
            query.used_at = datetime.now()
            query.save()
        return Response({
        })
