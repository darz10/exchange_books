<template>
    <div class="mainPage">
        <h1>Main page render</h1>
        <div v-for="book in listBooks" :key="book.id">
            <h3>{{book.user}}</h3>
            <h3>{{book.user}}</h3>
            <h3>{{book.user}}</h3>
            <h3>{{book.user}}</h3>
        </div>
    </div>
</template>
<script>
    export default {
        name: 'mainPage',
        data() {
            return {
                listBooks: [],
            }
        },
        created() {
            this.gettingBooks(this.page)
        },
        methods: {
             async gettingBooks(){
                this.listBooks = await fetch(`${this.$store.getters.getUrl}books/`).then(response => response.json())
                console.log(this.gettingBooks)
            },
            goTo(id) {
                this.$router.push({ name: 'SingleBook', params: {id: id} })
            },
        components: {},
        }
    }
</script>

<style scoped>
</style>