<template>
    <div>
        <h1>Exchange chat</h1>
        <textarea id="chat-log" cols="85" rows="15" style="margin-bottom: 15px; border-radius: 10px; border-color: rgb(141, 97, 190);"></textarea><br>
        <input id="chat-message-input" type="text" size="90"><br>
        <input id="chat-message-submit" type="button" value="Send" class="btn btn-success">
    </div>
</template>
<script>
    export default{
        name: 'exchange_chat',
        data() {
            return {
                usermane: '',
                message: '',
            }
        },
        created(){
            this.connection = new WebSocket(`ws://${window.location.host}/exchange_chat/`)
            console.log('Chat page was created!!!!')
        },
    //     mounted(){
    //         this.chatSocket.onmessage = e => {
    //           const data = JSON.parse(e.data);
    //           const message = data.message;
    //           this.messages.push(message);
    //         };      
    //         this.chatSocket.onclose = e => {console.error("chat socket closed unexpectedly!");
    //         };      
    //     },
    //     methods: {     
    //         sendMessage() {
    //             this.chatSocket.send(
    //                 JSON.stringify({
    //                     message: this.message
    //                 })        
    //             ),  

    //             this.message = "";
    //         }
    //     }       
    }
</script>

<style scoped>
</style>