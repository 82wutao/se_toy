# -*- coding: utf-8 -*-

from download.downloads import Downloader

if __name__ == "__main__":
    downloader = Downloader("")
    resp = downloader.download("http://www.sina.com.cn")
    print(resp.decode('utf-8'))

