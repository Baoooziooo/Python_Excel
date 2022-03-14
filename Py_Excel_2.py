'''
    读取excel文件
'''
import pandas as pd
import re
import os

get_file_name = os.listdir('./excel') # --使用os模块listdir函数获取./excel目录下所有文件名称
re_comp = re.compile('.*规划.*') # --创建一个正则表达式对象
for file_name in get_file_name: # --遍历listdir函数获取到的文件名称
    res = re_comp.findall(file_name) # --使用正则表达式对象获取到文件名
    if res:
        break
open_file_name = './excel/' + res[0] # --将文件名与路径整合
get_excel = pd.read_excel(open_file_name) # --使用pandas模块打开文件
get_oltip = input('输入OLTIP:')
get_oltcw = int(input('输入OLT槽位:'))
for i in get_excel.index:
    if get_excel['OLTIP'].at[i] == get_oltip:
        if get_excel['归属OLT槽位'].at[i] == get_oltcw:
            print('家宽:{}'.format(get_excel['PPPOESVLAN'].at[i]))
            print('电视:{}'.format(get_excel['OTVSVLAN'].at[i]))
            print('语音:{}'.format(get_excel['语音SVLAN'].at[i]))
# get_excel = pd.read_excel(open_file_name,header=1) # --header=n设置开始行,当第一行名称错误时可以修改此值,如果第一行为空则不需要修改
# get_excel = pd.read_excel(open_file_name,header=None) # --header=None设置不要开始行
# get_excel.columns = ['区县','OLTIP','OLT型号','归属BAS名称','归属汇聚交换机名称','归属OLT槽位','OLTIP+归属OLT槽位','单板型号','PPPOESVLAN','OTVSVLAN','语音SVLAN','备注'] # --手动设置开始行
# get_excel.set_index('区县',inplace=True) # --手动设置索引,inplace=True设置在已有基础上修改为索引,而不是新增索引,设置为索引的值columns将不在识别
# get_excel.to_excel(open_file_name) # --将修改保存到文件
# print('--shape打印表格行列--')
# print(get_excel.shape) # --.shape,获取这个表格有多少行多少列
# print('--columns打印表格列名--')
# print(get_excel.columns) # --.columns,获取这个表格的列名
# print('--head打印表格前多少行数据,默认5行--')
# print(get_excel.head(3)) # --.head,获取表格前n行数据
# print('--tail打印表格后多少行数据,默认5行--')
# print(get_excel.tail(3)) # --.tail,获取表格后n行数据

# get_excel = pd.read_excel(open_file_name,index_col='区县') # --index_col=xx,指定索引,系统将不在生成默认索引
# get_excel.to_excel(re.sub('\.xlsx','1.xlsx',open_file_name)) # --存储到新的文件
print('--end--')