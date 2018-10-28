# -*- coding: utf-8 -*-


from urllib.request import urlopen
from urllib.request import Request

from urllib.parse import urlencode


class Downloader(object):
    
    def __init__(self, user_agent=None):
        self._agent = user_agent
        pass

    def __merge_useragent_2_headers(self,headers):
        if headers is None:
            query_headers = dict()
        else:
            query_headers = dict(headers.items())

        if query_headers.get("User-Agent"):
            return query_headers
        if self._agent is None:
            return query_headers

        query_headers["User-Agent"] = self._agent
        return query_headers

    def __request(self,url,form,headers,method):
        request = Request(url, form, headers)
        request.get_method = lambda: method
        response = urlopen(request)

        url = response.geturl()
        status_code = response.getcode()
        if status_code != 200:
            return (url,status_code ,None,None)
        response_headers = dict(response.info().items())
        if method == 'HEAD':
            return (url, status_code, response_headers, None)
        document = response.read()
        return (url,status_code,response_headers,document)

    '''
    headers = { 
    'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  ,
    'Referer':'http://www.zhihu.com/articles' }  
    '''
    def get_method(self,url,parameters = None, headers = None):
        url = url+"?"+urlencode(parameters) if parameters is not None else url

        query_headers = self.__merge_useragent_2_headers(headers)

        return self.__request(url,None,query_headers,'GET')

    def post_method(self,url,form, headers = None):
        query_parameters = None
        query_headers = self.__merge_useragent_2_headers(headers)
        if form is not None:
            _parameters = dict(form.items())
            query_parameters = urlencode(_parameters).encode("utf-8")
        else:
            query_parameters = u"".encode("utf-8")

        return self.__request(url,query_parameters,query_headers,'POST')

    def head_method(self,url, headers = None):
        query_headers = self.__merge_useragent_2_headers(headers)
        return self.__request(url,None,query_headers,'HEAD')

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

