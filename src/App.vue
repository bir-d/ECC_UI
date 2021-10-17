<template>
  <div id="app">
    <navbar/>
    <router-view></router-view>
  </div>
</template>

<script>
import navbar from "./components/Navbar.vue"


export default {
  name: 'App',
  mounted() {
        //set local storage variable of room state
        localStorage.setItem("state", 'on');
  },
  components:{
    navbar,
  }
  
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
