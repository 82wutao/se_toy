# -*- coding: UTF-8 -*-

import numpy as np

# 算矩阵，还是算页面，好像矩阵好算
def remove_deadend():
    pass


'''
根据当前rank和转移矩阵，迭代一次求得新的rank向量
'''
def calcLinksRank(transition_matrix,rank_vector):
    new_rank_vector = np.dot(transition_matrix, rank_vector)
    return new_rank_vector



#TODO 欧式还是余弦
def distanceOfRanks(rank_vector,new_rank_vector):
    dist = np.sqrt(np.sum(np.square(rank_vector - new_rank_vector)))
    return dist
