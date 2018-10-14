# -*- coding: utf-8 -*-

from download.downloads import Downloader
from download.parse import parses

if __name__ == "__main__":
    downloader = Downloader("")
    url,code, headers,doc = downloader.get_method("http://www.sina.com.cn")
    parses.extract_links(doc,3)

