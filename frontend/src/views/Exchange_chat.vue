<template>
    <div>
        <h1>Exchange chat</h1>
       

        <div class="dialog">
            <div v-for="dialog in dialogs" direction="column" justify-content="start" align-items="end" :key="dialog.id">
                {{dialog.message}}
            </div>
        </div>
        <input v-model="form.textarea" multi-line :rows="4" full-width placeholder="Введите текст сообщения"><br>
        <button class="btn btn-success" @click="sendMes">Send</button>

    </div>
</template>
<script>
    export default{
        name: 'exchange_chat',
                data() {
                    return {
                        status: 'disconnect',
                        dialogs: [],
                        form: {
                            textarea: '',
                        },
                        chatSocket: '',
                        logs: [],
                        userName: '',
                    }
        },
        created(){
            this.connect()
        },
        mounted(){
            
        },
        methods: {
            connect() {
                this.socket = new WebSocket('ws:' + '127.0.0.1:8000/ws/exchange_chat/' + this.$route.params.id + '/');
                console.log("web sockettt")
                this.socket.onopen = () => {
                    this.status = "connected";
                    this.dialogs.push({event: "Connected to", message: ' Welcome to Exchange chat'})
                    this.socket.onmessage = ({data}) => {
                        this.dialogs.push(JSON.parse(data));
                        console.log(data);
                        console.log(this.dialogs)
                    };
                };
            },
            disconnect(){
                this.socket.close();
                this.status = "disconnected";
                this.dialogs = [];
                console.log(this.status)
            },
             
            sendMes(e) {
                this.socket.send(JSON.stringify({
                    'message': this.form.textarea, 'username': sessionStorage.getItem("username")
                }));
                // this.dialogs.push({event: "Sent message", message: this.form.textarea});
                this.form.textarea = "";

            },
            
            setName(){
                sessionStorage.setItem("username", this.userName);
            }
            
            
            
        }       
    }
</script>

<style scoped>
</style>