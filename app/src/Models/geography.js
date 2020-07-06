//parent class which all subclasses inherit from
export default class Geography {
    constructor(eastings, northings) {
        this.eastings = eastings
        this.northings = northings
                        
    }
    // expect two objects each with eastings and northings properties
    static distance(obj1, obj2) {
        const xValues = Math.pow(obj1.eastings - obj2.eastings, 2)
        const yValues = Math.pow(obj1.northings - obj2.northings, 2)
        const total = xValues + yValues
        const result = Math.sqrt(total)
        const miles = result * 0.00062137
        return Math.round(miles)
    }
}