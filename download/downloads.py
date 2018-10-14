# -*- coding: utf-8 -*-


from urllib.request import urlopen

class Downloader(object):
    
    def __init__(self, user_agent):
        self._agent = user_agent
        pass


    def download(self,url):
        html = urlopen(url)
        doc = html.read()
        html.close()
        return doc



# from bs4 import BeautifulSoup

# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait 
# import selenium.webdriver.support.ui as ui

# import csv

# url = 'http://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0'
# driver = webdriver.PhantomJS()
# wait = ui.WebDriverWait(driver,70)

# csv_file = open('playlist.csv','w',newline='')
# csv_writer = csv.writer(csv_file)


# csv_writer.writerow(['title','playcount','link'])
# while url!='javascript:void(0)':
#     driver.get(url)
#     wait.until(lambda driver:driver.find_element_by_id('m-pl-container'))


#     driver.switch_to.frame('contentFrame')
#     data = driver.find_element_by_id('m-pl-container').find_elements_by_tag_name('li')

#     for i in range(len(data)):
#         nb = data[i].find_element_by_class_name('nb').text
#         if '万' in nb and int(nb.split('万')[0])>500:
#             msk = data[i].find_element_by_css_selector('a.msk')
#             csv_writer.writerow([msk.get_attribute('title'),nb,msk.get_attribute('href')])

#     url = driver.find_element_by_css_selector('a.zbtn.znxt').get_attribute('href')
# csv_file.close()

