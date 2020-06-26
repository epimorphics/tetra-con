# tetra-con
Repo for the Disabled Parking app intern project 
- Data Engineering folder 
- Application folder

The Data Engineering folder contains a sample of the excel files in the Original Data return, from various Local Authorities, as well as some python files which
were created during the data exploration phase. Some of the scripts make use of the files mentioned and transform the individual csv files into rdf triples.
The various scripts address issues in the data such as multiple values in one cell, empty rows and punctuation.

The Application folder contains a Vue JS application which addresses the first user story, 'as a user I want to search by potscode for disabled parking bays'
- mockdata is in the folder which usees disabled bays from Dover, as well as some dummy data for Bristol.
- The App component contains a search component where the user can enter a destination postcode and home postcode,
- The results component returns an array from the store of bays with postcodes which match. 
- The inidvbay component brings back a selected bay and uses a distance method to calculate the distance in miles from the home postcode to this bay, there is something wrong in this method as the number returned is not correct.

Future steps
- It would be useful to update the application so that start location is entered fully, it could be by adding a method to create eastings and northings for a home postcode, or to allow the user to enter these.
- After the App contains more start and destination objects it would be good to add a previous journeys user story - this would require something such as using the 'Let's Go' button to select a start and end destination.
- Another useful feature would be to add a map into the app so the user can look at the spaces selected.


