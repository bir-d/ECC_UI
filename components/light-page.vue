<template>
    <div>
        <!-- Div for colour wheel -->
        
        <div id="app">
            <div>
                <span v-bind:class="[roomStateOn ? 'LightOn' : 'LightOff', light.selected ? 'selected' : '']" v-for="light in lights" :key="light" v-bind:style="[roomStateOn ? {'background-color': light.colour} : {'background-color': 'white'}]" v-bind:title="light.userlabel" v-on:click="toggleSelected(light)"><br> <br> <br> <center> {{light.label}}</center> </span>
                <colour-picker :width=150 :height=150 v-model="colour"> </colour-picker>
                    <div class="selected-color-info">
                        <p>Selected color:</p>
                        <svg height="24" width="24">
                            <circle cx="12" cy="12" r="11.25" :fill="colour" />
                        </svg>
                    </div>
                <p>{{ colour }}</p>
            </div>
            <br> <button class="btn btn-primary" v-on:click="toggleRoomState">Change Room State</button>
            <!-- Text field to enter a colour to change selected lights when button pressed later or 'enter' is pressed  -->
            <input v-model="newColour" type="text" placeholder="Add new light colour" v-on:keyup.enter="changeLight(newColour)">
            <!-- Button to change selected lights to the colour entered previously -->
            <button class="btn btn-primary" v-bind:disabled="newColour.length === 0" v-on:click="changeLight(newColour)">Save Colour</button>
            <!-- Change selected lights to colour currently presented in colour wheel -->
            <button class="btn btn-primary" v-on:click="changeLight(colour)">Colour Wheel Select</button>
            
        </div>
    </div>
</template>

<style>
    /* Brings border to show div for testing */
    #room {
        border: 5px solid black;
    }
    /* Style for lights being on when roomStateOn == true */
    .LightOn {
        height: 44px;
        width: 44px;
        background-color: teal;
        border: 3px solid black;
        border-radius: 50%;
        display: inline-block;
    }
    /* Style for lights being off when roomStateOn == false */
    .LightOff {
        height: 44px;
        width: 44px;
        background-color: white;
        border: 3px solid black;
        border-radius: 50%;
        display: inline-block;
    }
    /* Style for lights being selected */
    .selected {
        height: 44px;
        width: 44px;
        border-radius: 50%;
        border: 3px solid red;
        display: inline-block;
    }
    .center * {
        text-align: center;
    }
    /* Style Colour Wheel */
    #color-wheel {
    margin-left: auto;
    margin-right: auto;
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
</style>

<script>
    //Template for Colour WHeel structure
    
    // Assigns Colour Wheel template to appropriate div and records current colour of the Colour Wheel
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
                colour: '#ffffff',
                roomStateOn: true,
                newColour: '',
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
                    colour: "red",
                    //If the light has been selected
                    selected: false,
                },
                {
                    userlabel: "Light Top Right",
                    label: "LTR",
                    state: "On",
                    colour: "blue",
                    selected: false,
                },
                {
                    userlabel: "Light Middle",
                    label: "LM",
                    state: "On",
                    colour: "purple",
                    selected: false,
                },
                {
                    userlabel: "Light Bottom Left",
                    label: "LBL",
                    state: "On",
                    colour: "green",
                    selected: false,
                },
                {
                    userlabel: "Light Bottom Right",
                    label: "LBR",
                    state: "On",
                    colour: "brown",
                    selected: false,
                },   
                ]
            };
        },
        methods: {
            //Update light array to reflect if a specific light has been selected
            toggleSelected: function(Selectedlight) {
                console.log(Selectedlight.label)
                //Inverts the value of 'light.selected' (true -> false, false -> true)
                Selectedlight.selected = !Selectedlight.selected
            },
            // Same as above, but for room state instead
            toggleRoomState: function() {
                this.roomStateOn = !this.roomStateOn;
            },
            // Loops through light array to see which lights are selected, update the light's colour
            // to the new colour, and then unselect it. (For entering a colour manually, through name or code)
            changeLight: function(newColour) {
                for (this.changelight in this.lights) {
                    if (this.lights[this.changelight].selected == true) {
                        this.lights[this.changelight].colour = newColour;
                        this.lights[this.changelight].selected = false;
                    }
                }
                // Clears input field
                this.newColour = '';
            },
            // Same as above, but for colour wheel selection. I couldn't figure out how to do both in one function,
            // so I did it seperately.
            
        },
    };
    //import Vue from 'vue'

        
</script>