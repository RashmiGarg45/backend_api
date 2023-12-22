from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from team2b.models import CheckEventCount,IndigoScriptOrderIds,IgpScriptOrderIds
# Create your views here.
from datetime import datetime,timedelta
import json

class Indigo(APIView):
    def put(self, request):
        data = IndigoScriptOrderIds.objects.filter(id=request.GET.get('id'))
        query = IndigoScriptOrderIds()
        query.campaign_name = request.data.get('camp_name','indigomoddteam2modd')
        query.id = request.data.get('pnr')
        query.type = request.data.get('id_type','pnr')
        query.departure_date=datetime.strptime(request.data.get('departure_date'),'%Y-%m-%d %H:%M:%S')
        query.booking_date=request.data.get('booking_date')
        query.used_at = None
        query.extra_details = request.data.get('other_details','{}')
        query.save()
        return Response({
        })

    def get(self, request):
        departure_date=datetime.now().strftime('%Y-%m-%d')
        setUsed = request.GET.get('set_used')
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        query = IndigoScriptOrderIds.objects.filter(used_at=None,departure_date__gte=departure_date).order_by('-booking_date').first()
        extra_details = query.extra_details
        
        data = {
                "booking_date": query.booking_date, 
                "usedAt": query.used_at, 
                "departure_date": query.departure_date, 
                "transaction_id": extra_details.get('transaction_id'),#[{"value": "113097902036", "key": "ReferenceNo"}], 
                "email": extra_details.get('email'),#"nrd981@gmail.com", 
                "flight_reference": extra_details.get('flight_reference'),#"20231227 6E5265 GWLBOM", 
                "departure_city": extra_details.get('departure_city'),#"GWL", 
                "pnr": query.id, 
                "fare": extra_details.get('fare'),#"6031.0", 
                "company": extra_details.get('company'),#null, 
                "arrival_date": extra_details.get('arrival_date'),#"2023-12-27T16:15:00", 
                "used": True if query.used_at else False,#false, 
                "arrival_city": extra_details.get('arrival_city'),#"BOM", 
                "pushed_at": query.created_at
         }
        if setUsed:
            query = IndigoScriptOrderIds.objects.filter(id=data.get('pnr')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data
        })

    def post(self, request):
        set_used = request.data.get('used')
        pnr = request.data.get('pnr')
        if set_used:
            query = IndigoScriptOrderIds.objects.filter(id=pnr)
            if query:
                query.used_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                query.save()
        else:
            query = IndigoScriptOrderIds.objects.filter(id=pnr)
            if query:
                query.used_at = None
                query.save()
        return Response({
            'used':set_used,
            'pnr':pnr
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
        setUsed = request.GET.get('set_used')
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        query = IgpScriptOrderIds.objects.filter(used_at=None).order_by('-delivered_date').first()
        data = {
            'id':query.id,
            'extra_details':query.extra_details,
            'booking_date':query.booking_date,
            'delivered_date':query.delivered_date
        }
        if setUsed:
            query = IgpScriptOrderIds.objects.filter(id=data.get('id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'data':data
        })
        

    def post(self, request):
        query = IgpScriptOrderIds.objects.filter(id=request.GET.get('id'))
        if query:
            query.used_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            query.save()
        return Response({
        })
