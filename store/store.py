# -*- coding: UTF-8 -*-


from store import config
import json
import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

'''
这个由爬虫调用，来存储爬取结果
'''
def store(url, doc, status_code=200, response_headers=None):
    heads_json = "{}" if response_headers is None else json.dumps(response_headers)
    db = myclient["url_doc"]
    collections = db["urls"]

    mydict = {"url": url, "status":status_code,"headers":heads_json,"document":doc}
    collections.insert_one(mydict)

    pass


"""
一次默认取出100个文档来分析。
这个由分析模块来调用
"""
def get_documents(page_num=0,count=100):
    db = myclient["url_doc"]
    collections = db["urls"]

    offset = count * page_num
    total = count * (page_num+1)
    return collections.find().limit(total).skip(offset)


'''
存储某个url文档在关键字向量上的评分向量
这个由分析模块来调用
'''


def store_analysis_result(keyword_vector, rank_score_vector, url):
    pass


'''
查询一组关键字相应的url，按参数分页
'''


def query(keyword_vector, offset=0, limit=10):
    pass
