import xlrd
import re
import rdflib

from xlrd import open_workbook, cellname, empty_cell
from rdflib import Graph, Literal, Namespace, RDFS, URIRef
from rdflib.namespace import XSD

#create a graph
g = rdflib.Graph()
park_namespace = Namespace('http://disabled-parking.epimorphics.com/def/terms/')

#create our namespace park as a namespace

#bind our prefix with our namespace 
g.bind('park', park_namespace)

#create properties from our namespace to use in the triple
park_has_num_spaces = park_namespace.hasNumSpaces #hasNumSpaces is a property in our park ontology


file = 'Poole.xls'

work_book = xlrd.open_workbook(file)
sheet = work_book.sheet_by_index(0)

#get some file information
# print('this sheet contains {} rows'.format(sheet.nrows))
# print('this sheet contains {} columns'.format(sheet.ncols))

#print(sheet.row(0)) #prints row with cell type information
# print(sheet.col(1)) #prints col with cell type information

#get some information about how many empty cells

#print(sheet.row_slice(3)) #a list of cell objects for row 3
# print(sheet.row_slice(3,2))
# print(sheet.row_slice(3,2,4))

# print(sheet.row_values(3)) #a list of cell objects for row 3
# print(sheet.row_values(3,2))
# print(sheet.row_values(3,2,4))

car_parks = []

number_spaces = []
#working with groups of cells A4:B5
# for row_index in range(3, 5):                   #reads row then col
#     for col_index in range(0,2):        
#         print(cellname(row_index,col_index),'-',)        
#         print(sheet.cell(row_index,col_index).value) 



# for col_index in range(0,2):                      #reads column then row
#     for row_index in range(3, 5):    
#         print(cellname(row_index,col_index),'-',)        
#         print(sheet.cell(row_index,col_index).value)

#print(car_parks)
#declare two lists to hold values for car park name and number of spaces




for i in range(sheet.nrows): #ammend here for specific rows, have to start at 0
    car_parks.append(sheet.cell_value(i,0))  #takes what is in column 0

    
for j in range(sheet.ncols):             #ammend here for specific columns
    number_spaces.append(sheet.cell_value(0,j)) #value of the cell starts at col 1 to read column of parking spaces
        
    car_park_var = car_parks[i]
        #regex
    remove_spaces = re.sub(r'\s', '', car_park_var) #regex to remove spaces 
    clean = re.sub(r'[**&()]', '', remove_spaces)      #regex to remove stars
    number_spaces_var = number_spaces[j]
    car_park_uri = park_namespace[clean]
    g.add(
        (car_park_uri, park_has_num_spaces, Literal(number_spaces_var, datatype=XSD.integer) )
    )

#print(g.serialize(format='turtle').decode('utf-8'))

#print(car_parks)
print(number_spaces_var)
#print(car_parks.count(''))
#car_parks.sort()
print(number_spaces)