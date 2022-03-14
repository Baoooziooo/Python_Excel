'''
    行,列,单元格
'''

import pandas as pd

S1 = [1,2,3]
S2 = [10,20,30]
S3 = [100,200,300]

s1 = pd.Series(S1,index=[1,2,3],name='A')
s2 = pd.Series(S2,index=[1,2,3],name='B')
s3 = pd.Series(S3,index=[2,3,4],name='C')

df = pd.DataFrame({s1.name:s1,s2.name:s2,s3.name:s3}) # --DataFramed的索引跟Series的索引是对其关系
# df = pd.DataFrame([s1,s2,s3])

print(df)



















































