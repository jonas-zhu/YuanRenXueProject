# coding:utf-8
import json
import httpx

headers = {
            "User-Agent": "yuanrenxue.project",
            "Cookie": "sessionid=kvzwvuhg7d7qx2f2zzjz4wkzl3gamm19"
           }

num_number = 0
with httpx.Client(headers=headers, http2=True) as client:
    for page in range(1, 6):
        url = 'https://match.yuanrenxue.com/api/match/17?page={}'.format(page)
        res = client.get(url, timeout=10)
        print(res.status_code)
        print(res.text)
        datas = json.loads(res.text)['data']
        for data in datas:
            num_number += data['value']
print(num_number)
