<template>
  <div id="app" class="container">
    <div v-if="postLoading == false"><br/>
    <div class="row row-cols-1 row-cols-md-4 g-4" >
      <div class="col" v-for="post of posts" :key="post.id">
        <div class="card">
          <img :src="post.image" class="card-img-top" alt="post.title">
          <div class="card-body">
            <h5 class="card-title">
              <router-link :to="{ name: 'PostDetails', params: { id: post.id }}">
                {{ post.title }}
                </router-link>
                </h5>
            <p class="card-text">{{ post.excerpt }}</p>
            <a href="#" class="btn btn-primary">readmore</a>
          </div>
        </div>
      </div>
    </div>
    </div>
  <p v-else class="spinner-border text-primary" role="status"></p><br>
  <PaginationBar></PaginationBar>
  </div>
</template>

<script>
// eslint-disable-next-line no-unused-vars
import axios from 'axios';
import PaginationBar from '../components/Pagination.vue'
const baseURL = "http://127.0.0.1:8000/api/"

export default {
  name: 'HomePage',
  components: {
    PaginationBar,
  },
  data(){
    return {
      posts: [],
      postLoading: true,
    
    };
  },
  async created() {
    try {
      const res = await axios.get(baseURL);
      this.posts =res.data;//['results']
      this.postLoading = false;
    }catch (e){
      console.error(e);
    }
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
