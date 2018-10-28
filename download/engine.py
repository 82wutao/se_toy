# -*- coding: utf-8 -*-

from download.downloads import Downloader
from download.parse import parses
from download.config import Agent_Firefox

from store import store

if __name__ == "__main__":
    # downloader = Downloader(Agent_Firefox)
    # url,code, headers,doc = downloader.get_method("https://blog.csdn.net/jxw167")
    # links = parses.extract_links(url,doc,None,None)
    # store.store(url,doc,code,headers)

    collection=store.get_documents(0)
    for obj in collection:
        print(obj)
