<template>
 <b-container fluid class="footer">
  <b-row class="h-100" align-h="center">
    <b-col cols="3">
      <b-row align-h="center" class="m-5">
        <div class="logo-inverse"></div>
      </b-row>
      <b-row  align-h="center" class="d-flex flex-column align-items-center my-5">
        <router-link class="footer-link" to="/furniture">Аптеки</router-link>
        <router-link class="footer-link" to="/decor">Лекарства</router-link>
      </b-row>
    </b-col>
    <b-col>

    </b-col>
    <b-col>
      <div class="footer-img"></div>
    </b-col>

  </b-row>
 </b-container>
</template>

<script>
export default {
}
</script>

<style lang="css">
footer {
  text-align: center;
  font-size: 16px;
  padding: 20px;
}
</style>
