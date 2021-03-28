import Vue from 'vue'
import Router from 'vue-router'
import cart from '@/sections/cart'
import drugs from '@/sections/drugs'
import pharmacy from '@/sections/pharmacy'
import Landing from "../pages/Landing";
import DrugDetail from "../components/DrugDetail";

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'index',
      component: Landing,
    },
    {
      path: '/cart',
      name: 'cart',
      component: cart
    },
    {
      path: '/drugs',
      name: 'drugs',
      component: drugs
    },
    {
      path: '/drugs/:id',
      name: 'drugsDetail',
      component: DrugDetail
    },
    {
      path: '/pharmacy',
      name: 'pharmacy',
      component: pharmacy
    }
  ]
})
