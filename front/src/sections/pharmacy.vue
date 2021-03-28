<template>
  <b-container>
    <b-row>
      <b-col cols="6">
        <b-row align-v="center" align-h="between">
          <b-col cols="12">
            <b-container>
              <b-row class="my-5">
                <h3 class="text-left" style="text-transform: uppercase;font-weight: 900;">АПТЕКИ В {{$store.state.selectedCity}}</h3>
              </b-row>
            </b-container>
          </b-col>
        </b-row>

        <b-form @submit="searchStores">
          <b-row align-v="center">
            <b-col cols="9" class="align-items-center search-input">
              <b-form-input
                id="input-1"
                type="search"
                required
                placeholder="Введите названия лекарства"
              ></b-form-input>
            </b-col>

            <b-col cols="3">
              <b-button class="search-btn" type="submit" variant="primary">Искать</b-button>
            </b-col>
          </b-row>
        </b-form>



        <b-container class="">
          <b-row class="my-5" align-v="center" align-h="between">
            <b-col cols="12">
              <div class="text-left">
                Найдено {{ countStores }} аптеки
              </div>
            </b-col>
          </b-row>

          <StoreCard v-for="store in stores" :key="stores.length" :store="store"/>

        </b-container>
        <b-row align-h="center">
          <div class="overflow-auto">
            <b-pagination-nav pills :link-gen="linkGen" :number-of-pages="countStores/6" use-router></b-pagination-nav>
          </div>
        </b-row>
      </b-col>

      <b-col cols="6">
        <yandex-map :coords="[stores[0].latitude,stores[0].longitude]" style="width: 120%;height:100%;">
          <ymap-marker :balloon="{
            header:store.name,
            body:store.phone,
            footer:store.work_time_weekdays
          }" v-for="store in stores" :key="stores.length" :coords="[store.latitude,store.longitude]"></ymap-marker>
        </yandex-map>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import StoreCard from "../components/StoreCard";

export default {
  name: "drugs",
  components: {StoreCard},
  data() {
    return {
      stores: null,
      countStores: 0
    }
  },
  watch: {
    '$route': function (to, from) {
      const page = parseInt(this.$route.query.page)
      this.$store.dispatch('fetchStores', 6 * page).then(res => {
        this.countStores = res.data.count;
        this.stores = res.data.results
      })
    }
  },
  methods: {
    linkGen(pageNum) {
      return pageNum === 1 ? '?' : `?page=${pageNum}`
    },
    searchStores(e){
      e.preventDefault()
      this.$store.dispatch('searchStores',e.target[0].value).then(res=>{
        this.countStores = res.data.count;
        this.stores = res.data.results
      })
    }
  },
  mounted() {
    this.$store.dispatch('fetchStores').then(res => {
      this.countStores = res.data.count;
      this.stores = res.data.results
    })
  }
}
</script>

<style>
.page-link {
  color: #225195;
}

ul {
  list-style: none; /* Remove default bullets */
}

.dot::before {
  content: "\2022"; /* Add content: \2022 is the CSS Code/unicode for a bullet */
  color: #B3E5B2; /* Change the color */
  font-weight: bold; /* If you want it to be bold */
  display: inline-block; /* Needed to add space between the bullet and the text */
  width: 1em; /* Also needed for space (tweak if needed) */
  margin-left: -1em; /* Also needed for space (tweak if needed) */
}

.search-input input[type='search'] {
  color: #5044ff;
  border-radius: 100px;
  border: 1px solid #225195;
  padding: 12px 24px;
  height: 3.28em;

}

.search-btn {
  height: 3.28em;
  border-radius: 100px;
  background: #2AB9C7;
  width: 70%;
  border: 0;
}

.call-btn {
  border-radius: 50%;
  background: #2AB9C7;
  border: 0;
  width: 3.5rem;
  height: 3.5rem;
}
</style>

