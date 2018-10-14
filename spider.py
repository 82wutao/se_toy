# -*- coding: utf-8 -*-


from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.meitulu.com/item/3037.html')
bs_obj = BeautifulSoup(html.read(),'html.parser')
text_list = bs_obj.find_all("img",attrs={"class":"content_img"})
for text in text_list:
    print(text.get("src"))
html.close()
