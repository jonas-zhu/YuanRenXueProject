import json
import requests
import execjs


headers = {
            "User-Agent": "yuanrenxue.project",
            "Cookie": "sessionid=b99zabxytwpuy2btioxg26kpzrc9qtdv;"
           }

with open("./demo.js", mode='r', encoding='utf-8') as fp:
    js_fun = fp.read()
    js_fun_compile = execjs.compile(js_fun)


number_sum = 0
for index in range(1, 6):
    t_m = js_fun_compile.call("get_m_t")
    url = "https://match.yuanrenxue.com/api/match/16?page={}&m={}&t={}".format(index, t_m['m'], t_m['t'])
    print(url)
    res = requests.get(url=url, headers=headers, verify=False)
    print(res.text)
    for data in json.loads(res.text)["data"]:
        number_sum += data['value']
print(number_sum)










