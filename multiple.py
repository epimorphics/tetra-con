import xlrd
from xlrd import open_workbook

file = 'Dover.xls'
workbook = xlrd.open_workbook(file)
sheet = workbook.sheet_by_index(0)

#sheet information
number_of_rows = sheet.nrows
number_of_columns = sheet.ncols
total_cells = number_of_rows * number_of_columns

x = ''
count = 0
count2 = 0    
for row_index in range(sheet.nrows):
    for col_index in range(sheet.ncols):
        if sheet.cell_value(row_index,col_index) == x:
            count += 1
        else:
            count2 +=1



print('this worksheet has {} rows and {} columns'.format(sheet.nrows, sheet.ncols))
print('this worksheet has {} cells'.format(total_cells))
print('number of empty cells: {} and number of cells with values {}'.format(count, count2))


#look at where the empty rows are

# x = ''
# count = 0
# y = 0
# z = 0
# for rows in range(sheet.nrows):
#     if(sheet.cell_value(rows,0) == x):
#         print('row {} is empty'.format(y)) 
#         y += 1
#         count += 1
        
#     else:
#         y += 1
        
# for cols in range(sheet.ncols):   #this is wrong
#     if(sheet.cell_value(cols,0)!= x):
#         print('column {} is empty'.format(z))
#         z += 1
#         count+= 1
#     else:
#         z += 1

#declare empty lists for the values
location = []
grid_ref = []
data1 = []
data2 = []


for i in range(sheet.nrows):                   #index over rows
    data1.append(sheet.cell_value(i,0))     #returns cell value of cell at row index is at, and column 0
    
#print(data1)  #this list is column 1

for i in range(sheet.ncols):               #reading a row
    data2.append(sheet.cell_value(9,i))
    street = data2[0]
    #grid =   data2[1]



for i in data1:
    print(i)




#print('bay info {i}'.format)