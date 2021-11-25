import json
import requests
import execjs
from collections import Counter

"""
hook eval，打印出eval最后执行成功的代码
eval_temp = eval;
eval = function (val){
    console.log(val);
    return eval_temp(val)
}
"""
# https://match.yuanrenxue.com/match/3

cookie = {
    "sessionid": "fmr0wxyvf6u9zyn4orvab55p420685t5",
}

headers = {
    'Host': 'match.yuanrenxue.com',
    'Connection': 'keep-alive',
    'Content-Length': '0',
    'User-Agent': 'yuanrenxue.project',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Origin': 'http://match.yuanrenxue.com',
    'Referer': 'http://match.yuanrenxue.com/match/3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

session = requests.Session()
session.headers = headers
cookies = requests.utils.cookiejar_from_dict(cookie, cookiejar=None, overwrite=True)
session.cookies = cookies


number_ls = []
for index in range(1, 6):
    session.post("https://match.yuanrenxue.com/jssm")
    url = "https://match.yuanrenxue.com/api/match/3?page={}".format(index)
    res = session.get(url=url)
    print(res.text)
    for data in json.loads(res.text)["data"]:
        number_ls.append(data['value'])
print(number_ls)
max_count_number = Counter(number_ls).most_common(1)
print(max_count_number)
print(type(max_count_number))
