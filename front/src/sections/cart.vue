<template>
  <b-container style="height:50em">
    <b-row class="my-3">
      <h3>
        КОРЗИНА
      </h3>
    </b-row>
    <b-row align-h="between">
      <b-col cols="10">
        <div class="text-left">В корзине {{ $store.state.cartItems }} лекарства</div>
        <div class="text-left">Итого: {{$store.state.totalPrice}}тг.</div>
      </b-col>
      <b-col cols="2">
        <b-button v-b-modal.modal-1 class="search-btn">Купить</b-button>
      </b-col>
    </b-row>
    <hr>
    <DrugCardCart v-for="drug in products" :key="products.length" :drug="drug"></DrugCardCart>
    <b-modal id="modal-1" size="xl" :title="success ? 'Успешно':'Заполните данные для продолжения'">
      <b-row v-if="!success">
        <b-col cols="6">
          <div class="font-weight-bold my-3">Купить лекарства</div>

          <b-form-group
            id="input-group-1"
            label="Имя:"
            label-for="input-1"
          >
            <b-form-input
              id="input-1"
              v-model="form.name"
              type="text"
              class="form-control-pill"
              required
              placeholder=""
            ></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-2" label="Номер телефона:" label-for="input-2">
            <b-form-input
              id="input-2"
              v-model="form.phone"
              class="form-control-pill"
              required
              placeholder=""
            ></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-3" label="Адрес доставки:" label-for="input-3">
            <b-form-input
              id="input-3"
              v-model="form.address"
              class="form-control-pill"
              required
            ></b-form-input>
          </b-form-group>


        </b-col>
        <b-col cols="6">
          <div class="font-weight-bold my-3">Данные для оплаты</div>
          <b-form-group
            id="input-group-7"
            label="Имя Фамилия указанные на карте:"
            label-for="input-1"
          >
            <b-form-input
              id="input-1"
              class="form-control-pill"
              v-model="form.cart_holder"
              type="text"
              required
              placeholder=""
            ></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-5" label="Номер карты:" label-for="input-2">
            <b-form-input
              id="input-2"
              v-model="form.cart_number"
              required
              class="form-control-pill"
              placeholder=""
            ></b-form-input>
          </b-form-group>
          <b-row>
            <b-col>
              <b-form-group id="input-group-9" label="MM/YY:" label-for="input-3">
                <b-form-input
                  id="input-3"
                  class="form-control-pill"
                  v-model="form.date"
                  required
                ></b-form-input>
              </b-form-group>
            </b-col>
            <b-col>
              <b-form-group id="input-group-6" label="CVV:" label-for="input-3">
                <b-form-input
                  id="input-3"
                  class="form-control-pill"
                  v-model="form.cvv"
                  required
                ></b-form-input>
              </b-form-group>
            </b-col>
          </b-row>

        </b-col>
      </b-row>
      <b-row v-else align-h="center">
        <div class="d-flex flex-column align-items-center">
          <p v-if="success" class="h1 mt-2" style="font-size:100px!important">
            <b-icon icon="check-circle" variant="success"></b-icon>
          </p>
          <div class="my-3">Заказ принят! Ожидайте в ближайшее время!</div>
          <b-button
            variant="primary"
            class="search-btn"
            @click="closeModal('modal-1')"
          >
            Отлично!
          </b-button>
        </div>

      </b-row>
      <template #modal-footer>
        <div class="w-100">
          <b-row align-h="center">
            <b-col cols="4">
              <b-button
                v-if="!process && !success"
                variant="primary"
                class="search-btn"
                @click="processCheckout"
              >
                Оплатить
              </b-button>


              <b-spinner v-if="process" variant="success" type="grow" label="Spinning"></b-spinner>
            </b-col>

          </b-row>

        </div>
      </template>
    </b-modal>

  </b-container>
</template>

<script>
import DrugCardCart from "../components/DrugCardCart";

export default {
  name: 'cart',
  components: {
    DrugCardCart
  },
  data() {
    return {
      products: this.$store.state.cart,
      process: false,
      success: false,
      form: {
        name: null,
        phone: null,
        address: null,
        cart_holder: null,
        cart_number: null,
        date: null,
        cvv: null,

      }
    }
  },
  methods: {
    closeModal(id) {
      this.$bvModal.hide(id)
    },
    processCheckout() {
      this.process = true;
      setTimeout(() => {
        this.process = false;
        this.success = true;
        this.$store.dispatch('checkout')
        this.products = null;
      }, 1000)
    }
  }
}
</script>
<style>
.form-control-pill {
  border-radius: 50px;
}

.search-btn {
  height: 3.28em;
  border-radius: 100px;
  background: #2AB9C7;
  width: 70%;
  border: 0;
}
</style>
