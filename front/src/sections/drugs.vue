<template>
  <b-container>
    <b-row align-v="center" align-h="between">
      <b-col cols="6">
        <b-container>
          <b-row align-h="left" class="my-5">
            <h3 class="text-left" style="text-transform: uppercase;font-weight: 900;">поиск лекарств</h3>
          </b-row>
        </b-container>
      </b-col>
    </b-row>

    <b-form @submit="searchDrug">
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

    <b-container class="my-5">
      <b-row class="my-5" align-v="center" align-h="between">
        <b-col cols="12">
          <div class="text-left">
            Найдено {{ countDrugs }} лекарств
          </div>
        </b-col>
      </b-row>

      <DrugCard v-for="drug in drugs" :drug="drug" :key="drugs.length"></DrugCard>

    </b-container>
    <b-row align-h="center">
      <div class="overflow-auto">
        <b-pagination-nav pills :link-gen="linkGen" :number-of-pages="countDrugs/12" use-router></b-pagination-nav>
      </div>
    </b-row>
  </b-container>
</template>

<script>
import DrugCard from '@/components/DrugCard'

export default {
  name: "drugs",
  components: {DrugCard},
  data() {
    return {
      drugs: null,
      countDrugs: 0
    }
  },
  watch: {
    '$route': function (to, from) {
      const page = parseInt(this.$route.query.page)
      this.$store.dispatch('fetchDrugs', 12 * page).then(res => {
        this.countDrugs = res.data.count;
        this.drugs = res.data.results
      })
    }
  },
  mounted() {

    this.$store.dispatch('fetchDrugs').then(res => {
      this.countDrugs = res.data.count;
      this.drugs = res.data.results
    })
  },
  methods: {
    searchDrug(e) {
      e.preventDefault()
      console.log(e.target[0].value)
      this.$store.dispatch('searchDrugs', e.target[0].value).then(res => {
        this.countDrugs = res.data.count;
        this.drugs = res.data.results
      })
    },
    linkGen(pageNum) {
      return pageNum === 1 ? '?' : `?page=${pageNum}`
    }
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
  color: lawngreen; /* Change the color */
  font-weight: bold; /* If you want it to be bold */
  display: inline-block; /* Needed to add space between the bullet and the text */
  width: 1em; /* Also needed for space (tweak if needed) */
  margin-left: -1em; /* Also needed for space (tweak if needed) */
}

.red-dot::before {
  content: "\2022"; /* Add content: \2022 is the CSS Code/unicode for a bullet */
  color: red; /* Change the color */
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

.drug-name {
  color: black !important;
}

.drug-name:hover {
  color: #505050 !important;
  cursor: pointer;
}
</style>

