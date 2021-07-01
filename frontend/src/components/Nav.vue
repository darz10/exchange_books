<template>
     <div class="nav">
       <div class="align-self-center" style="margin:15px;">
          <h1 align="center">Exchange books</h1>
       </div>
        <div class="search">
          <form>
            <div class="d-flex flex-row-reverse bd-highlight">
              <div class="p-2 bd-highlight" style="margin-left:-10px;">
                <button class="btn btn-success">Search</button>
              </div>
              <div class="p-2 bd-highlight">
                <input class="form-control" type="text" placeholder="Search">
              </div>
            </div>
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
          margin-left: 50px;
        }
</style>