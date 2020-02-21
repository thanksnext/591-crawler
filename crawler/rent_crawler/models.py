from __future__ import unicode_literals
from django.db import models
from mongoengine import *


connect('591_rent_db',host = 'localhost',port = 27017)

class data(Document):
    houseid = StringField(max_length=45)
    sex = StringField(max_length=45)
    update_time = StringField(max_length=45)
    price = StringField(max_length=45)
    shape = StringField(max_length=45)
    kind = StringField(max_length=45)
    region_id = StringField(max_length=45)
    region = StringField(max_length=45)
    section = StringField(max_length=45)
    street = StringField(max_length=45)
    addr = StringField(max_length=45)
    linkman = StringField(max_length=45)
    identity = StringField(max_length=45)
    mobile = StringField(max_length=45)
    telephone = StringField(max_length=45)

    # 指明連線的資料表名
    meta = {'collection':'rent',
            'strict': False}
    def __unicode__(self):
        return self.name



def fun_raw_sql_query(**kwargs):
    phone = kwargs.get('phone')
    if phone:
        result = data.objects.raw('SELECT * FROM rent_crawler WHERE telephone = %s', [phone])
    else:
        result = data.objects.raw('SELECT * FROM rent_crawler')
    return result