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

        def exec_cmd(cmd):
            import subprocess
            pop = subprocess.run(cmd, shell=True)
            return pop
        
        import psutil
        PROCNAME = request.GET.get('filename')
        ORDER_ID = request.GET.get('id')

        custom_command = request.GET.get('custom_command')
        xx = []
        for p in psutil.process_iter(['name', 'open_files']):
            if 'python' in p.info['name'].lower():
                for file in p.info['open_files'] or []:
                    if PROCNAME.lower() in file.path.lower():
                        print("[-] Killed :: %-5s %-10s %s" % (p.pid, p.info['name'][:10], file.path))
                        p_kill = psutil.Process(p.pid)
                        p_kill.terminate()
                        if not custom_command:
                            zz = exec_cmd('nohup python ~/mining/{}.py {}> {}.log &'.format(PROCNAME,ORDER_ID,PROCNAME))
                        else:
                            zz = exec_cmd(custom_command)
                        print(zz)
                        return Response({
                            'service':'restarted',
                        })
                    
        if not custom_command:
            zz = exec_cmd('nohup python ~/mining/{}.py {}> {}.log &'.format(PROCNAME,ORDER_ID,PROCNAME))
        else:
            zz = exec_cmd(custom_command)
        print(zz)

        return Response({
            'service':'process not found, please restart it manually',
        })

