# -*- coding: utf-8 -*-

from download.downloads import Downloader
from download.parse import parses
from download.config import Agent_Firefox

if __name__ == "__main__":
    downloader = Downloader(Agent_Firefox)
    url,code, headers,doc = downloader.get_method("http://www.77e77e.com/vod/18-15.html")
    links = parses.extract_links("http://www.77e77e.com/vod/18-15.html",doc,None,None)
    for link in links:
        print(link)

