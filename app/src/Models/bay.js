import Geography from '@/Models/geography.js'
//Class to hold model for Bay object
export default class Bay extends Geography {
    constructor(bay) {                       //constructor takes in a bay object
        super(bay.eastings, bay.northings)           
        this.bayId = bay.bayId;
        this.postcode = bay.postcode;
        this.numSpaces = bay.numSpaces;
        
    }
    
}





