# -*- coding: utf-8 -*-
import json
import requests

headers = {
            "User-Agent": "yuanrenxue.project",
            "Cookie": "sessionid=k6p0s3j0oe1w90f21znptuzzg0tbzq4h"
           }
number_sum = 0
number_index = 0
for index in range(1, 6):
    js_url = "http://127.0.0.1:3010/page_m"
    data = {"page_": index}
    page_m = requests.post(url=js_url, data=data)
    page_m = json.loads(page_m.text)
    print(page_m)
    url = 'http://match.yuanrenxue.com/api/match/1?page={}&m={}'.format(index, page_m['m'])
    res = requests.get(url=url, headers=headers)
    datas = json.loads(res.text)
    print(datas)
    for data in datas['data']:
        number_sum += data['value']
        number_index += 1

number_sum_pingjun = number_sum/number_index
print(number_sum_pingjun)
