import Vue from 'vue'
import Vuex from 'vuex'
import actions from './actions'
import getters from './getters'
import mutations from './mutations'

Vue.use(Vuex)

export default new Vuex.Store({
  state: { // = data
    products: [],
    cart: [],
    cartItems: 0,
    totalPrice: 0,
    checkoutStatus: null,
    highprice: 1500,
    sale: false,
    cities: [],
    selectedCountry: localStorage.getItem('selectedCountry') || null,
    countries: [],
    selectedCity: localStorage.getItem('selectedCity') || null,
  },
  getters,
  actions,
  mutations
})
