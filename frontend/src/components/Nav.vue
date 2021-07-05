<template>
        <div class="navbar navbar-fixed-top">
        <div class="container">
          <h1 class="navbar-brand" style="font-size: 33px;">ExBook</h1>
          <div class="navbar-header">
            <form class="d-flex">
              <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
              <button class="btn btn-outline-success" type="submit">Search</button>
              <a><h4 style="margin: 7px;">Profile</h4></a>
            </form>
          </div>
        </div>
      </div>
</template>

<script>
    export default {
        name: "Nav"
    }
</script>

<style scoped>
    .navbar{
          margin: 0;
          width: 100%;
          height: 115px;
          background: hsl(59, 97%, 57%);
    }
</style>