<template>
  <div id="app" class="container">

<div class="card" style="width: 38rem;">
  <img :src="post.image" class="card-img-top" alt="post.title">
  <div class="card-body">
    <h1 class="card-title">{{ post.title }}</h1>
    <p class="card-text" v-html="post.content"></p>
  </div>
  <div class="card-footer text-muted">
    Comments()
   <div class="mt">
    <div class="row d-flex justify-content-center">
        <div class="col-md-12" >
            <div class="card p-3 mt-2" v-for="comment of comments" :key="comment.id">
                <div class="d-flex justify-content-between align-items-center">
                    <div class="user d-flex flex-row align-items-center"> <img src="https://i.imgur.com/hczKIze.jpg" width="30" class="user-img rounded-circle mr-2"> <span><small class="font-weight-bold text-primary">{{ comment.name }}</small> <small class="font-weight-bold">{{ comment.content }}</small></span> </div>
                </div>
                <div class="action d-flex justify-content-between mt-2 align-items-center">
                    <div class="reply px-4"><span class="dots"></span> <small>Reply</small></div>
                    <div class="icons align-items-center"> <i class="fa fa-star text-warning"></i> <i class="fa fa-check-circle-o check-icon"></i> </div>
                </div>
            </div>
        </div>
    </div><br>
</div>
  </div>
</div>
</div>
     

</template>
<script>
// eslint-disable-next-line no-unused-vars
import axios from 'axios';
const baseURL = "http://127.0.0.1:8000/api/"
//

export default {
  name: 'PostDetails',
  components: {
  },
  data(){
    return {
      post: {},
      comments: [],
      postLoading: true,
    };
  },
  async created() {
    try {
      const res = await axios.get(baseURL + this.$route.params.id);
      this.post =res.data;
      this.comments= res.data["comments"];
      console.log(this.post);
      console.log(this.comments);
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
  text-align: left;
  color: #2c3e50;
  margin-top: 60px;
}
</style>