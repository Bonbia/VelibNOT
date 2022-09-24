import json
import requests
from collections import defaultdict
from email import message
from pushbullet import PushBullet
from pywebio.input import *
from pywebio.output import * 
from pywebio.session import *
import time

def aaa():
    access_token = "#YOUR PUSHBULLET ACCES TOKEN"
    pb = PushBullet(access_token)

   
    r=requests.get('https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_status.json')
    packages_json = r.json()

    n=len(packages_json['data']['stations'])

    def stat(n):
        for i in range (n):
            if packages_json['data']['stations'][i]['stationCode']=="#TON CODE DE STATION":
               return(packages_json['data']['stations'][i]['num_bikes_available_types'][0]['mechanical'])

    titre= 'Nombre de Velib mecanique:'
    message = str(stat(n))

    push = pb.push_note(titre, message)

while(True):
    curr = time.time()
    obj = time.localtime(curr)
    if obj.tm_hour==19 and obj.tm_min >=30 : #LE TEMPS QUE TU VEUX
        aaa()
        print(obj.tm_hour,obj.tm_min)
        time.sleep(10)
