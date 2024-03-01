  
# import serializer from rest_framework
from rest_framework import serializers
from data_tracking.models import revenueReport

class revenueReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = revenueReport
        fields = ['serial','date','channel','network','offer_id','package_name','campaign','r_install','payout','revenue','networkrevenue']
