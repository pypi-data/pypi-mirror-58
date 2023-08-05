#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Seaky
# @Date:   2019/8/28 10:04

import numpy as np
import pandas as pd

from .string import change_type
from ..os.oper import path_open


def set_none(df, other=None, **kwargs):
    '''将nan替换为None, 可以应用于series'''
    return df.where(pd.notnull(df), other=other, **kwargs)


def drop_nan(df, col):
    '''按某一列nan舍弃行'''
    return df[pd.notnull(df[col])]


def select_row(df, func):
    '''
    :param df:
    :param func: return True/False
    :return:
    '''
    df1 = df.apply(func, axis=1)
    return df1[df1]


def to_df(data, cols=None, black=None, sort_by=None, sort_force_number=False, sort_desc=False, index_disp=False,
          index_name=None, use_none=True, **kwargs):
    '''
    :param data    dict/list/df
    :param cols:   []
    :param black:  cols黑名单
    :param sort_by:    str/dict, 以字段排序
    :param sort_force_number:    sort_key转数字排序
    :param sort_desc:    降序
    :param index_disp:    显示index
    :param index_name:    index名字，index_name-> df.index.name-> 'index'
    :param use_none:   替换nan为None
    :param kwargs:
        orient: columns/index   dict的key
        columns: 如果orient为index，可以分配columns
    '''
    df = pd.DataFrame.from_dict(data, **kwargs) if isinstance(data, (dict, list)) else data
    if index_disp:
        index_name = index_name or df.index.name or 'index'
        df[index_name] = df.index
        df = df[list(df)[-1:] + list(df)[:-1]]
    if not isinstance(black, list):
        black = []
    if not isinstance(cols, list):
        cols = df.columns.tolist()
    df = df[[x for x in cols if x in df.columns.tolist() and x not in black]]
    if sort_by:
        origin_columns = df.columns.tolist()
        if isinstance(sort_by, str):
            sort_by = [sort_by]
        if sort_force_number:
            _sort_by = []
            for co in sort_by:
                if df[co].dtype == np.object:
                    # 强制转np.object为float
                    key = '_sort_{}'.format(co)
                    try:
                        df[key] = df[co].astype(float, errors='raise')
                    except Exception:
                        # 混合情况
                        df[key] = df[co].apply(change_type, to_type=float, default=0)
                    _sort_by.append(key)
                else:
                    _sort_by.append(co)
        else:
            _sort_by = sort_by
        df = df.sort_values(by=_sort_by, axis=0, ascending=not sort_desc, inplace=False)[origin_columns]
    if use_none:
        df = set_none(df)
    return df


def array_to_df(lst, index=None, columns=None, **kwargs):
    if not index:
        index = range(int(len(lst) / len(columns)))
    if not columns:
        columns = range(int(len(lst) / len(index)))
    return pd.DataFrame(np.array(lst).reshape(len(index), len(columns)), index=index, columns=columns, **kwargs)


def array_to_np(list, **kwargs):
    return np.array(list, **kwargs)


def add_columns(df, col, value, axis=1):
    '''
    :param df:
    :param col: str/list
    :param value:
        如果value是函数，如果如果col是list，则value需要是一个函数，返回list；如果col是str, value返回str。
        如果没有匹配，最好返回np.nan，可以后续dropna()
    :return:
    '''
    if hasattr(value, '__call__'):
        if isinstance(col, list):
            def func(*args, **kwargs):
                return pd.Series(value(*args, **kwargs))

            df[col] = df.apply(func, axis=axis)
        else:
            df[col] = df.apply(value, axis=axis)
    elif isinstance(value, dict):
        df[col] = pd.Series(value)
    elif isinstance(value, list):
        df[col] = value
    else:
        df[col] = value


def df_dump(df, path, mode='csv', **kwargs):
    if mode == 'pickle':
        df.to_pickle(path_open(path, 'w'), **kwargs)
    elif mode == 'csv':
        df.to_csv(path_open(path, 'w'), **kwargs)


def df_load(path, mode='csv', **kwargs):
    if mode == 'pickle':
        return pd.read_pickle(str(path), **kwargs)
    elif mode == 'csv':
        return pd.read_csv(str(path), **kwargs)


def change_df_type():
    '''
    1、pd.to_numeric(series)
    2、df['x'].astype(str)
    3、df = df.infer_objects()'''
    pass
