# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     tool
   Description :
   Author :        Asdil
   date：          2019/12/26
-------------------------------------------------
   Change Activity:
                   2019/12/26:
-------------------------------------------------
"""
__author__ = 'Asdil'
import os
from tqdm import tqdm


def path_join(path1, path2):
    """
    合并两个目录
    :param path1:  路径
    :param path2:  文件名
    :return:
    """
    assert type(path1) is str
    assert type(path2) is str
    if path1[-1] != '/':
        path1 += '/'
    if path2[0] == '/':
        path2 = path2[1:]
    return path1+path2


def get_files(path, extension=None, key=None):
    """
    获取目标目录文件
    :param path:      路径
    :param extension: 后缀
    :param key:       关键字
    :return:
    """
    if extension is not None:
        length = -len(extension)
        ret = [path_join(path, each) for each in os.listdir(path) if each[length:] == extension]
    elif key is not None:
        ret = [path_join(path, each) for each in os.listdir(path) if key in each]
    else:
        ret = [path_join(path, each) for each in os.listdir(path)]
    return ret


def bar(data):
    """
    进度条
    :param data: 列表 字典 迭代器
    :return:
    """
    if isinstance(data, int):
        return tqdm(range(data))
    elif isinstance(data, list) or isinstance(data, dict):
        return tqdm(data)
    elif isinstance(data, iter):
        return tqdm(list(data))
    else:
        print('输入错误, 请输入int, list, dict')
