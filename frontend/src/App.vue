<template>
<NaviBar></NaviBar>
  <router-view />
  <div class="container">
  <hr/>
  </div>
</template>

<script>
import NaviBar from './components/NavBar.vue'
export default({
  components: {
    NaviBar,
  }
 
});
</script>


