<template>
  <div id="app">
    <subs/>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import subs from './components/subs.vue'

export default {
  name: 'App',
  components: {
    subs
    // HelloWorld

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
  margin-top: 5.8125rem;
  display: flex;
  justify-content: center;
}
</style>
