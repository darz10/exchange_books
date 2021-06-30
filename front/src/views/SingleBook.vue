<template>
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
            this.loadMovie()
        },
        methods: {
            async getBook() {
                this.book = await fetch(`${this.$store.getters.getUrl}/book/${this.id}`).then(response => response.json())
            }
        }
    }
</script>

<style scoped>
</style>