#look at empty rows and try to find a way of identifying them
#xlrd stores cells as rectangular grids of cells
#cells with only formating are classified as blank, empty cells include those with empty string

import xlrd
from xlrd import open_workbook, empty_cell

file = 'Cannock Chase.xls'
#file = 'hackney.xlsx'
#file = 'East Devon.xls'
work_book = xlrd.open_workbook(file)
sheet = work_book.sheet_by_index(0)

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
row1 = sheet.row_values(0)
row2 = sheet.row_values(1)
row3 = sheet.row_values(2)
row4 = sheet.row_values(3)
x = ''
count = 0
y = 0
for rows in range(sheet.nrows):
    if(sheet.cell_value(rows,0) == x):
        print('row {} is empty'.format(y)) 
        y += 1
        count += 1
        
    else:
        y += 1
        









