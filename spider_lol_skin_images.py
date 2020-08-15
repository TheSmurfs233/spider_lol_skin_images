# -*- coding = utf-8 -*-
# @Time: 2020/7/26 19:36
# @Author:QAQ
# @File: spider_lol_skin_images.py
# @Software: PyCharm


import requests
import re
class LolSkinImagesSpider:
    def __init__(self): #初始化
        self.url_temp = 'https://lol.qq.com/biz/hero/champion.js'
        self.list_temp = self.askURL(self.url_temp)
        self.save_data()


    def get_url_list(self):
        url_temp = 'https://lol.qq.com/biz/hero/champion.js'
        response = requests.get(url_temp)
        html_temp = response.content.decode('utf-8')
        #print(type(html_temp),html_temp)
        regex = r'{"keys":(.*?),"data"'
        list_temp = re.findall(regex,html_temp)
        base_url = 'https://game.gtimg.cn/images/lol/act/img/skin/big{}{}.jpg'
        url_list = []
        #print(list_temp[0])
        for num in eval(list_temp[0]):
            #print(type(num),num)
            for i in range(25):
                i=str(i)
                if len(i) == 1:
                    i = '00'+str(i)
                    url_list.append(base_url.format(num,i))
                elif len(i) == 2:
                    i = '0' + str(i)
                    url_list.append(base_url.format(num, i))

        return url_list

    def get_images_save_path(self):

        save_path_list =[]
        response = requests.get('https://lol.qq.com/biz/hero/champion.js')
        js_temp = response.content.decode('utf-8')
        #print(js_temp)
        for num in eval(self.list_temp[0]):
            regex = r'"key":"{}","name":(.*?),"title":(.*?),'.format(num)
            name_data = re.findall(regex,js_temp)
            #print(name_data)
            for i in range(25):
                name = eval(name_data[0][0])+eval(name_data[0][1])+str(i)

                save_list_one = '.\\images\\{}.jpg'.format(name)
                save_path_list.append(save_list_one)
            #print(save_path_list)
        return save_path_list

    def askURL(self,url):
        response = requests.get(url)
        js_temp = response.content.decode('utf-8')
        regex = r'{"keys":(.*?),"data"'
        list_temp = re.findall(regex, js_temp)
        return list_temp

    def save_data(self):
        n = 0
        url_list =self.get_url_list()
        save_path_list = self.get_images_save_path()
        #print(url_list)
        for url in self.get_url_list():
            res = requests.get(url)
            if res.status_code == 200:
                print("正在下载:{}".format(url_list[n]))
                f = open(save_path_list[n],'wb')
                f.write(res.content)
                f.close()
            n += 1

    def run(self):
        LolSkinImagesSpider.get_url_list()
        LolSkinImagesSpider.get_images_save_path()
        LolSkinImagesSpider.save_data()


if __name__ == '__main__':
    LolSkinImagesSpider = LolSkinImagesSpider()
    LolSkinImagesSpider.run()
    print('爬取完毕')
