<template>
    <!-- Waits until lights are loaded to render -->
    <div class="Page" v-if="lights[0].colour != 'undef'">
        <div id="app">
            <!-- Div used to organise everything onto on plane -->
            <div class="LightsBox">
                <!-- Attempt to dynamically style boz to match window size changes, needs work -->
                <div 
                    class="RoomLight" 
                    v-bind:style="[{'width': '40%'}, {'height': '40%'}]"
                >
                    <!-- For loops through lights and displays them within mock room box -->
                    <span 
                        v-bind:class="[roomStateOn ? 'LightOn' : 'LightOff', light.selected ? 'selected' : '']" 
                        v-for="light in lights" 
                        :key="light" 
                        v-bind:style="[roomStateOn ? {'background-color': (light.colour + light.brightness + ')')} : {'background-color': 'white'}, {'left': light.positionX}, {'top': light.positionY}, {'position': 'absolute'}]" 
                        v-bind:title="light.userlabel" 
                        v-on:click="toggleSelected(light)"
                    > </span>
                </div>
                <!-- Div that contains colour wheel and respective content -->
                <div class="ColourWheel">
                    <!-- Attempt to dynamically style colour wheel to match window size changes, needs work -->
                    <colour-picker 
                        :width=(windowHeight*0.2) 
                        :height=(windowHeight*0.2) 
                        v-model="colour"
                    > </colour-picker>
                    <!-- Display currently selected colour -->
                    <div class="selected-color-info">
                        <p>Selected color:</p>
                        <svg height="24" width="24">
                            <circle cx="12" cy="12" r="11.25" :fill="colour" />
                        </svg>
                    </div>
                    <input 
                        class="input is-rounded is-medium" 
                        v-model="colour" 
                        type="text" 
                        placeholder="Add new light colour" 
                        v-on:keyup.enter="changeLight(colour)"
                    >
                    <br>
                    <button 
                        class="button is-medium is-fullwidth is-rounded" 
                        v-on:click="changeLight(colour)"
                    >Select Colour</button>
                </div>
                <div class="columns">
                    <div 
                        class="column" 
                        id="Functions"
                    >
                    <!-- Select all Lights -->
                    <button 
                        class="button is-medium is-fullwidth is-rounded is-success" 
                        v-on:click="SelectAll()"
                    >
                    Select All Lights</button>
                    <br>
                    <!-- Unselect all Lights -->
                    <button 
                        class="button is-medium is-fullwidth is-rounded is-danger" 
                        v-on:click="UnselectAll()"
                    >
                    Unselect All Lights</button>
                    <br>
                    <!-- Mock preset creation for testing purposes -->
                    <!-- 0-100 scale input for brightness, to be changed into a sliding bar -->
                    <input 
                        class="input is-rounded is-medium" 
                        v-model="newBrightness" 
                        type="text" 
                        placeholder="Enter Brightness Level: 0 - 100" 
                        v-on:keyup.enter="changeBrightness(newBrightness)"
                    >
                    <br>
                    
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style>

    .Page{
        margin-top: 6em;
    }
    /* Keep sizes consistant */
    html, body, #app, .Page, .LightsBox {
        height: 100%;
        width: 100%;
    }
    html {
        background-color: #ece7e7;
    }
    /* Style for lights being on when roomStateOn == true */
    .LightOn {
        height: 15%;
        width: 7.5%;
        background-color: teal;
        border: 3px solid black;
        border-radius: 50%;
        display: inline-block;
    }
    /* Style for lights being off when roomStateOn == false */
    .LightOff {
        height: 15%;
        width: 7.5%;
        background-color: white;
        border: 3px solid black;
        border-radius: 50%;
        display: inline-block;
    }
    /* Style for lights being selected */
    .selected {
        height: 15%;
        width: 7.5%;
        border-radius: 50%;
        border: 3px solid red;
        display: inline-block;
    }
    .center * {
        text-align: center;
    }

    /* Scale and display mock room */
    .RoomLight {
        float: left;
        border: 1px solid black;
        left: 2.5%;
        height: 40%;
        width: 40%;
        position: relative;
    }

    /* Colour Wheel library css */
    .selected-color-info {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 15px 0;
    }
    
    .selected-color-info p {
    margin: 0 5px 0 0;
    }

    .ColourWheel {
        float: left;
        height: 40%;
        width: 20%;
        margin-left: 5em;
        /*border: 1px solid black;*/
    }

    #color-wheel {
        margin-left: auto;
        margin-right: auto;
        top: 5%;
    }
    
    #Functions{
        margin-left: 6em;
        margin-right: 6em;
    }
    input{
        margin-bottom: 1em;
    }
