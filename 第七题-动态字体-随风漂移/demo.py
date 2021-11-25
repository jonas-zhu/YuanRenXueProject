# coding:utf-8
import json
import re
import base64
import requests
from fontTools.ttLib import TTFont
from bs4 import BeautifulSoup


headers = {
    "User-Agent": "yuanrenxue.project",
    'Cookie': 'sessionid=kg8ym0vkcp101idc00rauaz2lxnxdveh'
}
font_glyf_dict = {
    '0': [[290, 718], [159, 729], [102, 618], [56, 529], [56, 187], [102, 97], [159, -14]],
    '1': [[305, 716], [267, 662], [155, 600], [114, 647], [114, 511], [199, 561], [269, 647]],
    '2': [[297, 718], [190, 718], [83, 591], [56, 465], [155, 546], [194, 616], [225, 666]],
    '3': [[305, 718], [214, 718], [155, 665], [77, 600], [78, 508], [163, 508], [143, 570]],
    '4': [[397, 716], [18, 225], [18, 193], [375, 193], [375, 0], [453, 0], [453, 193]],
    '5': [[119, 716], [78, 316], [145, 316], [159, 356], [220, 409], [252, 396], [290, 396]],
    '6': [[297, 718], [176, 718], [119, 618], [44, 523], [44, 332], [44, 161], [106, 92]],
    '7': [[78, 716], [78, 666], [437, 666], [185, 0], [267, 0], [532, 666], [532, 716]],
    '8': [[290, 718], [185, 718], [119, 665], [78, 666], [78, 529], [78, 482], [93, 445]],
    '9': [[279, 718], [186, 718], [44, 577], [44, 487], [44, 374], [111, 304], [164, 240]],
}


# woff文件转xml
def woff_to_xml(woff_content, file_name):
    with open('./font_files/{}.woff'.format(file_name), 'wb')as f:
        f.write(base64.b64decode(woff_content))
    font = TTFont('./font_files/{}.woff'.format(file_name))
    font.saveXML('./font_files/{}.xml'.format(file_name))

def get_font_dict(file_name):
    font_dict = {}
    with open('./font_files/{}.xml'.format(file_name), 'r', encoding='utf-8')as f:
        t = f.read()
    soup = BeautifulSoup(t, 'xml')
    ttg_list = soup.find_all('TTGlyph')
    for ttg in ttg_list:
        name = ttg.get('name')
        pts = ttg.find_all('contour')[0].find_all('pt')
        for key, values in font_glyf_dict.items():
            flag = True
            for index, value in enumerate(values):
                if index + 1 > len(pts):
                    continue
                x = int(pts[index].get('x'))
                y = int(pts[index].get('y'))
                if abs(x-value[0]) >= 100 or abs(y-value[1]) >= 100:
                    flag = False
            if flag:
                font_dict[name.replace("uni", "&#x")] = key
    return font_dict


all_number = []
# 1,请求api保存woff文件
for page in range(1, 6):
    url = 'https://match.yuanrenxue.com/api/match/7?page={}'.format(page)
    print(url)
    res = requests.get(url=url, headers=headers)
    result = json.loads(res.text)

    # 2, woff文件转xml
    woff = result['woff']
    woff_to_xml(woff, page)
    # 3,构造映射字典
    font_dict = get_font_dict(page)
    datas = result['data']
    for data in datas:
        values = data['value'].split(" ")
        number_ = int(''.join([font_dict[value] for value in values if value]))
        print(number_)
        all_number.append(number_)

names = ['极镀ギ紬荕', '爷灬霸气傀儡', '梦战苍穹', '傲世哥', 'мaη肆風聲', '一刀メ隔世', '横刀メ绝杀', 'Q不死你R死你', '魔帝殤邪', '封刀不再战', '倾城孤狼', '戎马江湖', '狂得像风', '影之哀伤', '謸氕づ独尊', '傲视狂杀', '追风之梦', '枭雄在世', '傲视之巅', '黑夜刺客', '占你心为王', '爷来取你狗命', '御风踏血', '凫矢暮城', '孤影メ残刀', '野区霸王', '噬血啸月', '风逝无迹', '帅的睡不着', '血色杀戮者', '冷视天下', '帅出新高度', '風狆瑬蒗', '灵魂禁锢', 'ヤ地狱篮枫ゞ', '溅血メ破天', '剑尊メ杀戮', '塞外う飛龍', '哥‘K纯帅', '逆風祈雨', '恣意踏江山', '望断、天涯路', '地獄惡灵', '疯狂メ孽杀', '寂月灭影', '骚年霸称帝王', '狂杀メ无赦', '死灵的哀伤', '撩妹界扛把子', '霸刀☆藐视天下', '潇洒又能打', '狂卩龙灬巅丷峰', '羁旅天涯.', '南宫沐风', '风恋绝尘', '剑下孤魂', '一蓑烟雨', '领域★倾战', '威龙丶断魂神狙', '辉煌战绩', '屎来运赚', '伱、Bu够档次', '九音引魂箫', '骨子里的傲气', '霸海断长空', '没枪也很狂', '死魂★之灵'];
max_number  = max(all_number)
max_index = all_number.index(max_number)
print("最大值是%d,下标是%d" % (max_number, max_index))
print(names[max_index+1])

# 最大值是9711,下标是29
# 冷视天下



'''
.notdef
3 unia698
0 unib143
6 unib723
4 unic291
2 unic864
5 unic962
1 unie159
7 unie895
9 unif753
8 unif791
'''
'''
.notdef
5 unia736
7 unia752
0 unib374
9 unib471
1 unib765
6 unib956
3 unib962
4 unic589
2 unic754
8 unie728
'''
