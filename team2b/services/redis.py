from django_redis import get_redis_connection
from django.db import models
from datetime import datetime
import json

class Redis:
    def __init__(self):
        self.connection = get_redis_connection()
    
    def save(self, key, value, ttl=24*60*60):
        print('[{}] Saving {}:{} to redis'.format(datetime.now(),key,value))
        if isinstance(value,list) or isinstance(value,dict):
            value = json.dumps(value)
        self.connection.set(key, value, ttl)

    def retrieve_data(self,key):
        print('[{}] Getting {} from redis'.format(datetime.now(),key))
        raw_data = self.connection.get(key)
        try:
            data = json.loads(raw_data)
            return data
        except:
            return raw_data
    
    def get_ttl(self,key):
        print('[{}] Getting ttl for {} from redis'.format(datetime.now(),key))
        return self.connection.ttl(key)
    
    def update_ttl(self, key, ttl):
        print('[{}] Getting ttl for {} from redis'.format(datetime.now(),key))
        return self.connection.expire(key, ttl)