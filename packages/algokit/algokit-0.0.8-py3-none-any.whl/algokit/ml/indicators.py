"""
各种模型评价指标
"""
import numpy as np
import pandas as pd


def mape_matrix(X: np.ndarray, W: np.ndarray, Y: np.ndarray):
    """
    MAPE of each line of matrix
    """
    try:
        m = np.abs(Y - np.matmul(X, W)) * 1.0 / Y
        return m
    except:
        raise Exception("parameter must numpy array")


def mape_value(x, w, y):
    return abs(y-w*x)*1.0/y


def mape_dataframe(df:pd.DataFrame, xcols:list, ycols:list, W):
    """
    对pandas数据集进行计算
    :param df:
    :param xcols:
    :param ycols:
    :param w:
    :return:
    """
    X = np.array(df[xcols].values)
    Y = np.array(df[ycols].values)
    if isinstance(W, (pd.DataFrame, pd.Series)):
        W = np.array(W.values)
    elif isinstance(W, list):
        W = np.array(W)
    return mape_matrix(X,W,Y)


if __name__ == '__main__':
    x = np.array([[1,2],[3,4]])
    y = np.array([1,2])
    w = np.array([0.1,0.2])
    print(type(w))
    print(mape_matrix(x,w,y))

