# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(1,10,30)
# 生成30个数字，范围是1-10，等差数列. np.logspace()是等比生成数字
plt.figure(figsize=(14, 6), dpi=80) #设置绘图区域的大小和像素
'''
     #两种设置坐标轴刻度的方法：
第一种：
plt.xlim(0, 12) # 确定x轴的范围为0-12
plt.ylim(-1,1) #确定y轴的范围为-1到1
第二种：
plt.xticks([1,2,3,4,5,6,7,8,9,10])#设置x轴的刻度线，括号内填数组
plt.yticks([-1,0,1])#设置x轴的刻度线，括号内填数组
    #把图片的中心设为原点(0,0),原封不动抄写即可
ax = plt.gca()   
ax.spines['right'].set_color('none')   
ax.spines['top'].set_color('none')    
ax.xaxis.set_ticks_position('bottom')   
ax.yaxis.set_ticks_position('left')         
ax.spines['bottom'].set_position(('data', 0))  
ax.spines['left'].set_position(('data', 0))
   #设置坐标轴名字的方法
plt.xlabel('variable x')
plt.ylabel('variable y')

    #设置图片的标题
plt.title('三角函数')
    
    #设置参考线
plt.axhline(y=0.0, c="r", ls="--", lw=2)
y：水平参考线的出发点 c：参考线的线条颜色
ls：参考线的线条风格 lw：参考线的线条宽度

    #在图片上加文字，加箭头等
plt.annotate('文字内容',xy=(x,y),xytext=(x1,y1),
 weight='bold', color='r',
 arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='r'))

第一个参数是添加的文字。 xy = (x,y) x,y 是想标准的点
xytext = (x1,y1) 是文字想放到哪个地方 weight 是字形，常用'light','normal','regular','bold'等
color 是字体，常用b, g, r   
arrowprops()设置了一个箭头

    #一张图里画多个图，并设置图例,以散点图为例
plt.scatter(x1,y1, label='0')
plt.scatter(x2,y2, label='1')
plt.legend()

   '''
plt.plot(x,np.sin(x),'-o')