</style>

<script>
    
    
    // Imports libraries
    import axios from 'axios'
    import ColourPicker from 'vue-color-picker-wheel';

    export default {
        name: 'App',
        // Imports ColourWheel library
        components: {
            ColourPicker
        },
        // Runs as instance is generated
        created() {
            // Creates lights array earlier than would normally be rendered
            this.pushLights();
            // Extracts light information stored in db
            this.getLights();
        },
        data() {
            return {
                // Sets up all variables used within page
                colour: '#000000',
                roomStateOn: true,
                newColour: '',
                newBrightness: '',
                newPresetName: '',
                PresetName: '',
                windowHeight: window.innerHeight,
                windowWidth: window.innerWidth,
                // Lights info from db stored as array
                dblights: [],
                // Lights data stored as array
                lights: [],
                
            };
        },
        // Part of dynamic function to style with changing window size, needs work
        mounted() {
            this.$nextTick(() => {
                window.addEventListener('resize', this.onResize);
            })
        },
        // Part of dynamic function to style with changing window size, needs work
        beforeDestroy() { 
            window.removeEventListener('resize', this.onResize); 
        },
        methods: {
            // Lights array information is generated earlier than deafualt rendering in data.
            // This is done beacuse otherwise the generation of lights overwrites the db values
            pushLights() {
                // Each light is pushed onto lights array
                this.lights.push({
                    // Descriptive label of light for user
                    userlabel: "Light Top Left",
                    // Abbreviated label of light for ease of use
                    label: "LTL",
                    // If Light is on/ off
                    state: true,
                    // Current colour of light
                    colour: "undef",
                    hexColour: "#ff0000",
                    // If the light has been selected
                    selected: false,
                    // Default position of light in horizontal of room
                    positionX: '5%',
                    // Default position of light in vertical of room
                    positionY: '5%',
                    // How bright light is on scale 0-1
                    brightness: 1,
                })
                this.lights.push({
                    userlabel: "Light Top Right",
                    label: "LTR",
                    state: true,
                    colour: "undef",
                    hexColour: "#0000ff",
                    selected: false,
                    positionX: '87.5%',
                    positionY: '5%',
                    brightness: 1,
                })
                this.lights.push({
                    userlabel: "Light Middle",
                    label: "LM",
                    state: true,
                    colour: "undef",
                    hexColour: "#ff00ff",
                    selected: false,
                    positionX: '46.25%',
                    positionY: '42.5%',
                    brightness: 1,
                })
                this.lights.push({
                    userlabel: "Light Bottom Left",
                    label: "LBL",
                    state: true,
                    colour: "undef",
                    hexColour: "#00ff00",
                    selected: false,
                    positionX: '5%',
                    positionY: '80%',
                    brightness: 1,
                })
                this.lights.push({
                    userlabel: "Light Bottom Right",
                    label: "LBR",
                    state: true,
                    colour: "undef",
                    hexColour: "#00ffff",
                    selected: false,
                    positionX: '87.5%',
                    positionY: '80%',
                    brightness: 1,
                })
            },
            // Lights infomration stored in db is extracted
            getLights() {
                axios({
                    method:'get',
                    // Url of backend location of data
                    url: 'http://127.0.0.1:8000/api/lights/',
                    auth: {
                        username: 'admin',
                        password: 'eccadmin123'
                    }
                // This section tells code to wait until lights have been rendered to extract db lights info
                }).then((response) => {

                    this.isLoaded = true;

                    // Check the response was a success
                    if(response.data != 'undefined')
                    {
                        this.dblights = response.data;
                        // Calls function to update lights values with db values
                        this.updateLights();
                    }
                });
            },
            // Update lights values with db values
            updateLights() {
                for (this.vuelight in this.lights) {
                    for (this.djangolight in this.dblights) {
                        // Matches db values and instance values on mock PK label
                        if(this.lights[this.vuelight].label == this.dblights[this.djangolight].name) {
                            this.lights[this.vuelight].colour = this.HexToRGBA(this.dblights[this.djangolight].colour);
                            this.lights[this.vuelight].hexColour = this.dblights[this.djangolight].colour;
                            // Brightness stored as whole number in db, so it is converted from float to percent
                            this.lights[this.vuelight].brightness = this.dblights[this.djangolight].brightness/100;
                            this.lights[this.vuelight].state = this.dblights[this.djangolight].light_on;
                            this.lights[this.vuelight].selected = this.dblights[this.djangolight].selected;
                        }
                        
                    }
                }
            },
            //Update light array to reflect if a specific light has been selected
            toggleSelected: function(Selectedlight) {
                //Inverts the value of 'light.selected' (true -> false, false -> true)
                Selectedlight.selected = !Selectedlight.selected
                this.colour = Selectedlight.hexColour
                // Dictionary defines a light's id from its label
                var PutLabelIds = {
                "LTL":1, "LTR":2, "LM":3, "LBL":4, "LBR":5
                }
                // Load non-changed data on light
                var name = Selectedlight.label;
                var colour = Selectedlight.hexColour;
                var brightness = Selectedlight.brightness * 100;
                var light_on = Selectedlight.state;
                // Get light id from label
                if (typeof PutLabelIds[Selectedlight.label] != 'undefined')
                    var lightId = PutLabelIds[Selectedlight.label];
                    // Updates light with new value/s
                    axios({
                        method:'put',
                        url: 'http://127.0.0.1:8000/api/lights/' + lightId,
                        headers: {
                        'Content-Type': 'application/json'
                        },
                        data: {
                        id: lightId,
                        name: name,
                        colour: colour,
                        brightness: brightness, 
                        light_on: light_on,
                        selected: Selectedlight.selected,
                        },
                        // Login to allow db updates/ edits
                        auth: {
                        username: 'admin',
                        password: 'eccadmin123'
                        }
                    })
            },
            // Same as above, but for room state instead
            toggleRoomState: function() {
                this.roomStateOn = !this.roomStateOn;
            },
            // First a colour is converted from name and/ or hexcode into rgba format without the a, which is controleld by the brightness
            // Loops through light array to see which lights are selected, update the light's colour
            // to the new colour, and then unselect it.
            changeLight: function(newColour) {
                var coloursName = {
                "aliceblue":"#f0f8ff", "antiquewhite":"#faebd7", "aqua":"#00ffff", "aquamarine":"#7fffd4", "azure":"#f0ffff",  "beige":"#f5f5dc", "bisque":"#ffe4c4", "black":"#000000", "blanchedalmond":"#ffebcd", "blue":"#0000ff", "blueviolet":"#8a2be2", "brown":"#a52a2a", "burlywood":"#deb887",  "cadetblue":"#5f9ea0", "chartreuse":"#7fff00", "chocolate":"#d2691e", "coral":"#ff7f50", "cornflowerblue":"#6495ed", "cornsilk":"#fff8dc", "crimson":"#dc143c", "cyan":"#00ffff",  "darkblue":"#00008b", "darkcyan":"#008b8b", "darkgoldenrod":"#b8860b", "darkgray":"#a9a9a9", "darkgreen":"#006400", "darkkhaki":"#bdb76b", "darkmagenta":"#8b008b", "darkolivegreen":"#556b2f",  "darkorange":"#ff8c00", "darkorchid":"#9932cc", "darkred":"#8b0000", "darksalmon":"#e9967a", "darkseagreen":"#8fbc8f", "darkslateblue":"#483d8b", "darkslategray":"#2f4f4f", "darkturquoise":"#00ced1",  "darkviolet":"#9400d3", "deeppink":"#ff1493", "deepskyblue":"#00bfff", "dimgray":"#696969", "dodgerblue":"#1e90ff",  "firebrick":"#b22222", "floralwhite":"#fffaf0", "forestgreen":"#228b22", "fuchsia":"#ff00ff",  "gainsboro":"#dcdcdc", "ghostwhite":"#f8f8ff", "gold":"#ffd700", "goldenrod":"#daa520", "gray":"#808080", "green":"#008000", "greenyellow":"#adff2f",
                "honeydew":"#f0fff0", "hotpink":"#ff69b4", "indianred ":"#cd5c5c", "indigo":"#4b0082", "ivory":"#fffff0", "khaki":"#f0e68c",  "lavender":"#e6e6fa", "lavenderblush":"#fff0f5", "lawngreen":"#7cfc00", "lemonchiffon":"#fffacd", "lightblue":"#add8e6", "lightcoral":"#f08080", "lightcyan":"#e0ffff", "lightgoldenrodyellow":"#fafad2",  "lightgrey":"#d3d3d3", "lightgreen":"#90ee90", "lightpink":"#ffb6c1", "lightsalmon":"#ffa07a", "lightseagreen":"#20b2aa", "lightskyblue":"#87cefa", "lightslategray":"#778899", "lightsteelblue":"#b0c4de",  "lightyellow":"#ffffe0", "lime":"#00ff00", "limegreen":"#32cd32", "linen":"#faf0e6",  "magenta":"#ff00ff", "maroon":"#800000", "mediumaquamarine":"#66cdaa", "mediumblue":"#0000cd", "mediumorchid":"#ba55d3", "mediumpurple":"#9370d8", "mediumseagreen":"#3cb371", "mediumslateblue":"#7b68ee",        "mediumspringgreen":"#00fa9a", "mediumturquoise":"#48d1cc", "mediumvioletred":"#c71585", "midnightblue":"#191970", "mintcream":"#f5fffa", "mistyrose":"#ffe4e1", "moccasin":"#ffe4b5", "navajowhite":"#ffdead", "navy":"#000080",  "oldlace":"#fdf5e6", "olive":"#808000", "olivedrab":"#6b8e23", "orange":"#ffa500", "orangered":"#ff4500", "orchid":"#da70d6",  "palegoldenrod":"#eee8aa",
                "palegreen":"#98fb98", "paleturquoise":"#afeeee", "palevioletred":"#d87093", "papayawhip":"#ffefd5", "peachpuff":"#ffdab9", "peru":"#cd853f", "pink":"#ffc0cb", "plum":"#dda0dd", "powderblue":"#b0e0e6", "purple":"#800080",  "rebeccapurple":"#663399", "red":"#ff0000", "rosybrown":"#bc8f8f", "royalblue":"#4169e1",  "saddlebrown":"#8b4513", "salmon":"#fa8072", "sandybrown":"#f4a460", "seagreen":"#2e8b57", "seashell":"#fff5ee", "sienna":"#a0522d", "silver":"#c0c0c0", "skyblue":"#87ceeb", "slateblue":"#6a5acd", "slategray":"#708090", "snow":"#fffafa", "springgreen":"#00ff7f", "steelblue":"#4682b4",   "tan":"#d2b48c", "teal":"#008080", "thistle":"#d8bfd8", "tomato":"#ff6347", "turquoise":"#40e0d0", "violet":"#ee82ee",   "wheat":"#f5deb3", "white":"#ffffff", "whitesmoke":"#f5f5f5", "yellow":"#ffff00", "yellowgreen":"#9acd32"
                }
                // CHecks for colour name in above dict and changes it to hex
                if (typeof coloursName[newColour.toLowerCase()] != 'undefined')
                    newColour = coloursName[newColour.toLowerCase()];
                // hexcode is changed to rgba
                var RGBAHex = this.HexToRGBA(newColour)
                // Loops through lights and updates selected lights colour and hex value to new input colour
                // Unselects light when updated
                for (this.changelight in this.lights) {
                    if (this.lights[this.changelight].selected == true) {
                        this.lights[this.changelight].colour = RGBAHex;
                        this.lights[this.changelight].hexColour = newColour;
                        this.lights[this.changelight].selected = false;
                        var PutLabelIds = {
                        "LTL":1, "LTR":2, "LM":3, "LBL":4, "LBR":5
                        }
                        var name = this.lights[this.changelight].label;
                        var selected = this.lights[this.changelight].selected;
                        var brightness = this.lights[this.changelight].brightness  * 100;
                        var light_on = this.lights[this.changelight].state;
                        if (typeof PutLabelIds[this.lights[this.changelight].label] != 'undefined')
                            var lightId = PutLabelIds[this.lights[this.changelight].label];
                            axios({
                                method:'put',
                                url: 'http://127.0.0.1:8000/api/lights/' + lightId,
                                headers: {
                                'Content-Type': 'application/json'
                                },
                                data: {
                                id: lightId,
                                name: name,
                                colour: newColour,
                                brightness: brightness, 
                                light_on: light_on,
                                selected: selected,
                                },
                                auth: {
                                username: 'admin',
                                password: 'eccadmin123'
                                }
                            })
                    }
                }
                
                // Clears input field
                this.newColour = '';
            },
            // Part of dynamic function to style with changing window size, needs work
            onResize() {
                this.windowHeight = window.innerHeight;
                this.windowWidth = window.innerWidth;
            },
            //Hex to RGBA converter part 1
            HexToRGBA: function(hexValue) {
                // Splits hex code into R, G and B hex value sections
                // e.g. #ff55a9 is split into R = ff, G = 55, B = a9
                var hexR = [hexValue[1], hexValue[2]];
                var hexG = [hexValue[3], hexValue[4]];
                var hexB = [hexValue[5], hexValue[6]];
                // parses hex code into value converter
                var R = this.HexToRGBAFilter(hexR)
                var G = this.HexToRGBAFilter(hexG)
                var B = this.HexToRGBAFilter(hexB)
                // returns converted hex in rbga format minus the brightness value, which 
                // is dynamically added in rendering code (line 9 as time of writing)
                return ("rgba(" + R + ", " + G + ", " + B + ", ")


            },
            //Hex to RGBA converter part 2
            HexToRGBAFilter: function(hexDouble) {
                // define libraries that convert first and second position letters into respective
                // numeric value
                var HexLetterCon1 = {
                "a":160, "b":176, "c":192, "d":208, "e":224,  "f":240
                }
                var HexLetterCon2 = {
                "a":10, "b":11, "c":12, "d":13, "e":14,  "f":15
                }
                var hex = 0
                // Checks if hex value has letter in first position
                if (typeof HexLetterCon1[hexDouble[0].toLowerCase()] != 'undefined'){
                    // Checks if hex value has letter in second position
                    if (typeof HexLetterCon2[hexDouble[1].toLowerCase()] != 'undefined') {
                        // Converts hex based on respective letter dictionary values from above for both positions
                        hex = HexLetterCon1[hexDouble[0].toLowerCase()] + HexLetterCon2[hexDouble[1].toLowerCase()];
                    }
                    // If hex value isn't a letter in second position
                    else {
                        // Converts hex based on respective letter dictionary values from above for first positions and adds second position number
                        hex = HexLetterCon1[hexDouble[0].toLowerCase()] + parseInt(hexDouble[1]);
                    } 
                }
                // If hex value isn't a letter in first position
                else {
                    // Checks if hex value has letter in second position
                    if (typeof HexLetterCon2[hexDouble[1].toLowerCase()] != 'undefined') {
                        // Converts hex based on respective letter dictionary values from above for second positions and adds that to first position with the position 1 numeric multiplied by 10
                        hex = (parseInt(hexDouble[0]) * 10) + HexLetterCon2[hexDouble[1].toLowerCase()];
                    }
                    // If hex value isn't a letter in second position
                    else {
                        // Adds the two numeric values of hex together with the position 1 numeric multiplied by 10
                        hex = (parseInt(hexDouble[0]) * 10) + parseInt(hexDouble[1])
                    }
                }
                return hex
            },
            // Change light Brightness 
            changeBrightness: function(Brightness) {
                // Changes brightness for lights selected
                for (this.changebrightness in this.lights) {
                    if (this.lights[this.changebrightness].selected == true) {
                        // update selected lights brighness value and convert brightness from 0-100 scale to 0-1 scale
                        this.lights[this.changebrightness].brightness = Brightness/100;
                        // Note light is not unselected, as when a bar is added it will need to be a sliding change
                        // which will not work if a light is unselected as soon as the bar is moved
                        var PutLabelIds = {
                        "LTL":1, "LTR":2, "LM":3, "LBL":4, "LBR":5
                        }
                        var name = this.lights[this.changebrightness].label;
                        var selected = this.lights[this.changebrightness].selected;
                        var colour = this.lights[this.changebrightness].hexColour;
                        var light_on = this.lights[this.changebrightness].state;
                        
                        if (typeof PutLabelIds[this.lights[this.changebrightness].label] != 'undefined')
                            var lightId = PutLabelIds[this.lights[this.changebrightness].label];
                            axios({
                                method:'put',
                                url: 'http://127.0.0.1:8000/api/lights/' + lightId,
                                headers: {
                                'Content-Type': 'application/json'
                                },
                                data: {
                                id: lightId,
                                name: name,
                                colour: colour,
                                brightness: Brightness, 
                                light_on: light_on,
                                selected: selected,
                                },
                                auth: {
                                username: 'admin',
                                password: 'eccadmin123'
                                }
                            })
                    }
                }
            },
            // Select all lights that aren't currently selected
            SelectAll: function() {
                for (this.select in this.lights) {
                    if (this.lights[this.select].selected == false) {
                        this.toggleSelected(this.lights[this.select])
                    }
                }
            },
            // Unselect all lights that are currently selected
            UnselectAll: function() {
                for (this.select in this.lights) {
                    if (this.lights[this.select].selected == true) {
                        this.toggleSelected(this.lights[this.select])
                    }
                }
            },
            
        }, 
    };

        
</script>



