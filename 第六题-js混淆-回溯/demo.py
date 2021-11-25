# coding:utf-8
import base64
import json
import time
from urllib import parse
import execjs
import requests

headers = {
    "User-Agent": "yuanrenxue.project",
    'Cookie': 'qpfccr=true; no-alert3=true; sessionid=hjax26n7nnetduj0314q975i1zsvpipr'
}

with open('./demo.js', mode='r', encoding='utf8') as fp:
    js_fun = fp.read().replace('\xa0', '')
    js_fun_compile = execjs.compile(js_fun)

q_ls = []
number_sum = 0
for page in range(1, 6):
    data = {}
    data['page'] = page
    js_result = js_fun_compile.call('get_m', page)
    now_time = js_result['now_time']
    m = js_result['m']
    q = '{}-{}|'.format(page, now_time)
    q_ls.append(q)
    data['m'] = m
    data['q'] = "".join(q_ls)
    url = 'https://match.yuanrenxue.com/api/match/6?' + parse.urlencode(data)
    print(url)
    res = requests.get(url=url, headers=headers)
    datas = json.loads(res.text)['data']
    print(res.status_code)
    print(datas)
    for data in datas:
        third_prize = data['value']
        second_prize = third_prize * 8
        first_prize = third_prize * 15
        number_sum += third_prize + second_prize + first_prize

print(number_sum)
