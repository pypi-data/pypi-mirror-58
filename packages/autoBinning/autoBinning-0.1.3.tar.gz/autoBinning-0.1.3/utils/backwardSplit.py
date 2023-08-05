# -*- coding: utf-8 -*-
from .trendSplit import *
import numpy as np
import copy
import math


class backwardSplit(trendSplit):
    def __init__(self, x, y, bad=1):
        trendSplit.__init__(self, x, y, bad)

    def fit(self, init_split=0, num_split=0, minv=0, sby='iv'):
        '''
        :param init_split: 备选初始切割点数
        :param num_split: 最大切割点数,不包含最大最小值
        :param minv: 最小分裂所需数值，woe/iv
        :param sby: 'iv','chi'
        :param min_sample: 每个分箱最小样本数
        :return: numpy array -- 切割点数组
        '''
        self.set_init()

        if init_split == 0 or len(self.x) <= init_split:
            self.everysplit()
        else:
            self.equalSize(init_split)

        candidate = []
        for r in self.range_dict:
            candidate.append(r[0])
            candidate.append(r[1])
        self.candidate = sorted(list(set(candidate)))

        param = {'minv': minv, 'sby': sby}
        cut = self.find_cut(**param)

        if cut:
            self.candidate.remove(cut)
            while True:
                cut = self.find_cut(**param)

                if cut:
                    self.candidate.remove(cut)
                else:
                    break

                if num_split:
                    #print(len(set(self.candidate)),num_split, self.candidate)
                    #print()
                    if len(set(self.candidate)) <= num_split:
                        break

            self.bins = np.array(sorted(list(set(self.candidate))))
        else:
            self.bins = None


    def find_cut(self,minv=0, num_split=0, sby='iv'):
        '''
        :param minv: 最小分裂所需数值，woe/iv
        :param sby: 'iv','chi'
        :param num_split: 最大切割点数,不包含最大最小值
        :return:
        '''

        cut = None
        if sby == 'chi':
            minv = 10**7
        if len(self.candidate)>num_split:
            for i in range(1, len(self.candidate)-1):
                candidate_list = [c for c in self.candidate if c!=self.candidate[i]]
                down_idx = candidate_list.index(self.candidate[i+1])
                iv_range = tuple(candidate_list)
                near_range_before = (self.candidate[i-1], self.candidate[i], self.candidate[i+1])

                if sby=='iv':
                    iv = self.cal_iv_by_range(iv_range)
                    if iv > minv:
                        minv = iv
                        cut = self.candidate[i]
                elif sby=='chi':
                    chi_v = self.cal_chisquare_by_range(near_range_before)
                    if chi_v < minv:
                        minv = chi_v
                        cut = self.candidate[i]
        return cut
