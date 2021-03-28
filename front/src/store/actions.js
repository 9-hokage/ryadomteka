import shop from '@/api/shop'
import axios from 'axios'

axios.defaults.baseURL = 'http://localhost:8000/api'
// axios.defaults.headers.common['Accept'] = 'application/json'
export default { // actions = mehtods
  async fetchDrugs(state, offset) {
    if (offset)
      return await axios.get(`/drugs/?limit=12&offset=${offset}`,)
    return await axios.get(`/drugs/`,)
  },
  async fetchStatistics(state) {
    return await axios.get(`/statistics/?country=${state.state.selectedCountry}`,)
  },
  fetchCities(context) {
    return new Promise(function (resolve, reject) {
      axios.get(`/cities/`).then(res => {
        context.commit('setCities', res.data)
        resolve();
      })
    })
  },
  async fetchDrugDetail(state, id) {
    return await axios.get(`/drugs/${id}/`)
  },
  async fetchDrugDetailStores(state, id) {
    return await axios.get(`/drugs/${id}/stores/`)
  },
  async fetchStores(state, offset) {
    console.log(state)
    if (offset)
      return await axios.get(`/stores/?limit=6&offset=${offset}&city=${state.state.selectedCity}`,)
    return await axios.get(`/stores/?city=${state.state.selectedCity}`,)
  },
  async searchDrugs(state, name) {
    console.log(name)
    return await axios.get(`/drugs/?search=${name}`)
  },
  async searchStores(state, name) {
    console.log(name)
    return await axios.get(`/stores/?city=${state.state.selectedCity}&search=${name}`)
  },
  fetchCountries(context) {
    return new Promise(function (resolve, reject) {
      axios.get(`/countries/`).then(res => {
        context.commit('setCountries', res.data)
        resolve();
      })
    })
  },
  fetchProducts(context) {
    return new Promise(function (resolve, reject) {
      shop.getProducts(products => {
        context.commit('setProducts', products)
        resolve();
      })
    })
  },

  addProductToCart(context, product) {
    // if(product.inventory > 0)
    console.log(product)

    const cartItem = context.state.cart.find(item => item.id === product.id)
    if (!cartItem) {
      context.commit('pushProductToCart', product)
    } else {
      context.commit('incrementItemQty', cartItem)
    }

    // context.commit('decrementProductInventory', product)

    
  },

  checkout(context) {
    context.commit('emptyCart')
    context.commit('setCheckoutStatus', 'success')
  }
}
