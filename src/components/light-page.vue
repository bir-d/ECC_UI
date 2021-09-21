<template>
    <div class="Page">
        <div id="app">
            <!-- Div used to organise everything onto on plane -->
            <div class="LightsBox">
                <!-- Attempt to dynamically style boz to match window size changes, needs work -->
                <div class="RoomLight" v-bind:style="[{'width': '40%'}, {'height': '40%'}]">
                    <span v-bind:class="[roomStateOn ? 'LightOn' : 'LightOff', light.selected ? 'selected' : '']" v-for="light in lights" :key="light" v-bind:style="[roomStateOn ? {'background-color': (light.colour + light.brightness + ')')} : {'background-color': 'white'}, {'left': light.positionX}, {'top': light.positionY}, {'position': 'absolute'}]" v-bind:title="light.userlabel" v-on:click="toggleSelected(light)"> </span>
                </div>
                <div class="ColourWheel">
                    <colour-picker :width=(windowHeight*0.2) :height=(windowHeight*0.2) v-model="colour"> </colour-picker>
                    <div class="selected-color-info">
                        <p>Selected color:</p>
                        <svg height="24" width="24">
                            <circle cx="12" cy="12" r="11.25" :fill="colour" />
                        </svg>
                    </div>
                    <input v-model="colour" type="text" placeholder="Add new light colour" v-on:keyup.enter="changeLight(colour)">
                    <br>
                    <button class="btn btn-primary" v-on:click="changeLight(colour)">Select Colour</button>
                </div>
                <div>
                    <input v-model="newBrightness" type="text" placeholder="Enter Brightness Level" v-on:keyup.enter="changeBrightness(newBrightness)">
                    <br>
                    <button class="btn btn-primary" v-on:click="SelectAll()">Select All Lights</button>
                    <br>
                    <button class="btn btn-primary" v-on:click="UnselectAll()">Unselect All Lights</button>
                    <br>
                    <input v-model="newPresetName" type="text" placeholder="Enter Preset Name" v-on:keyup.enter="AddPreset(newPresetName)">
                    <br>
                    <input v-model="PresetName" type="text" placeholder="Enter Preset To Use" v-on:keyup.enter="SyncPresets(PresetName)">
                     <ul>
                        <li v-for="preset in presets" :key="preset" v-on:click="SyncPresets(preset.name)"> {{ preset.name }}</li>
                    </ul>
                </div>
            </div>
            <!-- <br> <button class="btn btn-primary" v-on:click="toggleRoomState">Change Room State</button> -->
            <!-- Text field to enter a colour to change selected lights when button pressed later or 'enter' is pressed  -->
            <!-- <input v-model="newColour" type="text" placeholder="Add new light colour" v-on:keyup.enter="changeLight(newColour)"> -->
            <!-- Button to change selected lights to the colour entered previously -->
            <!-- <button class="btn btn-primary" v-bind:disabled="newColour.length === 0" v-on:click="changeLight(newColour)">Save Colour</button> -->
            <!-- Change selected lights to colour currently presented in colour wheel -->
            <!-- <button class="btn btn-primary" v-on:click="changeLight(colour)">Colour Wheel Select</button> -->
        </div>
    </div>
</template>

<style>
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

    
    .selected-color-info {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 15px 0;
    }
    
    .selected-color-info p {
    margin: 0 5px 0 0;
    }
    
    .RoomLight {
        float: left;
        border: 1px solid black;
        left: 2.5%;
        height: 40%;
        width: 40%;
        position: relative;
    }

    .ColourWheel {
        float: left;
        height: 40%;
        width: 20%;
        margin-left: 2.5%;
        /*border: 1px solid black;*/
    }

    #color-wheel {
        margin-left: auto;
        margin-right: auto;
        top: 5%;
    }
    
</style>

