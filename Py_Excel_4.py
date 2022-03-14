'''
    数据区域读取填充
'''
import pandas as pd
from datetime import date,timedelta

def add_month(d,md):
    yd = md // 12
    m = d.month + md % 12
    if m != 12:
        yd += m // 12
        m = m % 12
    return date(d.year + yd, m, d.day)

books = pd.read_excel('./excel/book.xlsx',skiprows=3,usecols='C:F',index_col=None,dtype={'ID':str,'InStore':str,'Date':str})
start = date(2018,1,1)
# for i in books.index: # --通过Series去改值
#     books['ID'].at[i] = i + 1
#     books['InStore'].at[i] = 'Yes' if i % 2 == 0 else 'NO'
#     # books['Date'].at[i] = start + timedelta(days=i) # --日
#     # books['Date'].at[i] = date(start.year + i,start.month,start.day)  # --年
#     books['Date'].at[i] = add_month(start,i) # --月

for i in books.index: # --通过DataFrame去改值
    books.at[i,'ID'] = i + 1
    books.at[i,'InStore'] = 'Yes' if i % 2 == 0 else 'NO'
    # books['Date'].at[i] = start + timedelta(days=i) # --日
    # books['Date'].at[i] = date(start.year + i,start.month,start.day)  # --年
    books.at[i,'Date'] = add_month(start,i) # --月
books.set_index('ID',inplace=True)
books.to_excel('./excel/book2.xlsx')
print('--end--')