#!/usr/bin/env python3

import requests
import xml.etree.ElementTree as ET

uri = 'http://w2.dwar.mail.ru/hunt_conf.php?mode=hunt_farm&area_id={}&instance_id=0'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

def getItems(area_id, names):
    items = []
    r = requests.get(uri.format(area_id), headers=headers)
    if r.status_code == 200:
        print('Request is successful')
        root = ET.fromstring(r.text)
        for name in names:
            for item in root.findall('.//item[@name="{}"][@farming="1"]'.format(name)):
                i = item.attrib
                items.append({'name':i['name'],'x':int(i['x']),'y':int(i['y']), 'farming':int(i['farming'])})
        return items

    else:
        print('Some request error ', r.status_code, r.text)
        return false
