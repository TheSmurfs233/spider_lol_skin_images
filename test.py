# -*- coding = utf-8 -*-
# @Time: 2020/7/26 19:58
# @Author:QAQ
# @File: test.py
# @Software: PyCharm

import requests
# url_temp = 'https://lol.qq.com/biz/hero/champion.js'
# response = requests.get(url_temp)
# html_temp = response.content.decode('utf-8')
# print(type(html_temp),html_temp)

# i = 2
# if len(i) == 1:
#     i = '00'+str(i)
#     print(i)
import re
# str = '{"Aatrox":{"id":"Aatrox","key":"266","name":"\u6697\u88d4\u5251\u9b54","title":"\u4e9a\u6258\u514b\u65af","tags":["Fighter","Tank"],"image":{"full":"Aatrox.png","sprite":"champion0.png","group":"champion","x":0,"y":0,"w":48,"h":48}}'
# regex = r'"key":"{}","name":"(.*?)","title":"(.*?)"'.format('266')
#
# a = re.findall(regex,str)
# print(a)
# b = a[0][0] +a[0][1]
# print(b)

response = requests.get('https://lol.qq.com/biz/hero/champion.js')
js_temp = response.content.decode('utf-8')
#print(type(js_temp),js_temp)
regex = '"key":"266","name":(.*?),"title":(.*?),'

name_data = re.findall(regex,js_temp)
name = eval(name_data[0][0])+eval(name_data[0][1])
print(name)








