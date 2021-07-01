<template>
    <div class="mainPage">
        <!-- <div class="d-flex justify-content-between"> -->
        <form>
            <input type="text">
            <button type="submit">Click</button>
        </form>
        <div class="row">
            <div v-for="book in listBooks" :key="book.id">
                <div class="col">
                    <div class="card border-warning mb-3" style="width: 530px; height: 250px;">
                        <div class="row g-0">
                            <div class="col-md-4" style="border-radius: 20px;">
                              <img src="#" class="img-fluid rounded-start" alt="#">
                            </div>
                            <div class="col-md-8">
                              <div class="card-body">
                                <h5>Владелец книги: {{book.user}} </h5><hr>
                                <h5>Название книги: {{book.name_book}}</h5>
                                <h5>Готовность к обмену: {{book.exchange_status}}</h5>
                                <h5>Автор: {{book.author}}</h5><hr>
                                <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
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