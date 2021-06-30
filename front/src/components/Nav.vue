<template>
     <div class="nav">
        <div class="position-relative top-100 start-50 translate-middle mt-1 bi bi-caret-down-fill">
          <h1 align="center">Exchange books</h1>
        </div>
        <div class="search">
          <form>
            <div class="search-area">
              <input class="form-control" type="text" placeholder="Search">
            </div>
            <button class="btn btn-success">Search</button>
          </form>
        </div>
      </div>
</template>

<script>
    export default {
        name: "Nav"
    }
</script>

<style scoped>
    .nav{
          margin: 0;
          width: 100%;
          height: 150px;
          background: hsl(59, 97%, 57%);
        }
        .position-relative{
          margin-bottom: -60px;
        }
</style>