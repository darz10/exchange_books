<template>
        <div class="navbar navbar-fixed-top">
        <div class="container">
          <h1 class="navbar-brand" style="font-size: 40px;"><b> ExBook</b></h1>
          <a><h4 style="margin: 7px;">Profile</h4></a>
        </div>
      </div>
</template>

<script>
    export default {
        name: "Nav",
        // data(){
        //   return{
        //     status: false,
        //   }
        // },
        // computed: {
        //     auth() {
        //         if (sessionStorage.getItem("auth_token")) {
        //             return true
        //         }
        //     }
        // },
        // methods: {
        //     goLogin() {
        //         this.$router.push({name: "login"})
        //     },
        //     logout() {
        //         sessionStorage.removeItem("auth_token")
        //         this.$router.push({name: "login"})
        //     },
        // }
    }
</script>

<style scoped>
    @import url('https://fonts.googleapis.com/css2?family=Questrial&display=swap');
    .navbar{
          margin: 0;
          width: 100%;
          height: 115px;
          background: #ffffff;
          background: radial-gradient(circle, rgba(251,251,251,1) 0%, rgba(255,237,4,1) 18%, rgba(255,186,0,1) 100%); 
    }
    h1, h2, h3, h4, h5, h6{
      font-family: 'Questrial', sans-serif;
    }
    a{
      font-family: 'Questrial', sans-serif;
    }
</style>