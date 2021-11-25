import json
import re
import execjs
import requests
from requests import Session


url = 'http://match.yuanrenxue.com/match/13'
headers = {
            "User-Agent": "yuanrenxue.project",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "http://match.yuanrenxue.com/match/13"

           }
session = Session()
Session.headers = headers
cookies = requests.utils.cookiejar_from_dict({"sessionid": "09jtadcgi655kbf7vx3xyw43f3c57bfx"}, cookiejar=None, overwrite=True)
session.cookies=cookies
res = session.get(url=url)
script_text = re.findall(r"(cookie=.*)\+\';path=/\'", res.text, flags=re.S)[0]
js_funtion = "function get_cookie(){%s; return cookie}" %script_text
print(js_funtion)
cookie_ =  execjs.compile(js_funtion).call("get_cookie").split("=")
print(cookie_)
cookie = {
          "sessionid": "09jtadcgi655kbf7vx3xyw43f3c57bfx",
            cookie_[0]: cookie_[1],
          }
print(cookie)
cookies = requests.utils.cookiejar_from_dict(cookie, cookiejar=None, overwrite=False)
session.cookies=cookies
session.headers=headers
number_sum = 0
for index in range(1, 6):
    url = "http://match.yuanrenxue.com/api/match/13?page={}".format(index)
    if index ==1:
        url = "http://match.yuanrenxue.com/api/match/13"
    res = session.get(url=url)
    datas = json.loads(res.text)
    for data in datas['data']:
        number_sum += data['value']

print(number_sum)