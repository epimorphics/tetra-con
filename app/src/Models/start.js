import Geography from '@/Models/geography.js'

export default class Start extends Geography {
    constructor(start) {        
        super(start.eastings, start.northings)
        this.journeyStart = start.journeyStart   
        this.placeName = start.placeName
    }
}