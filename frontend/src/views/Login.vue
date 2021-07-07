<template>
    <div class="container">
        <h1 class="text-center">Welcome to ExBook!</h1>
        <button v-on:click="show = !show" type="button" class="btn btn-outline-success">Регистрация</button>
        <button v-on:click="show = !show" type="button" class="btn btn-outline-success">Вход</button>
        <transition name="fade" mode="out-in">
            <div v-if="show" id="auth-container" class="row">
              <div class="col-sm-4 offset-sm-4">
                      <div class="form-group">
                          <input v-model="username" type="text" class="form-control" id="username" placeholder="Имя пользователя" required>
                          <input v-model="password" type="password" class="form-control" id="password" placeholder="Пароль" required>
                      </div>
                      <button @click="setLogin" type="submit" class="btn btn-block btn-primary">Sign in</button>
                </div>          
            </div>
        
            <div v-else class="sign up">
                <div class="col-sm-4 offset-sm-4">
                    <div class="form-group">
                        <label>Username</label>
                        <input type="text" class="form-control form-control-lg" v-model="username" id="username" required>
                    </div>

                    <div class="form-group">
                        <label>Email address</label>
                        <input type="email" class="form-control form-control-lg" v-model="email" id="email" required>
                    </div>

                    <div class="form-group">
                        <label>Password</label>
                        <input type="password" class="form-control form-control-lg" v-model="password" id="password" required>
                    </div>

                    <button @click="registerAccount()" type="submit" class="btn btn-dark btn-lg btn-block">Sign Up</button>
                </div>
            </div>
        </transition>
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
                email: '',
                show: true
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
            registerAccount(){
                $.ajax({
                    url: "http://127.0.0.1:8000/auth/users/",
                    type: "POST",
                    data: {
                        username: this.username,
                        password: this.password,
                        email: this.email,

                    },
                    success: (response) => {
                        console.log('account was registrated')
                        alert("Ваш аккаунт был успешно зарегитрирован")
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Логин или пароль не верен")
                        }
                    }
                })
            },
            swapForm(){

            }

        }
    }
</script>

<style scoped>
    .form-control{
        margin-bottom: 5px;
    }
</style>