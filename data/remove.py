import xlrd
import xlrd 
import re
import rdflib
from rdflib import Graph, URIRef,Literal, RDFS, Namespace
from rdflib.namespace import XSD

from xlrd import open_workbook, cellname, empty_cell

#to remove headers we need to remove empty cells, blanks, ','
#find and match on target values 
#appears we cannot loop over a list and drop or remove elements

#read xls excel format #, encoding=''

#book = open_workbook('Poole.xls')
book = open_workbook('Purbeck.xlsx')
sheet = book.sheet_by_index(0)

#get an idea of the size of the sheet
# print('file has {} worksheets '.format(book.nsheets))
# print('file has {} rows '.format(sheet.nrows))
# print('file has {} columns '.format(sheet.ncols))

#method 1 use the first param of range() to manual start at a specified row
three = 3
eight = 8
for row_index in range(eight,sheet.nrows):
    #print(sheet.row(row_index))
    print(sheet.row_values(row_index))

#empty cells can be checked with python identity check
#Cells where no information is present in the Excel file are represented by the xlrd.XL_CELL_EMPTY 

#print(sheet.cell(0,0).value) #reads the value of a cell

#using range is not working
# for i in range(sheet.nrows):    
#     #print(sheet.cell_value(i,0)) #reads the first column
#     carpark = sheet.cell_value(i,0) #rowx, columnx                 - returns one cell
#     carpark2 = sheet.row_slice(0)    #row index start, finish, end - returns a list of cell objects
#     carpark3 = sheet.row_values(5)   #row index start, finish, end - returns a list of objects
#     print(carpark3)
#     #search = re.search(r'Wareham', carpark3)     #regex nothing to search for in this file
#     empty = ''
#     if carpark3 == empty:
#         print('empty string')
#     else:
#         print('contains value')


# doesn't work - with xlrd?
# with open(book,'r') as file:
#     for current_line in file:
#          # check if the current line
#          # starts with "#"
#          if current_line.startswith(''):
#              print('starts with empty cell')
            
            
        #  else:
        #     print('contains text')
            

# for row in book:
#     car_park_name = row['PURBECK DISTRICT COUNCIL']
#     print(car_park_name)
    # car_park_name_clean = re.sub(r"[- \&]", '', car_park_name)   #apply regex to car park name to remove spaces
    # # print(car_park_name)
    # print(car_park_name_clean)

#access a row

#print(sheet.row_slice(3,0))                  #first index of rows, second is start column


#row method for printing a row by index
# print(sheet.row(0))

#print(sheet.row_values(3,0))                  #row.values is more useful
#print(sheet.col_values(0,2))                   #first index of columns second index of rows
