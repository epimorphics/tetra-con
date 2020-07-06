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

# row_slice returns a list of cell objects
for row_index in range(3,sheet.nrows):
    list_of_values = sheet.row_values(row_index)
    car_park = list_of_values[0]
    clean = re.sub(r'\s', '', car_park) #regex to remove spaces 
    result = re.sub(r'[**]', '', clean)      #regex to remove stars
    num_spaces = list_of_values[1]
    car_park_uri = park_namespace[result] #subject of triple
    print(car_park)
    print(num_spaces)
    g.add(
        (car_park_uri, park_has_num_spaces, Literal(num_spaces, datatype=XSD.integer))
    )
    
print(g.serialize(format='turtle').decode('utf-8'))



