<template>
    <div class="singleBook">
        <h1>SIIngel hello</h1>
        <p>{{book.}}</p>
        <p>{{book.author}}</p>
        <p>{{book.author}}</p>
        <p>{{book.author}}</p>
        <p>{{book.author}}</p>
        <p>{{book.author}}</p>
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
                this.book = await fetch(`${this.$store.getters.getUrl}/api/book/${this.id}`).then(response => response.json())
                console.log(this.book)
            }
        }
    }   
</script>

<style scoped>
</style>