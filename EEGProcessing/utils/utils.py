# -*- coding: UTF-8 -*-
"""
@Project: EEGProcessing_V3 
@File: utils.py
@IDE: PyCharm 
@Author: Xueqiang Wang
@Date: 2023/9/1 15:14 
@Description:  
"""

import datetime
from itertools import groupby
import scipy


def second2time(second):
    """
    Pass second, return time format %d:%H:%M:%S from 00:00:00:00
    :param second:
    :return:
    """

    return (datetime.datetime(2000, 1, 1, 0, 0, 0) + datetime.timedelta(seconds=second)).strftime("%d:%H:%M:%S")


def time_delta2second(str_time1, str_time2):
    str_time1 = [int(each) for each in str_time1.split(":")]
    str_time2 = [int(each) for each in str_time2.split(":")]
    return int((datetime.datetime(2000, 1, str_time2[0], str_time2[1], str_time2[2], str_time2[3]) -
                datetime.datetime(2000, 1, str_time1[0], str_time1[1], str_time1[2], str_time1[3])).total_seconds())


def str_time2second(str_time):
    """

    :param str_time: dd:HH:MM:SS
    :return:
    """

    return int((datetime.datetime.strptime(str_time, "y%/m%/%d %H:%M:%S") -
                datetime.datetime(1900, 1, 1, 0, 0, 0)).total_seconds())


def lst2group(pre_lst):
    """
    Convert a list like [[1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 1], [7, 1], [8, 1], [9, 3], [10, 3]] to
    [[1, 5, 2], [6, 8, 1], [9, 10, 3]]
    :param pre_lst:
    :return:
    """

    # Convert to [[[1, 2], [2, 2], [3, 2], [4, 2], [5, 2]], [[6, 1], [7, 1], [8, 1]], [[9, 3], [10, 3]]]
    pre_lst = [list(group) for idx, group in groupby(pre_lst, key=lambda x: x[1])]

    # Convert to [[1, 5, 2], [6, 8, 1], [9, 10, 3]]
    return [[each[0][0], each[-1][0], each[0][1]] for each in pre_lst]


def down_sample(raw_data, data_point_num):
    """
    Down sample the data when there are too many data point in a row data
    :return:
    """

    return scipy.signal.resample(raw_data, num=data_point_num)




