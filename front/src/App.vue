<template>
  <div id="app">
    <TopNavigation/>
    <div style="min-height:52vh;" class="container-fluid">
      <router-view/>
    </div>
    <Footer/>
  </div>
</template>

<script>
import TopNavigation from '@/components/TopNavigation'
import Footer from '@/components/Footer'

export default {
  name: 'App',
  components: {
    Footer,
    TopNavigation
  },
  mounted() {
    this.$store.dispatch('fetchCities');
    this.$store.dispatch('fetchCountries')
  }
}
</script>
<style> @import './assets/styles.css'; </style>
