<template>
    <div class="chat">
        <h1>Exchange chat</h1>
        <textarea id="chat-log" cols="100" rows="20" style="margin-bottom: 15px; border-radius: 10px; border-color: rgb(141, 97, 190);"></textarea><br>
        <input id="chat-message-input" type="text" size="90"><br>
        <input id="chat-message-submit" type="button" value="Send">
    </div>
</template>
<script>
    export default {
        name: "exchange_chat",
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