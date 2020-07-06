import xlrd
import re
import rdflib
from rdflib import Graph, URIRef,Literal, RDFS, Namespace
from rdflib.namespace import XSD

from xlrd import open_workbook, cellname

#read xls excel format #, encoding='cp-1252'

#book = open_workbook('Poole.xls')
book = open_workbook('Purbeck.xlsx')
sheet = book.sheet_by_index(0)

#create a graph
g = rdflib.Graph()

#create our namespace park as a namespace
park_namespace = Namespace('http://disabled-parking.epimorphics.com/def/terms/')

#create  a property number of spaces from our namespace to use in the triple
park_has_num_spaces = park_namespace.hasNumSpaces #hasNumSpaces is a property in our park ontology


#bind our prefix with our namespace 
g.bind('park', park_namespace)


empty = ','
match = 'Wareham'

# for row_index in range(sheet.nrows):
#     #print(sheet.row_values(row_index))
#     carpark = sheet.row_values(row_index)  #row_value works here row_slice doesn't, optional start and end index
#     bay = carpark[0] #column 1
#     #add regex to bay to prevent it breaking the uri
#     spaces = carpark[2]
#     #add regex to spaces
#     #print('location is {} which has {} spaces'.format(bay, spaces))
#     carpark_uri = park_namespace[bay]
#     #print(carpark_uri) #this is not right
#     g.add(
#         (carpark_uri, park_has_num_spaces, Literal(spaces, datatype=XSD.integer))
#     )





#iterate over the worksheet and show the contents as a list  
# for row_index in range(sheet.nrows):                   
#     search = sheet.row_values(row_index)
#     if match in search:
#         #print('found matching')
#         #clean = row_index[match]
#     else:
#             print('not found')
    
# for row_index in range(sheet.nrows):
#     search = sheet.row_values(row_index)
#     match = re.search(r'\bWareham\b', search)  #regex search for word boundaries 
#     if match:
#         carpark_name = search[row_index] 
#         print(carpark_name)
        
   
# for row in range(sheet.nrows):                   #one option is use the start param of range to start where we know the data starts
#     #print(sheet.row(row_index))
#     print(sheet.cell_value(0, row))


#access a row
#print(sheet.row_slice(3,0))                  #first index of rows, second is columns


#row method for printing a row by index
# print(sheet.row(0))

#print(sheet.row_values(3,0))                  #row.values is more useful
#print(sheet.col_values(0,2))                   #first index of columns second index of rows

# cellname could be used to show how many cells a header takes up.




    
        





