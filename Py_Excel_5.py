'''
    函数填充
'''
import pandas as pd

def add_2(x):
    return x + 2

books = pd.read_excel('./excel/bookm.xlsx',index_col='ID')
# books['Price'] = books['ListPrice'] * books['Discount']
# for i in books.index:
#     books['Price'].at[i] = books['ListPrice'].at[i] * books['Discount'].at[i]
# for i in range(5,16):
#     books['Price'].at[i] = books['ListPrice'].at[i] * books['Discount'].at[i]

# books['ListPrice'] = books['ListPrice'] + 2
# books['ListPrice'] = books['ListPrice'].apply(add_2)
books['ListPrice'] = books['ListPrice'].apply(lambda  x:x + 2)
print(books)









































