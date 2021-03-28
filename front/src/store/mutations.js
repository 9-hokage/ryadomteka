import shop from '@/api/shop'

export default { // setting and updating the state
  setProducts(state, products) {
    state.products = products
  },

  pushProductToCart(state, product) {
    state.cart.push({product: product, quantity: 1})
    state.totalPrice += product.price
    state.cartItems++
  },
  incrementItemQty(state, cartItem) {
    cartItem.quantity++
    state.cartItems++
  },
  decrementProductInventory(state, product) {
    product.inventory--
  },
  setCheckoutStatus(state, status) {
    state.checkoutStatus = status
  },
  emptyCart(state) {
    state.cart = []
    state.cartItems = 0
    state.totalPrice = 0
  },
  setHighPrice(state, event) {
    state.highprice = event
  },
  toggleSale(state) {
    state.sale = !state.sale
  },
  setCities(state, cities) {
    state.cities = cities
  },
  setCountries(state, countries) {
    state.countries = countries
  },
  setCountry(state, country) {
    state.selectedCountry = country;
    localStorage.setItem('selectedCountry', state.selectedCountry);
  },
  setCity(state, city) {
    state.selectedCity = city;
    localStorage.setItem('selectedCity', state.selectedCity);
    window.location.reload()
  }
}
