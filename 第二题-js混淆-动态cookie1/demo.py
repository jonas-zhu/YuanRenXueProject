import json

import execjs
import requests

with open("./demo.js", mode='r', encoding='utf-8') as fp:
    js_fun = fp.read()
    js_fun_compile = execjs.compile(js_fun)

headers = {
            "User-Agent": "yuanrenxue.project",
            # "Cookie": "sessionid=gzu0o2gz1erwplduo3jozk6pcpgq1w79;"
           }
session = requests.Session()
session.headers = headers
cookie = {"m": js_fun_compile.call("get_cookie").split("=")[1].split(";")[0], "sessionid": "gzu0o2gz1erwplduo3jozk6pcpgq1w79"}
cookies = requests.utils.cookiejar_from_dict(cookie, cookiejar=None, overwrite=True)
session.cookies = cookies
number_sum = 0
for index in range(1, 6):
    url = "https://match.yuanrenxue.com/api/match/2?page={}".format(index)
    res = session.get(url=url, headers=headers)
    print(res.text)
    for data in json.loads(res.text)["data"]:
        number_sum += data['value']
print(number_sum)


