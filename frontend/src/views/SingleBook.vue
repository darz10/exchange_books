<template>
    <div class="singleBook">
        <h1>SIIngel hello</h1>
        <p>{{book.user}}</p>
        <p>{{book.name_book}}</p>
        <p>{{book.author}}</p>
        <p>{{book.genre}}</p>
        <p>{{book.country}}</p>
        <p>{{book.book_describe}}</p>
        <p>{{book.book_state}}</p>
        <p>{{book.exchange_status}}</p>
        <p>{{book.hashtag}}</p>
    </div>
</template>
<script>
    export default {
        name: "SingleBook",
        props: ['id'],
        data() {
            return {
                book: {}
            }
        },
        created() {
            this.getBook()
        },
        methods: {
            async getBook() {
                this.book = await fetch(`${this.$store.getters.getUrl}/api/book/${this.id}`, {headers: {"Authorization": "Token " + sessionStorage.getItem('auth_token')}}).then(response => response.json())
                console.log(this.book)
            }
        }
    }   
</script>

<style scoped>
</style>