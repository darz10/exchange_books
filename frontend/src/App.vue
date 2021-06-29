<template>

  <div id="app">
    <div class="books">
      <div v-for="book in listBooks" :key="book.id">
          <h4>Владелец книги: {{ book.user }} </h4>
          <h4>Название книги: {{ book.name_book }} </h4>
          <h4>Автор: {{ book.author }} </h4>
          <h4>Жанр: {{ book.genre }} </h4>
          <h4>Страна: {{ book.country }} </h4>
          <h4>Описание: {{ book.book_describe }} </h4>
          <h4> {{ book.book_state }} </h4>
          <h4> {{ book.exchange_status }} </h4>
          <h4> {{ book.comment_book }} </h4>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'App',
  data() {
    return {
      listBooks: [],
      listB: [],
    }
  },
  async created(){
    this.gettingBooks()
    console.log(this.listBooks)
    console.log(this.listB)
  },
  methods: {
    async gettingBooks(){
      this.listBooks = await fetch('http://127.0.0.1:8000/profile/').then(response => response.json())
    },
    async gettingBooks1(){
      var response = await fetch('http://127.0.0.1:8000/profile/')
      this.listB = response.json()
    
    }
  },
  components: {
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
