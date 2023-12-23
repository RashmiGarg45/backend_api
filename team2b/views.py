from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from team2b.models import CheckEventCount,IndigoScriptOrderIds,IgpScriptOrderIds,McdeliveryScriptOrderIds

from datetime import datetime,timedelta
import json

from django.db.models import Count

class GenericScriptFunctions(APIView):
    def get(self, request):
        tablesDict = {
            'mcdelivery':McdeliveryScriptOrderIds,
            'indigo':IndigoScriptOrderIds
        }
        table = request.GET.get('table')
        today = datetime.now().strftime('%Y-%m-%d')
        used_count = tablesDict[table].objects.filter(used_at__contains=str(today)).aggregate(Count('used_at')).get('used_at__count')
        remaining_count = len(tablesDict[table].objects.filter(used_at=None))
        return Response({
            'used_count':used_count,
            'remaining_count':remaining_count
        })


class Indigo(APIView):
    def put(self, request):
        query = IndigoScriptOrderIds()
        query.campaign_name = request.data.get('camp_name','indigomoddteam2modd')
        query.id = request.data.get('pnr')
        query.type = request.data.get('id_type','pnr')
        query.departure_date=request.data.get('departure_date')
        query.booking_date=request.data.get('booking_date')
        query.used_at = None
        query.extra_details = request.data.get('other_details','{}')
        query.save()
        return Response({
        })

    def get(self, request):
        departure_date=datetime.now().strftime('%Y-%m-%d')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        pnr_used = IndigoScriptOrderIds.objects.filter(used_at__contains=str(departure_date)).aggregate(Count('used_at'))
        if pnr_used:
            pnr_used = pnr_used.get('used_at__count')

        data = {}
        if pnr_used<=100:
            query = IndigoScriptOrderIds.objects.filter(used_at=None,departure_date__gte=departure_date).order_by('-booking_date').first()
            extra_details = query.extra_details
            
            data = {
                    "booking_date": query.booking_date, 
                    "usedAt": query.used_at, 
                    "departure_date": query.departure_date.strftime('%Y-%m-%d %H:%M:%S'), 
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
            'body':data,
            'pnr_used':pnr_used+1
        })

    def post(self, request):
        set_used = request.data.get('used')
        pnr = request.data.get('pnr')
        channel = request.data.get('channel')
        offer_id = request.data.get('offer_id')
        network_name = request.data.get('network_name')
        if set_used:
            query = IndigoScriptOrderIds.objects.filter(id=pnr).first()
            custom_text = query.extra_details
            custom_text.update({
                'channel':channel,
                'offer_id':offer_id,
                'network_name':network_name,
            })
            IndigoScriptOrderIds.objects.filter(id=pnr).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),extra_details=custom_text)
        else:
            query = IndigoScriptOrderIds.objects.filter(id=pnr).update(used_at=None)
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


class Mcdelivery(APIView):
    def put(self, request):
        query = McdeliveryScriptOrderIds()
        query.campaign_name = request.data.get('camp_name','mcdeliverymodd')
        query.id = request.data.get('order_id')
        invoice_date = request.data.get('invoice_date')
        if request.data.get('invoice_time'):
            invoice_date += ' '+request.data.get('invoice_time')
        query.invoice_date_time = invoice_date
        query.address=request.data.get('address')
        query.gross_amount=request.data.get('gross_amount')
        query.member_name=request.data.get('member_name')
        query.used_at = None
        query.extra_details = request.data.get('other_details',{})
        query.save()
        return Response({
        })

    def get(self, request):
        invoice_date_time=datetime.now().strftime('%Y-%m-%d')
        setUsed = request.GET.get('set_used',True)
        if setUsed and (setUsed == 'False' or setUsed == 'false'):
            setUsed = False
        
        query = McdeliveryScriptOrderIds.objects.filter(used_at=None,invoice_date_time__gte=invoice_date_time).order_by('-invoice_date_time').first()
        
        data = {
                'order_id':query.id,
                'invoice_date':query.invoice_date_time.strftime('%Y-%m-%d'),
                'address':query.address,
                'gross_amount':query.gross_amount,
                'member_name':query.member_name,
                'used_at':query.used_at,
                'extra_details':query.extra_details,
        }
        if setUsed:
            query = McdeliveryScriptOrderIds.objects.filter(id=data.get('order_id')).update(used_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return Response({
            'body':data,
        })