<script>
    
    
    
    import ColourPicker from 'vue-color-picker-wheel';

    export default {
        name: 'App',
        components: {
            ColourPicker
        },
        created() {
        },
        data() {
            return {
                //Sets up all variables used within page
                colour: '#000000',
                roomStateOn: true,
                newColour: '',
                newPresetName: '',
                PresetName: '',
                windowHeight: window.innerHeight,
                windowWidth: window.innerWidth,
                //Lights data stored as array
                lights: [
                {
                    //Descriptive label of light for user
                    userlabel: "Light Top Left",
                    //Abbreviated label of light for ease of use
                    label: "LTL",
                    //If Light is on/ off
                    state: "On",
                    //Current colour of light
                    colour: "rgba(255, 0, 0, ",
                    hexColour: "#ff0000",
                    //colour: "rgb(255, 0, 0 ," + this.opacity + ")",
                    //If the light has been selected
                    selected: false,
                    positionX: '5%',
                    positionY: '5%',
                    brightness: 1,
                },
                {
                    userlabel: "Light Top Right",
                    label: "LTR",
                    state: "On",
                    colour: "rgba(0, 0, 255, ",
                    hexColour: "#0000ff",
                    selected: false,
                    positionX: '87.5%',
                    positionY: '5%',
                    brightness: 1,
                },
                {
                    userlabel: "Light Middle",
                    label: "LM",
                    state: "On",
                    colour: "rgba(255, 0, 255, ",
                    hexColour: "#ff00ff",
                    selected: false,
                    positionX: '46.25%',
                    positionY: '42.5%',
                    brightness: 1,
                },
                {
                    userlabel: "Light Bottom Left",
                    label: "LBL",
                    state: "On",
                    colour: "rgba(0, 255, 0, ",
                    hexColour: "#00ff00",
                    selected: false,
                    positionX: '5%',
                    positionY: '80%',
                    brightness: 1,
                },
                {
                    userlabel: "Light Bottom Right",
                    label: "LBR",
                    state: "On",
                    colour: "rgba(0, 255, 255, ",
                    hexColour: "#00ffff",
                    selected: false,
                    positionX: '87.5%',
                    positionY: '80%',
                    brightness: 1,
                },   
                ],
                // Array within array is used to store presets
                presets: [ {
                    name: "Test",
                    presetinfo: [
                    {
                        label: "LTL",
                        state: "On",
                        colour: "rgba(255, 0, 0, ",
                        hexColour: "#ff0000",
                        brightness: 1,
                    },
                    {
                        label: "LTR",
                        state: "On",
                        colour: "rgba(0, 0, 255, ",
                        hexColour: "#0000ff",
                        brightness: 1,
                    },
                    {
                        label: "LM",
                        state: "On",
                        colour: "rgba(255, 0, 255, ",
                        hexColour: "#ff00ff",
                        brightness: 1,
                    },
                    {
                        label: "LBL",
                        state: "On",
                        colour: "rgba(0, 255, 0, ",
                        hexColour: "#00ff00",
                        brightness: 1,
                    },
                    {
                        label: "LBR",
                        state: "On",
                        colour: "rgba(0, 255, 255, ",
                        hexColour: "#00ffff",
                        brightness: 1,
                    },
                ]
                },
                ]
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
            //Update light array to reflect if a specific light has been selected
            toggleSelected: function(Selectedlight) {
                //Inverts the value of 'light.selected' (true -> false, false -> true)
                Selectedlight.selected = !Selectedlight.selected
                this.colour = Selectedlight.hexColour
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
                var newColourRGBA = RGBAHex[0]
                var hexValue = RGBAHex[1]
                for (this.changelight in this.lights) {
                    if (this.lights[this.changelight].selected == true) {
                        this.lights[this.changelight].colour = newColourRGBA;
                        this.lights[this.changelight].hexColour = hexValue;
                        this.lights[this.changelight].selected = false;
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
                var hexR = [hexValue[1], hexValue[2]];
                var hexG = [hexValue[3], hexValue[4]];
                var hexB = [hexValue[5], hexValue[6]];
                var R = this.HexToRGBAFilter(hexR)
                var G = this.HexToRGBAFilter(hexG)
                var B = this.HexToRGBAFilter(hexB)
                return ["rgba(" + R + ", " + G + ", " + B + ", ", hexValue]


            },
            //Hex to RGBA converter part 2
            HexToRGBAFilter: function(hexDouble) {
                var HexLetterCon1 = {
                "a":160, "b":176, "c":192, "d":208, "e":224,  "f":240
                }
                var HexLetterCon2 = {
                "a":10, "b":11, "c":12, "d":13, "e":14,  "f":15
                }
                var hex = 0
                if (typeof HexLetterCon1[hexDouble[0].toLowerCase()] != 'undefined'){
                    if (typeof HexLetterCon2[hexDouble[1].toLowerCase()] != 'undefined') {
                        hex = HexLetterCon1[hexDouble[0].toLowerCase()] + HexLetterCon2[hexDouble[1].toLowerCase()];
                    }
                    else {
                        hex = HexLetterCon1[hexDouble[0].toLowerCase()] + parseInt(hexDouble[1]);
                    } 
                }
                else {
                    if (typeof HexLetterCon2[hexDouble[1].toLowerCase()] != 'undefined') {
                        hex = (parseInt(hexDouble[0]) * 10) + HexLetterCon2[hexDouble[1].toLowerCase()];
                    }
                    else {
                        hex = (parseInt(hexDouble[0]) * 10) + parseInt(hexDouble[1])
                    }
                }
                return hex
            },
            changeBrightness: function(Brightness) {
                for (this.changebrightness in this.lights) {
                    if (this.lights[this.changebrightness].selected == true) {
                        this.lights[this.changebrightness].brightness = Brightness/100;
                    }
                }
            },
            SelectAll: function() {
                for (this.select in this.lights) {
                    if (this.lights[this.select].selected == false) {
                        this.lights[this.select].selected = true;
                    }
                }
            },
            UnselectAll: function() {
                for (this.select in this.lights) {
                    if (this.lights[this.select].selected == true) {
                        this.lights[this.select].selected = false;
                    }
                }
            },
            AddPreset: function(PresetName){
            this.presets.push({
                name: PresetName,
                presetinfo: [ {
                    label: this.lights[0].label,
                    state: this.lights[0].state,
                    colour: this.lights[0].colour,
                    hexColour: this.lights[0].hexColour,
                    brightness: this.lights[0].brightness,
                },
                {
                    label: this.lights[1].label,
                    state: this.lights[1].state,
                    colour: this.lights[1].colour,
                    hexColour: this.lights[1].hexColour,
                    brightness: this.lights[1].brightness,
                },
                {
                    label: this.lights[2].label,
                    state: this.lights[2].state,
                    colour: this.lights[2].colour,
                    hexColour: this.lights[2].hexColour,
                    brightness: this.lights[2].brightness,
                },
                {
                    label: this.lights[3].label,
                    state: this.lights[3].state,
                    colour: this.lights[3].colour,
                    hexColour: this.lights[3].hexColour,
                    brightness: this.lights[3].brightness,
                },
                {
                    label: this.lights[4].label,
                    state: this.lights[4].state,
                    colour: this.lights[4].colour,
                    hexColour: this.lights[4].hexColour,
                    brightness: this.lights[4].brightness,
                },
                ]
            })
            this.newPresetName = ''
            },
            SyncPresets: function(PresetName){
                for (this.element in this.presets) {
                    if (this.presets[this.element].name == PresetName) {
                        for (this.presetconfig in this.presets[this.element].presetinfo) {
                            for (this.lightconfig in this.lights) {
                                if (this.presets[this.element].presetinfo[this.presetconfig].label == this.lights[this.lightconfig].label) {
                                    this.lights[this.lightconfig].state = this.presets[this.element].presetinfo[this.presetconfig].state
                                    this.lights[this.lightconfig].colour = this.presets[this.element].presetinfo[this.presetconfig].colour
                                    this.lights[this.lightconfig].hexColour = this.presets[this.element].presetinfo[this.presetconfig].hexColour
                                    this.lights[this.lightconfig].brightness = this.presets[this.element].presetinfo[this.presetconfig].brightness
                                }
                            }
                        }
                    }
                }
                this.PresetName = '';
            }
        }, 
    };

        
</script>