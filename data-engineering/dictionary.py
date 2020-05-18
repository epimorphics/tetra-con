import csv
import xlrd
from xlrd import open_workbook
import rdflib
from rdflib import Namespace, URIRef, RDFS, Literal, Graph
from rdflib.namespace import XSD
import re

excel = 'Dover.xls'
work_book = xlrd.open_workbook(excel)
sheet = work_book.sheet_by_index(0)

print('sheet has {} rows and {} cols'.format(sheet.nrows, sheet.ncols))
col_headers = sheet.row_values(5) #headers this one doesn't need to change, has to be this row


#row_of_data = sheet.row_values(9) #first row of data need to iterate to get this to change

    

header = col_headers
#print(len(col_headers))
#print(type(col_headers))


# print(row_of_data)
# print(col_headers)

#removing the space from first element
#location = values[0]
#remove = re.sub('\s', '', location)
#values[0] = remove
#print(remove)

#add extra element to the headers list - values
header[3] = 'easting'
header.insert(4, 'northing')
#print(header)
#print(values[3])
#print(values[4])
#values.insert(4, values[3]) #essentially copying the element
#print(values)

#regex on the values in the list
#mult_values = values[3]
#split = re.split('-',mult_values)
#values[3] = split[0]
#values[4] = split[1]
#print(values)


#use zip function to create a dictionary
#pairs = dict(zip(header,values))
#print(pairs)

####can read in several rows but can't loop over creation of lists and dictionaries
#print rows in a range of rows 9-12
# for row_index in range(9,12): 
#      data.append(sheet.row_values(row_index))
#      print(len(data))

# list_zero = data[0]
# list_one = data[1]
# list_two = data[2]
# print(list_zero)

# #create a list of headers
# col_headers = sheet.row_values(5) #headers this one doesn't need to change, has to be this row




for ind in range(sheet.nrows):
    if ind < 9:
        continue
    elif ind >= 9 and ind < 14:
        mylist = sheet.row_values(ind)
        
        #print('header 5',header[0])
        #print('data 5',mylist[5])
        space = mylist[0]
        remove = re.sub('\s', '', space)
        mylist[0] = remove
        mult_values = mylist[3]
        split = re.split('-',mult_values)
        mylist[3] = split[0]
        mylist[4] = split[1]
        pairs = dict(zip(header,mylist))
        #print(pairs)
        g = Graph()
        park_namespace = Namespace('http://disabled-parking.epimorphics.com/def/terms/')
        g.bind('park', park_namespace)  #creat prefix and bind it to our namespace

        park_has_num_spaces = park_namespace.HasNumSpaces #creating a property has number of spaces


        car_park_uri = park_namespace[pairs['Location']]   #subject of rdf triple
        #print(car_park_uri)
        #num_spaces = pairs['Number of spaces']
        num_spaces = mylist[5] #the inserted list element for the northing has pushed the column for number of spaces out of sync
        #print(num_spaces)

        g.add(
            (car_park_uri, park_has_num_spaces, Literal(num_spaces, datatype=XSD.integer))
        )

        print(g.serialize(format='turtle').decode('utf-8'))
    else:
        continue