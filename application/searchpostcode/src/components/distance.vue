<template>
    <div>
        <h2>Let's calculate!</h2>
        <form>
            <label>Enter start postcode</label>
            <input id="inputbox" type="text">
            <button id="button">Enter</button>
        </form>
    </div>
</template>
<script>
export default {
    name: 'distance',
    data() {
        return {
            startPostcode: '', //string
            apiUrl: 'https://api.postcodes.io/postcodes/', //https://api.postcodes.io/postcodes/:postcode
            //apiKey: '', //haven't seen that it takes  a key
            postcodesData: null //or empty array?
        }
    },
    methods: {
        getStartPostcode: function() {
            //could take user input here
        },
        getPostcodes: function() {
            //https://api.postcodes.io/postcodes?q=BS4%202LG checked on browser
            //const url = encodeURI(`${this.apiUrl}?q=${this.startPostcode}`)
            const url = `${this.apiUrl}?q=${this.startPostcode}&limit=5`
            //const url = "https://api.postcodes.io/postcodes?q=BS4%202LG"
            console.log(url)
            fetch(url)
            .then(response => response.json())
            .then(data => {
                console.log(data)
                this.postcodesData = data //bind data to a variable
            })
            .catch(error => console.error(error));
            
        },
        
    },
    //call getPostcodes in created part of life cycle
    created: function() {
        this.getPostcodes()
        },
}
</script>
<style>

</style>