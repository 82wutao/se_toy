# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

def extract_links(document,include_pattern,exclude_pattern=None):
    dom = BeautifulSoup(document, 'html.parser')
    links = dom.find_all("a")
    for link in links:
        print("\t\t%s" % link)
    pass