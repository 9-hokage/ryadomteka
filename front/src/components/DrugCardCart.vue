<template>
  <b-row class="my-5" align-v="center" align-h="between">
    <b-col cols="9">
      <h4 @click="showInstruction(drug.product.id)" style="" class="text-left font-weight-bold drug-name">
        {{ drug.product.name }}   <span style="color:#2AB9C7"> x{{drug.quantity}}</span>
      </h4>
      <div class="text-left text-muted">
        <div v-if="available">
          Цена {{ drug.product.price }}тг
        </div>
        <ul class="pl-3">
          <li :class="drug.product.recipe ? 'red-dot' : 'dot'">{{ drug.product.recipe ? 'Только с рецептом' : 'Без рецепта' }}</li>
        </ul>
        <div>
          {{drug.product.category}}
        </div>
      </div>
    </b-col>

    <b-col cols="3">
      <b-button class="search-btn" type="submit" v-if="available" @click="$store.dispatch('addProductToCart',drug)" variant="primary">Убрать из корзины</b-button>
      <div v-else class="text-danger">
        Нет в наличии
      </div>
    </b-col>
    <hr>
    <b-modal :id="drug.product.id" size="xl" :title="drug.product.name">
      <div v-html="drug.product.description">{{drug.product.description}}</div>
    </b-modal>
  </b-row>

</template>

<script>
export default {
  name: "DrugCard",
  props: [
    'drug'
  ],
  data(){
    return{
      available:false,
    }
  },
  mounted(){
    if (this.drug.product.price && this.drug.quantity)
      this.available = true
  },
  methods: {
    showInstruction(id){
      this.$bvModal.show(id)
    }
  }
}
</script>

<style scoped>
.but-btn{

}
</style>
