import json
import requests
import execjs


headers = {
            "User-Agent": "yuanrenxue.project",
            # "Cookie": "sessionid=cj233x3l8smtunqpuh78isjljlvs9mey;"
           }

with open("./demo.js", mode='r', encoding='utf-8') as fp:
    js_fun = fp.read()
    js_fun_compile = execjs.compile(js_fun)


number_sum = 0
for index in range(1, 6):
    url = "http://match.yuanrenxue.com/api/match/15?m={}&page={}".format(js_fun_compile.call("get_m"), index)
    res = requests.get(url=url, headers=headers)
    print(res.text)
    for data in json.loads(res.text)["data"]:
        number_sum += data['value']
print(number_sum)