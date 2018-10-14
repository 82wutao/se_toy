# -*- coding: UTF-8 -*-


'''
这个由爬虫调用，来存储爬取结果
'''
def store(url, doc, status_code=200, response_headers=None):
    pass


'''
一次默认取出100个文档来分析。
这个由分析模块来调用
'''
def get_documents(count=100):
    pass

'''
存储某个url文档在关键字向量上的评分向量
这个由分析模块来调用
'''
def store_analysis_result(keyword_vector,rank_score_vector,url):
    pass

'''
查询一组关键字相应的url，按参数分页
'''
def query(keyword_vector,offset=0,limit=10):
    pass
