from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import psutil

from datetime import datetime,timedelta
import json

from django.db.models import Count

class RestartAPIService(APIView):
    def get(self, request):
        if request.GET.get('neo')!='bottleofwater':
            return Response({
            'service':'Boom',
        })

        import psutil
        PROCNAME = "damraymining.py"

        for proc in psutil.process_iter():
            print(proc.name())
            # if PROCNAME in proc.name():
        
        return Response({
            'service':'restarted',
        })

