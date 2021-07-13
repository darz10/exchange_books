<template>
    <div class="container">
        <h1>Profile</h1>
        <div>
            <p>{{userData.username}}</p>
        </div>
    </div>
</template>
<script>
    export default {
        name: "Profile",
        data() {
            return {
                userData: []
            }
        },
        created() {
            this.loaduserData()
        },
        methods: {
            async loaduserData() {
                this.userData = await fetch(`${this.$store.getters.getUrl}/profile/`, {headers: {"Authorization": "Token " + sessionStorage.getItem('auth_token')}}).then(response => response.json())
                console.log(this.userData)
            }
        }
    }   
</script>

<style scoped>
</style>