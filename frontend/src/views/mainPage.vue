<template>
    <div class="mainPage">
        <h1>Main page render</h1>
        <div v-for="book in listBooks" :key="book.id">
            <div class="card border-warning mb-3 " style="max-width: 540px;">
                <div class="card-header"><h3>Владелец книги: {{book.user}}</h3></div>
                <div class="row g-0">
                        
                        <h3>Название книги: {{book.name_book}}</h3>
                        <h3>{{book.exchange_status}}</h3>
                        <h3>{{book.rate_book}}</h3>
                    </div>
                </div>
            </div>
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
            this.gettingBooks()
        },
        methods: {
             async gettingBooks(){
                this.listBooks = await fetch(`${this.$store.getters.getUrl}books/`).then(response => response.json())
                console.log(this.listBooks)
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