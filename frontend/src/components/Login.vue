<template>
    <div class="container">
    <h1 class="text-center">Welcome to ExBook!</h1>
    <div id="auth-container" class="row">
      <div class="col-sm-4 offset-sm-4">
              <div class="form-group">
                  <input v-model="username" type="text" class="form-control" id="username" placeholder="Имя пользователя" required>
                  <input v-model="password" type="password" class="form-control" id="password" placeholder="Пароль" required>
              </div>
              <button @click="setLogin" type="submit" class="btn btn-block btn-primary">Sign in</button>
          </div>          
        </div>
      </div>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "Login",
        data() {
            return {
                username: '',
                password: '',   
            }
        },
        methods: {
            setLogin() {
                $.ajax({
                    url: "http://127.0.0.1:8000/auth/token/login/",
                    type: "POST",
                    data: {
                        username: this.username,
                        password: this.password
                    },
                    success: (response) => {
                        console.log(response.auth_token)
                        alert("Добро пожаловать в ExBook")
                        sessionStorage.setItem("auth_token", response.auth_token)
                        this.$router.push({ name: 'mainPage'})
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Логин или пароль не верен")
                        }
                    }
                })
            },
        }
    }
</script>

<style scoped>
    .form-control{
        margin-bottom: 5px;
    }
</style>