# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 13:16:12 2020

@author: gzy
"""
# encoding: utf-8

import random
import string
import time
import csv

company = []
relation = []
ID = set()  ###
NAME = []

# 模拟产生企业ID及NAME

for i in range(5000):
    # 模拟企业18位纳税人识别号

    id = random.randint(100000000,1000000000)
    id = str(id)
    #id = "'" + id

    # 模拟企业名称，随机生成的四个汉字

    first_name_val = random.randint(0x4e00, 0x5e95)
    second_name_val = random.randint(0x4e00, 0x5e95)
    third_name_val = random.randint(0x4e00, 0x5e95)
    fourth_name_val = random.randint(0x4e00, 0x5e95)

    first_name = chr(first_name_val)
    second_name = chr(second_name_val)
    third_name = chr(third_name_val)
    fourth_name = chr(fourth_name_val)

    name = first_name + second_name + third_name + fourth_name
    if id not in ID:  ###
        ID.add(id)    ####
        NAME.append(name)
        company.append([id,name])

ID = list(ID)
# 模拟产生企业间票流

for i in ID:  
    startID =  random.choice(ID)
    
    J = random.randint(0,10)
    
    for j in range(J):
        endID = random.choice(ID)
        if startID != endID:
            K = random.randint(0,10)
            for k in range(K):

                amount = random.randint(0,10000)
                Type = random.choice(string.ascii_uppercase)
                
                a1=(2019,1,1,0,0,0,0,0,0)                     # 设置开始日期时间元组
                a2=(2019,12,31,23,59,59,0,0,0)                # 设置结束日期时间元组
                start=time.mktime(a1)                         # 生成开始时间戳
                end=time.mktime(a2)                           # 生成结束时间戳
                t=random.randint(start,end)
                creat_time_touple=time.localtime(t)
                creat_time=time.strftime("%Y-%m-%d",creat_time_touple)

            
                relation.append((startID,endID,amount,Type,creat_time))
                
        else:
             continue


# 企业数据写入company.csv


with open(r'/data1/tq/neo4j-community-3.5.5/import/company.csv','w',newline='')as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['id:ID','name'])
    for string in company:
        writer.writerow(string)


# 关系数据写入relation.csv

with open(r'/data1/tq/neo4j-community-3.5.5/import/relation.csv','w',newline='')as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([':START_ID',':END_ID','amount:int',':Type','ctime:datetime'])
    for string in relation:
        writer.writerow(string)


# 输出企业数据及关系数据
# print(company)
# print(relation)





