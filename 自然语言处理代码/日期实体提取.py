import re
from datetime import datetime,timedelta
from dateutil.parser import parse
import jieba.posseg as psg

def time_extract(text):
    time_res = []
    word = ''
    keyDate = {'今天':0,'明天':1,'后天':2}
    for k,v in psg.cut(text): #k是分好的词，v是词性
        if k in keyDate:
            if word != '':
                time_res.append(word)
            word = (datetime.today()+timedelta(days=keyDate.get(k,0))).strftime('%Y年%m月%d日')
        elif word != '':
            if v in ['m','t']:
                word = word + k
            else:
                time_res.append(word)
                word = ''
