new Vue({
    el: '#vue-app',   //property
    data: {
        name: 'Astrid',
        age: 4,
        breakfast: 'chocolate porridge',
        drink: 'milkshake',
        description: ' lockdown treats',
        attends: 'weds',
        website: 'https://www.oasisacademymarksburyroad.org/',
        link: '<a href="https://www.oasisacademymarksburyroad.org/">The school website</a>',
        inStock: true,
        onSale: true,
        items: 5,
        details: ["apple", "orange", "bars", "water", "sandwhiches" ],
        places: [
            {
                placeType: 1,
                placeName: "Claverton"
             },
            {
                placeType: 2,
                placeName: "beach"
            },
            {
                placeType: 1,
                placeName: "river park"
            }
        ]
        

    },
        methods: {
            greet: function() {
                return "Good afternoon"
            },
            add: function(inc) {
                this.items+= inc;
            },
            subtract: function() {
                this.items--;
            }
        }
        
    
    
});