# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 15:36:22 2020

@author: gzy
"""

import math

def L(x,y,p=2):
    # x = [1,1],y = [5,1]
    if len(x)==len(y) and len(x) > 1:
        sum = 0
        for i in range(len(x)):
            sum += pow(abs(x[i] - y[i]),p)
        sum = pow(sum,1/p)
        return sum
    else:
        return 0
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from collections import Counter
iris = load_iris()
df = pd.DataFrame(iris.data,columns = iris.feature_names)
df['label'] = iris.target
df.columns = ['sepal length', 'sepal width', 'petal length', 'petal width', 'label']
plt.scatter(df[:50]['sepal length'], df[:50]['sepal width'], label='0')
plt.scatter(df[50:100]['sepal length'], df[50:100]['sepal width'], label='1')
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.legend() # 添加图例
# loc：通过选取行（列）标签索引数据 
# iloc：通过选取行（列）位置编号索引数据
data = np.array(df.iloc[:100, [0, 1, -1]]) #data.ndim 可以看出data是二维数组
X, y = data[:,:-1], data[:,-1] 
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2)
class KNN:
    def __init__(self,X_train,y_train,n_neighbors =3, p=2):
        self.X_train = X_train
        self.y_train = y_train
        self.n=n_neighbors
        self.p = p
    def predict(self,X):
        #取出n个点
        knn_list = []
        for i in range(self.n):
            
        