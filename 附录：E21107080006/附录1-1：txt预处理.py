#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 数据预处理
# 正常异常对比
# 计算异常点
# 改变信号发射点，求取异常点
# 画出路径

import os
import numpy as np
import glob
import openpyxl 
import xlwt
import xlwings as xw
import re
import pandas as pd


# In[2]:


txt_normal_path = '../E_code/data_txt_normal/'
excel_normal_path = '../E_code/data_excel_normal/'

txt_abnormal_path = '../E_code/data_txt_abnormal/'
excel_abnormal_path = '../E_code/data_excel_abnormal/'


# In[3]:


txt_normal_list = os.listdir(txt_normal_path)
total_nor_Num = len(txt_normal_list)
print(total_nor_Num)

txt_abnormal_list = os.listdir(txt_abnormal_path)
total_abnor_Num = len(txt_abnormal_list)
print(total_abnor_Num)


# In[4]:


# for i in range(total_nor_Num):
    
#     file_extension=os.path.splitext(txt_abnormal_list[i])[0]
    
# #     excel_name = excel_normal_path + file_extension + str('.xls')
#     excel_name = excel_abnormal_path + file_extension + str('.xls')
    
#     try:
#         f_txt_file = open(txt_abnormal_path + str(txt_abnormal_list[i]))
#         head = f_txt_file.readline()
#         xls = xlwt.Workbook()
        
#         sheet = xls.add_sheet('sheet', cell_overwrite_ok=True)
#         x = 0
#         while True:
#             a = f_txt_file.readline()
#             b = f_txt_file.readline()
#             c = f_txt_file.readline()
#             d = f_txt_file.readline()
#             i_total = a + b + c + d
#             if not a:
#                 break
#             for i in range(len(i_total.split(':'))):
#                 item = i_total.split(':')[i]
#                 sheet.write(x, i, item)
#             x += 1
#         f_txt_file.close()
#         xls.save(excel_name)
#     except:
#         raise 
        
        
        


# In[5]:


for i in range(total_nor_Num):
    
    file_extension=os.path.splitext(txt_abnormal_list[i])[0]
    
#     excel_name = excel_normal_path + file_extension + str('.xls')
    excel_name = excel_abnormal_path + file_extension + str('.xls')
    
    try:
        f_txt_file = open(txt_abnormal_path + str(txt_abnormal_list[i]))
        head = f_txt_file.readline()
        xls = xlwt.Workbook()
        sheet = xls.add_sheet('sheet', cell_overwrite_ok=True)
        x = 0
        while True:
            
            a = f_txt_file.readline()
            print(a)
            b = f_txt_file.readline()
            print(b)
            c = f_txt_file.readline()
            print(c)
            d = f_txt_file.readline()
            print(d)
            print('===============================================')
            
            
            # 此处加入判断，即对数据是否正确进行验证
            # 时间戳是否相同
            # 
            
            i_total = a + ':' +b + ':' + c + ':' + d
            if not a:
                break
            for i in range(len(i_total.split(':'))):
                item = i_total.split(':')[i]
                sheet.write(x, i, item)
            x += 1
        f_txt_file.close()
        xls.save(excel_name)
    except:
        raise 
        
        


# In[ ]:





# In[ ]:




