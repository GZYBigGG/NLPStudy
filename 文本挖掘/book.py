# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 19:50:01 2020

@author: gzy
"""
import nltk
#from nltk.book import *
import os
import re
import jieba
from wordcloud import WordCloud as wc
import matplotlib.pyplot as plt
'''
f = open('text.txt',encoding = 'UTF-8')
raw = f.read()
fd = nltk.FreqDist(raw)
l = sorted(fd.items(),key = lambda x:x[1],reverse = True)
print(l[:10])
raw = nltk.Text(raw)
raw.dispersion_plot(['之','若','去'])
'''
f = open('十九大.txt',encoding = 'UTF-8')
mytext = f.read()
l = jieba.lcut(mytext,use_paddle=True) #lcut返回list
mytext = " ".join(l) #返回的mytext是字符串
# 词频统计
count= {}
for word in l:
    if len(word)==1:
        continue
    else:
        count[word]=count.get(word,0)+1
items=list(count.items()) 
items.sort(key=lambda x:x[-1],reverse=True)
print(items[:10])
wordcloud = wc(font_path="C:\Windows\Fonts\STSONG.TTF",\
               background_color='white',scale = 10).generate(mytext)
plt.imshow(wordcloud, interpolation='bilinear')



