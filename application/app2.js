Vue.component('product', {
    template: `
    <div class="product">

    <div class="product-image">
        <img :src="image">
    </div>

    <div class="product-info">
                <h1>{{title}}</h1>
                <p v-if="inStock">In stock</p>
                <p v-else>Out of stock</p>

            
                <ul>
                    <li v-for="f in food" >{{f}}</li>
                </ul>
    
                
            
            
                <div class="color-box" 
                    v-for="(variant, index) in variants" 
                    :key="variant.variantId"
                    :style="{ backgroundColor: variant.variantColour }" 
                    @mouseover="updateProduct(index)"
                    >
                </div>

                <button v-on:click="addToTrolley" 
                :disabled="inStock"
                :class="{ disabledButton: !inStock }"
                >
                Add to trolley
                </button>

            <div class="=trolley">
                <p>Trolley {{trolley}}</p>
            </div>
        </div>
    </div>
    `
})
new Vue({
    el: '#app', // attach this js file to the html
    data: {
        brand: "LockDown!",
        topProduct: 'sun lotion',
        data_image: 'images/store.svg',
        inStock: true,
        food: ["ice-cream", "chocolate", "marshmallows"],
        variants: [
            {
                variantId: 1,
                name: "red leggings",
                variantColour: 'red',
                image: '/images/red_leggings.jfif',
                variantWaist: 'high',
                variantMaterial: 'bamboo'
            },
            {
                variantId: 2,
                name: "blue leggings",
                variantColour: 'blue',
                image: '/images/blue_leggings.jfif',
                variantWaist: 'low',
                variantMaterial: 'polyester'
            },
            {
                variantId: 3,
                name: "hot pink leggings",
                variantColour: 'hot pink',
                variantWaist: 'mid',
                variantMaterial: 'mixed'
            }
        ],
        trolley: 0,
        },
        methods: {
            addToTrolley: function() {
                this.trolley +=1
            },
            updateProduct: function(image) {
                this.image = image
            },
            RemoveFromTrolley: function() {
                this.trolley -=1
            },
        },
        computed: {
            title() {
                return this.brand + ' ' + this.topProduct
            }
        }

})