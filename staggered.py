#using the term staggered to describe date where the first row contains all data but subsequent rows ommit repeated values
#ie town, street, number of bays
#   Axebridge, church street, 2
#              high street,   2

import xlrd
import re
from xlrd import open_workbook, sheet, cellname

file = 'Hambleton.xlsx'
work_book = xlrd.open_workbook(file)
sheet = work_book.sheet_by_index(0)

print('worksheet has {} rows and {} columns'.format(sheet.nrows, sheet.ncols))

# count = 0
# for row_index in range(sheet.nrows):
#     if '' in sheet.row_values(row_index):
#         print(' row {} contains empty cells'.format(count))
#         count += 1
#         x = sheet.row_values(row_index)
    
#     else:
#         print(' row {} has values'.format(count))
#         count+= 1

# print(sheet.row_values(1)) #header
full =  sheet.row_values(3) #full set of values
partial = sheet.row_values(4) #partial values - need to make int not reading float values
# print(sheet.row_values(5)) #partial values

partial[3] = '67'
partial[4] = '2'

headers = sheet.row_values(1)
headers_clean = []

#removing the space from first element
car_park = headers[1]
remove = re.sub('[\s -]', '', car_park)
headers[1] = remove

disabled = headers[4]
remove2 = re.sub('\s', '', disabled)
headers[4] = remove2
print(headers)

# print(full)
# print(partial)

for i in range(len(partial)):
    if '' in partial[i]:
        partial[i] = full[0]

print(full)
