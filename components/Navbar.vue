<template>
  <div class="hello">
    <b-navbar>
        <template #brand>
            <b-navbar-brand tag="router-link" :to="{ path: '/' }" id="brand">
                <a href="/"><img src="../assets/navbar-thales-logo.png" alt="Thales Logo"></a>
            </b-navbar-brand>
        </template>
        <template #start>
            <b-navbar-item href="/videowall">
                <p id="navbar">Video Wall</p>
            </b-navbar-item>
            <b-navbar-item href="#">
                <p id="navbar">Workstations</p>
            </b-navbar-item>
            <b-navbar-item href="/lights">
                <p id="navbar">Lights</p>
            </b-navbar-item>
<!--          p: set the router-link to display-->
            <b-navbar-item href="/display">
                <p id="navbar">Displays</p>
            </b-navbar-item>
        </template>

        <template #end>
            <b-navbar-item tag="div">
                <div class="buttons">
                    <a class="button">
                        <p id="button-text">+ Preset</p>
                    </a>
                </div>
            </b-navbar-item>
            <b-navbar-item tag="div">
                <div class="buttons">
                    <a class="button">
                        <p id="button-text">Settings</p>
                    </a>
                </div>
            </b-navbar-item>
        </template>
    </b-navbar>
  </div>    
</template>

<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
#navbar{
    font-size: 15px;
    font-family: monospace;
    color: #6b705c;
}
#button-text{
    font-family: monospace;
    color: white;
    
}
.button{
    background-color:#6b705c;
}
#brand{
    height: 60px;
    width: 60px;
    margin-left: 25px;
    margin-right: 25px;
}
</style>
