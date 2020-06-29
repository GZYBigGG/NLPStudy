import re
from datetime import datetime,timedelta
from dateutil.parser import parse
import jieba.posseg as psg
text = '今天我真高兴啊'
for k,v in psg.cut(text):
    print(k+":"+v)