import requests
from bs4 import BeautifulSoup
import lxml
import os
import datetime

class GETIMAGES():
    def __init__(self):
        pass

    def writeCur(self,n):
        with open("date.txt",'w') as f:
            f.write(n)

    def get_images(self):
        week = datetime.date.today().isoweekday()
        with open("date.txt") as f:
            self.n=f.read()

        if week==1:
            self.n+=1
            self.writeCur(self.n)
        url="https://dxx.wwwtop.top/dxx_finish?a=12&b={}&d=0".format(self.n)
        re=requests.get(url=url)
        soup=BeautifulSoup(re.content,"lxml")
        imagesUrl=soup.find('img').get('src')
        image=requests.get(imagesUrl).content
        with open('dxxend.png','wb') as f:
            f.write(image)
        print("获取图片成功")
# if __name__ == '__main__':
#     ge=GETIMAGES()

#     ge.get_images()