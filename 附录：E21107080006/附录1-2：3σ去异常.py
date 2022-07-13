#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 获取excel文件列表
# 读取每一个excel文件
# 获取A0、A1、A2、A3的值
# 进行正态分布计算
# 计算3μ的值
# 剔除脏数据

import os
import numpy as np
import pandas as pd
import xlwt


# In[2]:


excel_normal_path = '../E_code/data_excel_normal/'

excel_abnormal_path = '../E_code/data_excel_abnormal/'

norDist_excel_Normal_path = 'E:\\CodeProject\\AnacondaJupyter\\E_code\\norDist_excel_normal\\'

norDist_excel_abnormal_path = 'E:\\CodeProject\\AnacondaJupyter\\E_code\\norDist_excel_abnormal\\'


# In[3]:


normal_list = os.listdir(excel_normal_path)
normal_len = len(normal_list)

abnormal_list = os.listdir(excel_abnormal_path)
abnormal_len = len(abnormal_list)


# In[4]:


def abnormalDataProcessing(fileName, savePath, 
                           data0_mean, data0_std, data0_index,
                           data1_mean, data1_std, data1_index,
                           data2_mean, data2_std, data2_index,
                           data3_mean, data3_std, data3_index
                          ):
    
    sheetCheck = pd.read_excel(fileName).values
    
    data0_left = data0_mean - 3 * data0_std
    data0_right = data0_mean + 3 * data0_std
    
    data1_left = data1_mean - 3 * data1_std
    data1_right = data1_mean + 3 * data1_std
    
    data2_left = data2_mean - 3 * data2_std
    data2_right = data2_mean + 3 * data2_std
    
    data3_left = data3_mean - 3 * data3_std
    data3_right = data3_mean + 3 * data3_std
    
    x = 0
    save_excel_path = savePath
    workbook = xlwt.Workbook()
    sheetADD = workbook.add_sheet('sheetADD', cell_overwrite_ok=True)
    for i in range(sheetCheck.shape[0]):
#         if (sheetCheck[i][1] != sheetCheck[i][10] or
#             sheetCheck[i][1] != sheetCheck[i][19] or
#             sheetCheck[i][1] != sheetCheck[i][28] ):
            
        if (sheetCheck[i][5] >= data0_left and sheetCheck[i][5] <= data0_right and 
            sheetCheck[i][14] >= data1_left and sheetCheck[i][14] <= data1_right and
            sheetCheck[i][23] >= data2_left and sheetCheck[i][23] <= data2_right and
            sheetCheck[i][32] >= data3_left and sheetCheck[i][32] <= data3_right):

            try:
                for j in range(len(sheetCheck[i])):
                    item = sheetCheck[i][j]
                    sheetADD.write(x, j, item)
                x += 1
                workbook.save(save_excel_path)
            except:
                raise
        else:
            print('-------------------------------------')
#         else:
#             print('===================================')
            


# In[5]:


for j in range(abnormal_len):
    A0_tatol = []
    A1_tatol = []
    A2_tatol = []
    A3_tatol = []
    file_name = excel_abnormal_path + str(abnormal_list[j])    
    sheet = pd.read_excel(file_name).values
    for i in range(sheet.shape[0]):
        A0_tatol.append(sheet[i][5])
        A1_tatol.append(sheet[i][14])
        A2_tatol.append(sheet[i][23])
        A3_tatol.append(sheet[i][32])
#         print(sheet[i][5])
#         print(sheet[i][14])
#         print(sheet[i][23])
#         print(sheet[i][32])
#         print(sheet[i])
    
    #   标准差
    A0_std = np.std(A0_tatol)
    A1_std = np.std(A1_tatol)
    A2_std = np.std(A2_tatol)
    A3_std = np.std(A3_tatol)
#     print(A0_std)
    
    #   均值
    A0_mean = np.mean(A0_tatol)
    A1_mean = np.mean(A1_tatol)
    A2_mean = np.mean(A2_tatol)
    A3_mean = np.mean(A3_tatol)
    
    savePath = norDist_excel_abnormal_path + str(abnormal_list[j])  
    print(savePath)
    
    # 脏数据剔除
    abnormalDataProcessing(file_name, savePath,
                           A0_mean, A0_std, 5,
                           A1_mean, A1_std, 14,
                           A2_mean, A2_std, 23,
                           A3_mean, A3_std, 32
                          )
    
#     print('===================================')

