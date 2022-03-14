'''
    初识pandas模块
'''
import pandas as pd

df = pd.DataFrame({'ID': [1, 2, 3],'Name':['小明','小张','小王']})
print('没设置索引:\n{}'.format(df)) # --没设置索引
df = df.set_index('ID') # --将ID列设置为索引
print('设置了索引:\n{}'.format(df)) # --设置了索引
df.to_excel('./excel/output.xlsx')
print('--end--')