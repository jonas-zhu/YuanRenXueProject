import base64
import json
import requests
from scrapy.selector import Selector


st = 'hello world!'.encode()
res = base64.b64encode(st).decode()
headers = {"User-Agent": "yuanrenxue.project",
           "Cookie": "sessionid=09jtadcgi655kbf7vx3xyw43f3c57bfx"}

number_sum = 0
for index in range(1, 6):
    m = base64.b64encode(('yuanrenxue'+str(index)).encode()).decode()
    url = "http://match.yuanrenxue.com/api/match/12?page={}&m={}".format(index, m)
    res = requests.get(url=url, headers=headers)
    datas = json.loads(res.text)
    print(datas)
    for data in datas['data']:
        number_sum += data['value']

print(number_sum)
# 172082
