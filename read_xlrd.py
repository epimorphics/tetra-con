import xlrd
import re
import rdflib

from xlrd import open_workbook, cellname, empty_cell
from rdflib import Graph, Literal, Namespace, RDFS, URIRef
from rdflib.namespace import XSD

#create a graph
g = rdflib.Graph()

#create our namespace park as a namespace
park_namespace = Namespace('http://disabled-parking.epimorphics.com/def/terms/')

#bind our prefix with our namespace 
g.bind('park', park_namespace)

#create properties from our namespace to use in the triple
park_has_num_spaces = park_namespace.hasNumSpaces #hasNumSpaces is a property in our park ontology


#read xls excel format #, encoding=''
#book = open_workbook('East Devon.xls')
book = open_workbook('Poole.xls')
sheet = book.sheet_by_index(0)



#get an idea of the size of the sheet
print('file has {} worksheets '.format(book.nsheets))
print('file has {} rows '.format(sheet.nrows))
print('file has {} columns '.format(sheet.ncols))

#access a cell
# print(sheet.cell(1,0).value) #is a string
# if sheet.cell(1,0).value == xlrd.empty_cell.value:
#     print('is empty')
# else:
#     print('contains value')

# print(sheet.cell(3,0))  #row col, car park column name
# print(sheet.cell(3,1))
# print(sheet.cell(3,2))
# print(sheet.cell(3,3))
# #print(sheet.cell(3,4)) #hidden columns?
# #print(sheet.cell(3,5))
# print(sheet.cell(3,6))

#read a specified area of the sheet A4:B10
# for row_index in range(3,9):              #removed sheet.nrows
#     for col_index in range(0,2):
#         #print(sheet.cell(row_index,col_index).value) #prints sheet by cell as string or float
#          cell = str(sheet.cell(row_index,col_index).value)
#          #print('This is one cell {}'.format(cell))
#          print(cell)
           

#access a row  #couldn't work out how to reference just first three rows
                  #first index of rows, second is starting at column index
first_row = sheet.row_slice(3,0)
#print(type(first_row[0])) #type is xlrd.sheet.cell object

# for row_index in range(sheet.nrows):    
#     for col_index in range(sheet.ncols):        
#         print(cellname(row_index,col_index),'----',)        
#         print(sheet.cell(row_index,col_index).value) 

#x = re.search(r'Car Park Name', first_row)

#values we want with row_values
# for col_index in range(0,sheet.ncols):
#     #print(sheet.row(row_index))
#     list_of_values = sheet.col_slice(col_index) #string is a list
    #ar_park = col_index[0]
    # string = ''.join(list_of_values)
    #print(list_of_values)
    
    
    #print(type(row_index)) #row_index is int
    #x = re.search(r'Car Park Name', list_of_values) #can't regex on a list
    #print(type(list_of_values))
    #print(list_of_values[0:5]) #prints the row of values we want as lists


# row_slice returns a list of cel objects
for row_index in range(3,sheet.nrows):
    #print(sheet.row(row_index))
    #list_of_values = sheet.row_slice(row_index) #string is a list
    list_of_values = sheet.row_values(row_index)
    car_park = list_of_values[0]
    clean = re.sub(r'\s', '', car_park) #regex to remove spaces 
    result = re.sub(r'[**]', '', clean)      #regex to remove stars
    num_spaces = list_of_values[1]
    car_park_uri = park_namespace[result] #subject of triple
    #x = re.search(r'Car Park Name', list_of_values) #can't regex on a list
    #print(list_of_values)
    #print(list_of_values[0:5]) #prints the row of values we want as lists
    print(car_park)
    print(num_spaces)
    g.add(
        (car_park_uri, park_has_num_spaces, Literal(num_spaces, datatype=XSD.integer))
    )
    
print(g.serialize(format='turtle').decode('utf-8'))

    


#loop through the list, either for loop, while loop, enumerate

#enumerate
# for row_index in range(3,sheet.nrows):
#     list_of_values = sheet.row_slice(row_index) #string is a list
    
#     #x = re.search(r'Car Park Name', list_of_values) #can't regex on a list
#     #print(list_of_values)
#     #print(list_of_values[0:5]) #prints the row of values we want as lists
#     for i, x in enumerate(list_of_values):
#         print('list has element {} and value {}'.format(i,x))


# for row_index in range(3,sheet.nrows):
#     #print(sheet.row(row_index))
#     list_of_values = sheet.row_values(row_index) # a list
#     for x in list_of_values:
#         print(type(x))     #makes the values string




# while loop
# for row_index in range(3,sheet.nrows):
#     #print(sheet.row(row_index))
#     list_of_values = sheet.row_values(row_index) #string is a list
#     ind = 0   
#     while ind < len(list_of_values):
#         print(list_of_values[ind])
#         ind += 1
        


# empty = sheet.cell(0,2)
# print(empty)
# print(empty.ctype,repr(empty.value))

#row method for printing a row by index
# print(sheet.row(0))

#access a row
#print(sheet.row_slice(3,0))                  #first index of rows, second is columns

#print(sheet.row_values(3,0))                  #row.values is more useful
#print(sheet.col_values(0,2))                   #first index of columns second index of rows


