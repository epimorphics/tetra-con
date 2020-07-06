import csv
import rdflib
import re

from rdflib import Graph, Literal, RDFS, URIRef, Namespace
from rdflib.namespace import XSD                             

#open csv file
input_file = csv.DictReader(open('Daventry.csv',)) #no headers in this file

#create a graph
g = rdflib.Graph()

#create our namespace park as a namespace
park_namespace = Namespace('http://disabled-parking.epimorphics.com/def/terms/')

#bind our prefix with our namespace 
g.bind('park', park_namespace)

#create properties from our namespace to use in the triple
park_has_num_spaces = park_namespace.hasNumSpaces #hasNumSpaces is a property in our park ontology
park_has_locatiaon = park_namespace.hasLocation   #hasLocation is a property in our ontology which maps to xsd integer for easting and northing values in object

#reading through file
for row in input_file:
    carpark = row['St John’s Square 457430,252675']
    remove_whitespace = re.sub(r'\s', '', carpark, 1) #removes first occurence whitespace replaces with empty string still got errors
    no_quotes = re.sub(r'[\"]', '', remove_whitespace)       #regex to remove quation marks replaces with empty string 
    split = re.split(r'[, \s]', no_quotes)         #split on comma and white space
    name = split[0]
    easting = split[1]
    #print(easting)
    carpark_uri = park_namespace[name] #create the namespace from our park namespace adding the cleaned up first column - value is now street
    car_park_spaces = row['10.0'] #again no column header
    #clean_num = re.split(r'\d')  #could use regex to split on .
    
    #add to the graph 
    g.add(
        (carpark_uri, park_has_locatiaon, Literal(easting))
    )
    g.add(
        (carpark_uri, park_has_num_spaces, Literal(car_park_spaces, datatype=XSD.float) ) #couldn't find the docs atm but until I can regex the column it's a float
    )
    
    
print(g.serialize(format='turtle').decode('utf-8'))
