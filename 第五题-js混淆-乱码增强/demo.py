import json
import time

import requests


headers = {
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "User-Agent": "yuanrenxue.project",
    "Referer": "https://match.yuanrenxue.com/match/5",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8"
}
session = requests.Session()
session.headers = headers
js_url = "http://127.0.0.1:3011/get_cookie_m_f"
js_url_res = requests.get(url=js_url)
cookie_m_f = json.loads(js_url_res.text)
print(cookie_m_f)
cookie_dict = {}
for temp in cookie_m_f['cookie'].split("; "):
    cookie_dict[temp.split("=")[0]] = '='.join(temp.split("=")[1:])

cookie = {"sessionid": "zp2qzglxdneziyhqhpv69cq7pybuhuzl"}
cookie.update(cookie_dict)
cookies = requests.utils.cookiejar_from_dict(cookie, cookiejar=None, overwrite=True)
session.cookies = cookies

number_sum = []
for index in range(1, 6):
    url = "https://match.yuanrenxue.com/api/match/5?page={}&m={}&f={}".format(index, cookie_m_f['m'], cookie_m_f['f'])
    print(url)
    res = session.get(url=url)
    for data in json.loads(res.text)["data"]:
        print(data)
        number_sum.append(data['value'])

print(number_sum)
number_sum.sort()

print(number_sum)

print(number_sum[-5:])

print(sum(number_sum[-5:]))