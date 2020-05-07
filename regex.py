#look at regex for csv files which have spaces, punctuation, multiple values in one cell and so on.

import rdflib
import re

#Daventry - has no headers but assume data is first column - car park, easting, northing, second column - a number of spaces
# example "Newlands 457145,262375",5.0

#remove whitespace
carpark = "Lodge Road "
result = re.sub(r'\s', '', carpark) 
print(carpark + 'changed to ' + result)

#remove quotations
daventry = ' "Newlands 457145,262375" '
no_quotes = re.sub(r'[\"]', '', daventry)
print(daventry + 'changed to ' + no_quotes)


daventry2 = ' "New lands 457145,262375" '
remove = re.sub(r'[\" ]', '', daventry2)
print(daventry2 + 'changed to ' + remove)

#split on , returns the elements as a list
location = '457145,262375'
split = re.split(',', location)
print('access elements by index  ' + split[0])
print(split[1])


#split on comma them remove quotes
daventry = ' "Newlands 457145,262375" '
clean = re.split(',',daventry)
no_quotes = re.sub(r'[\"]', '', daventry)
print(no_quotes)

# remove quotes them split on whitespace and comma
daventry = ' "Newlands 457145,262375" '  
no_quotes = re.sub(r'[\"]', '', daventry)
clean = re.split(r'[, \s]', no_quotes)
carpark_name = clean[1] 
easting = clean[2]
northing = clean[3]
print('best approach is: ' + carpark_name, easting, northing)


#remove &
carpark2 = 'Mary & Magdalene 2'
resultb = re.sub(r'[ \&]', '', carpark2)
print('remove & ' + resultb)

#remove hyphen -
carpark = 'Mary-san-jose'
result = re.sub(r'[-]', '', carpark)
print('remove - ' + result)
