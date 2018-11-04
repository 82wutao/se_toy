# -*- coding: utf-8 -*-


from common.parse import parses
import numpy as np

LOOP_MAX_LIMIT = 10000
a = 0.85
delta=0.00001
'''
求得有效的外链
'''


def effective_outer_link(url, doc):
    links = parses.extract_links(url, doc, None, None)

    ret_dict = dict()
    for link in links:
        if link == url:  # 外链和自己相等
            continue
        else:
            ret_dict.setdefault(link, 1)
    return ret_dict


def build_prVector_transformMatrix(page_enties):
    size = len(page_enties)
    transform_matrix = np.zeros([size, size], float)

    clmn_j = 0
    for (url, doc) in page_enties:
        links_dict = effective_outer_link(url, doc)
        links_num = len(links_dict)
        if links_num == 0:
            transform_matrix[:, clmn_j] = 1/size
        else:
            row_i = 0
            for page,doc in page_enties:
                link_2_page = links_dict.get(page)
                if link_2_page:
                    transform_matrix[row_i, clmn_j] = 1/links_num
                row_i = row_i + 1

        clmn_j = clmn_j + 1

    pr_vector = np.zeros([size, 1], float)
    pr_vector[:, 0] = 1/size
    return (pr_vector, transform_matrix)

'''
使用幂迭代法来进行收敛
'''
def convergence(transform_matrix, pr_vector):
    size = len(pr_vector)
    prob_next = 1-a
    b = prob_next/size
    b_matrix = np.zeros([size,1],float)
    for i in range(size):
        b_matrix[i,0]=b


    for i in range(LOOP_MAX_LIMIT):
        sigma = np.dot(transform_matrix, pr_vector)
        new_pr_vector = a * sigma + b_matrix 

        diff = 0
        for j in range(size):
            diff = diff + abs(new_pr_vector[j,0]-pr_vector[j,0])
        if diff <= delta:
            break    
        pr_vector = new_pr_vector
    return pr_vector

if __name__ == "__main__":
    # urls and docs
    page_enties=[]
    page_enties.append(("http://h/a","<html><head></head><body><a href='http://h/d'></a><a href='http://h/c'></a><a href='http://h/b'></a></body></html>")) 
    page_enties.append(("http://h/b","<html><head></head><body><a href='http://h/d'></a><a href='http://h/d'></a></body></html>")) 
    page_enties.append(("http://h/c","<html><head></head><body><a href='http://h/a'></a><a href='http://h/d'></a></body></html>")) 
    page_enties.append(("http://h/d","<html><head></head><body><a href='http://h/b'></a><a href='http://h/c'></a></body></html>")) 

    # matrix and pr_vector
    pr_vector,m=build_prVector_transformMatrix(page_enties)

    #con
    result = convergence(m,pr_vector)    
    print(result)
    # show
    pass