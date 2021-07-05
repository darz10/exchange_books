<template>
        <div class="navbar navbar-fixed-top">
        <div class="container">
         <h1 class="navbar-brand" style="font-size: 33px;"> <a href="/">ExBook</a></h1>
          <div class="navbar-header">
            <form class="d-flex">
              <!-- <button v-if="!auth" @click="goLogin">Вход</button>
              <button v-else @click="logout">Выход</button> -->
              <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
              <button class="btn btn-outline-success" type="submit">Search</button>
              <a><h4 style="margin: 7px;">Profile</h4></a>
            </form>
          </div>
        </div>
      </div>
</template>

<script>
    export default {
        name: "Nav",
        
        computed: {
            
        },
        methods: {
            auth() {
                if (sessionStorage.getItem("auth_token")) {
                    return true
                }
            },
            goLogin() {
                this.$router.push({name: "login"})
            },
            logout() {
                sessionStorage.removeItem("auth_token")
                window.location = '/'
            },
        }
    }
</script>

<style scoped>
    .navbar{
          margin: 0;
          width: 100%;
          height: 115px;
          background: hsl(59, 97%, 57%);
    }
</style>