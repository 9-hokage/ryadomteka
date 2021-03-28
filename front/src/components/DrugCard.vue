<template>
  <b-row class="my-5 drug-card" align-v="center" align-h="between">

    <b-col cols="9">
      <router-link :to="'/drugs/'+drug.id+'/'">

      <h4 @click="showInstruction(drug.id)" style="" class="text-left font-weight-bold drug-name">
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
      </div>
      </router-link>

    </b-col>

    <b-col cols="3">
      <b-button class="search-btn" type="submit" v-if="available" @click="()=>{
        clicked = true;
        $store.dispatch('addProductToCart',drug)
      }" variant="primary">{{ clicked ? 'Добавлено!' : 'Добавить в корзину' }}
      </b-button>
      <div v-else class="text-danger">
        Нет в наличии
      </div>
    </b-col>
    <hr>
    <b-modal :id="drug.id" size="xl" :title="drug.name">
      <div v-html="drug.description">{{ drug.description }}</div>
    </b-modal>
  </b-row>

</template>

<script>
export default {
  name: "DrugCard",
  props: [
    'drug'
  ],
  data() {
    return {
      available: false,
      clicked: false
    }
  },
  mounted() {
    if (this.drug.min_price && this.drug.min_quantity)
      this.available = true
  },
  methods: {
    showInstruction(id) {
      this.$bvModal.show(id)
    }
  }
}
</script>

<style>

.drug-card:hover {
  background-color: rgba(0, 0, 0, 0.01);
}
</style>
