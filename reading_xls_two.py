import xlrd
import re
import rdflib
from rdflib import Graph, Literal, RDFS, URIRef, Namespace

from rdflib.namespace import XSD
from xlrd import open_workbook, cellname, empty_cell

#create a graph
g = rdflib.Graph()

#create our namespace park as a namespace
park_namespace = Namespace('http://disabled-parking.epimorphics.com/def/terms/')

#bind our prefix with our namespace 
g.bind('park', park_namespace)

#create properties from our namespace to use in the triple
park_has_num_spaces = park_namespace.hasNumSpaces #hasNumSpaces is a property in our park ontology


#book = open_workbook('East Devon.xls')
book = open_workbook('Poole.xls')
sheet = book.sheet_by_index(0)

#this method can be used to pick out an several area of the sheet if range in ncols specifies columns
for row in range(2,9):                             #for only rows 2 to 9 - could use nrows for all rows in sheet

    values = []                                    
    
    for col in range(sheet.ncols):                 #for each column, append cell at row col's value to the list
        values.append(str(sheet.cell(row,col).value)) #had some int values now changed to string
        car_park_name = values[0] #first col is car park name
        clean = re.sub(r'\s', '', car_park_name) #removes whitespace
        result = re.sub(r'[**]', '', clean)
        spaces = values[1:2]                       #returns float, apparently all numbers are stored in excel as float
        car_park_uri = park_namespace[result] #create a uri variable with cleaned car park name

        #add to the graph
        g.add(
            (car_park_uri, park_has_num_spaces, Literal(spaces, datatype=XSD.int))
        )

#print(car_park_uri)
print(g.serialize(format='turtle').decode('utf-8'))
