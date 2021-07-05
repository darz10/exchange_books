<template>
    <div class="singleBook">
        <h1>Profile</h1>
        <div>
            <p>{{userData.username}}</p>
        </div>
    </div>
</template>
<script>
    export default {
        name: "Profile",
        props: ['id'],
        data() {
            return {
                userData: {}
            }
        },
        created() {
            this.loaduserData()
        },
        methods: {
            async loaduserData() {
                this.userData = await fetch(`${this.$store.getters.getUrl}/profile/user/${this.id}`).then(response => response.json())
            }
        }
    }   
</script>

<style scoped>
</style>