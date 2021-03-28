<template>
  <b-container fluid="">
    <div class="row">
      <div class="col-12 col-sm-12 col-md-5 col-lg-5 col-xl-5 d-flex justify-content-center align-items-center">
        <div class="col-9" style="">
          <h1 class="text-left">РЯДОМ-ТЕКА</h1>
          <h4 class="text-left">Ваш виртуальный помощник по уходу за здоровьем</h4>
          <b-row align-h="start">
            <b-col cols="8" class="text-left">
              <router-link to="/drugs">
                <button class="help-button mt-5">Мне нужна помощь!</button>
              </router-link>

            </b-col>

          </b-row>
        </div>

      </div>
      <div class="col-sm-7">
        <div class="hero-background">
        </div>
      </div>


      <!--      choose-block-->
      <b-container class="my-4">
        <b-row align-h="around">
          <b-col cols="4">
            <router-link to="/pharmacy">
              <div class=" choose-block d-flex flex-column align-items-center justify-content-center h-100 ">
                <div class="drugs-store">
                </div>
                <h3 class="mt-4">АПТЕКИ</h3>
              </div>
            </router-link>


          </b-col>
          <b-col cols="4">
            <router-link to="/drugs">
              <div class="choose-block d-flex flex-column align-items-center justify-content-center h-100 ">
                <div class="drugs mr-2">
                </div>
                <h3 class="mt-3">ЛЕКАРСТВА</h3>
              </div>
            </router-link>

          </b-col>
        </b-row>
      </b-container>
      <!--      end-choose-block-->

      <b-container fluid class="my-4">
        <b-row align-h="around">
          <b-col>
            <h4>
              Статистика COVID-19
            </h4>
          </b-col>

        </b-row>
        <b-row align-h="around">
          <b-col cols="10">

            <line-chart class="my-3" :options="options" v-if="chartData.datasets[0].data.length>100"
                        :chart-data="chartData"></line-chart>
            <v-select v-if="countries" class="header-button-outline" v-model="selectedCountry"
                      :clearable="false"
                      :options="countries"></v-select>
          </b-col>
        </b-row>
      </b-container>

    </div>

  </b-container>

</template>

<script>
import LineChart from '../components/LineChart.js'

export default {
  name: "Landing",
  components: {
    LineChart
  },
  data() {
    return {
      options: {
        title: 'TESt',
        maintainAspectRatio: false,
        scales: {

          xAxes: [{
            gridLines: {
              display: false,
            },
            type: 'time',
            time: {
              unit: 'month',
              stepSize: 20
            },
            distribution: 'series'
          }]
        },
      },
      datacollection: null,
      selectedCountry: this.$store.state.selectedCountry ? this.$store.state.selectedCountry : 'Selected country',
      chartData: {
        labels: [],
        datasets: [
          {
            label: this.$store.state.selectedCountry,
            backgroundColor: '#225195',
            pointRadius: 2,
            data: []
          }
        ]
      },
    }
  },
  mounted() {
    this.fillData()
    this.$store.dispatch('fetchStatistics').then(obj => {
      console.log(obj.data)
      for (let countryCase of obj.data) {
        this.chartData.labels.push(new Date(countryCase.case_date).toDateString())
        this.chartData.datasets[0].data.push(countryCase.cases)
      }

    })
  },
  watch: {
    selectedCountry: function (val) {
      this.$store.commit('setCountry', val)
      this.chartData = {
        labels: [],
        datasets: [
          {
            label: this.$store.state.selectedCountry,
            backgroundColor: '#225195',
            pointRadius: 2,
            data: []
          }
        ]
      }
      this.$store.dispatch('fetchStatistics').then(obj => {
        console.log(obj.data)
        for (let countryCase of obj.data) {
          this.chartData.labels.push(new Date(countryCase.case_date).toDateString())
          this.chartData.datasets[0].data.push(countryCase.cases)
        }

      })
    }
  },
  computed: {
    countries() {
      return this.$store.state.countries.map(city => {
        return city.name
      })
    }
  },
  methods: {
    fillData() {
      this.datacollection = {
        labels: [this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt()],
        datasets: [
          {
            label: 'Data One',
            backgroundColor: '#f87979',
            data: [this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt()]
          }, {
            label: 'Data One',
            backgroundColor: 'green',
            data: [this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt()]
          }
        ]
      }
    },
    getRandomInt() {
      return Math.floor(Math.random() * (100 - 5 + 1)) + 5
    }
  }
}
</script>

<style>
body {
  background-color: #FDFDFD;
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
</style>
