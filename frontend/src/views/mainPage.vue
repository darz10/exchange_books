<template>
    <div class="mainPage">
        <div class="row row-cols-1 row-cols-md-3 g-4">
            <div v-for="book in listBooks" :key="book.id">
                <div class="col">
                    <div class="card border-warning mb-3" style="width: 530px; height: 250px;">
                        <div class="row g-0">
                            <div class="col-md-4">
                                <img src="assets/images/index.jpeg" class="img-fluid rounded-start" alt="#">
                            </div>
                            <div class="col-md-8">
                                <div class="card-body">
                                    <h6>Владелец книги: {{book.user}} </h6><hr>
                                    <h6>Название книги: {{book.name_book}}</h6>
                                    <h6>Автор: {{book.author}}</h6>
                                    <h6>Готовность к обмену: {{book.exchange_status}}</h6>
                                    <hr>
                                    <div class='d-flex'>
                                        <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
                                        <button @onclick="Chat" class="btn btn-outline-warning" style="height: 40px;"><p>Хочу прочитать!</p></button>
                                    </div>                                      
                                    </div>
                            </div>
                        </div>
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
            },
            goTo(id) {
                this.$router.push({ name: 'SingleBook', params: {id: id} })
            },
            Chat(){ 
                this.$router.push({name: 'exchange_chat'})
            },
        components: {},
        }
    }
</script>

<style scoped>
</style>