<template>
  <b-container>
    <b-row class="my-5 drug-card" align-v="center" align-h="between">

      <b-col cols="9">
        <h4 style="" class="text-left font-weight-bold drug-name">
          {{ drug.name }}
        </h4>
        <div class="text-left text-muted">
          <div v-if="available">
            Цена от {{ drug.min_price }}тг
          </div>
          <ul class="pl-3">
            <li :class="drug.recipe ? 'red-dot' : 'dot'">{{ drug.recipe ? 'Только с рецептом' : 'Без рецепта' }}</li>
          </ul>
          <div v-html="drug.category_name">
            {{ drug.category_name }}
          </div>
          <div style="text-decoration: underline; color:black; cursor:pointer" class="mt-3"
               @click="showInstruction(drug.id)">
            Инструкция
          </div>
        </div>
      </b-col>

      <b-col cols="3">
        <img :src="drug.image" class="img-fluid" alt="">

      </b-col>
      <hr>
      <b-modal :id="drug.id" size="xl" :title="drug.name">
        <div v-html="drug.description">{{ drug.description }}</div>
      </b-modal>
    </b-row>
    <b-row v-for="store in stores" :key="store.id" class="my-5" align-v="center" align-h="between">
      <b-col cols="9">
        <h4  class="text-left font-weight-bold drug-name">
          {{store.store.name}}
        </h4>
        <div class="text-left">
          Цена {{store.price}}тг.
        </div>
        <div class="text-left text-muted">
          <div>
            {{store.store.address}}
          </div>
          <ul class="pl-3">
            <li class="dot">Открыто с 9:00 до 22:00</li>
          </ul>
        </div>
      </b-col>

      <b-col cols="3">
        <b-button class="btn search-btn btn-primary" type="submit" v-if="available" @click="()=>{
        clicked = true;
        $store.dispatch('addProductToCart',drug)
      }" variant="primary">{{ clicked ? 'Добавлено!' : 'Добавить в корзину' }}
        </b-button>
        <div v-else class="text-danger">
          Нет в наличии
        </div>
      </b-col>
      <hr>

    </b-row>
    <b-row v-if="stores.length===0" class="my-4">
      <h4>На данный момент, нету аптек с такими лекарствами :(</h4>
    </b-row>
  </b-container>
</template>

<script>
export default {
  name: "DrugDetail",
  data() {
    return {
      available: false,
      clicked: false,
      drug: null,
      stores: null,
    }
  },
  mounted() {
    this.$store.dispatch('fetchDrugDetail', this.$route.params.id).then(res => {
      this.drug = res.data
      if (this.drug.min_price && this.drug.min_quantity)
        this.available = true
    })
    this.$store.dispatch('fetchDrugDetailStores', this.$route.params.id).then(res => {
      this.stores = res.data.filter(store => {
        if (this.$store.state.selectedCity === store.store.city_name)
          return store
      })
    })

  },
  methods: {
    showInstruction(id) {
      this.$bvModal.show(id)
    }
  }
}
</script>

<style>

.drug-name {
  color: black !important;
}

.drug-name:hover {
  color: #505050 !important;
  cursor: pointer;
}
</style>
