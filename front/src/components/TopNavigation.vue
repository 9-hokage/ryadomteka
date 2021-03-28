<template>
  <b-navbar toggleable="lg" sticky>
    <b-container fluid>
      <b-navbar-brand
        class="d-flex justify-content-around align-items-center col-9 col-sm-5 col-md-3 col-lg-3 col-xl-3 ">
        <router-link to="/" class="d-flex justify-content-center align-items-center" exact>
          <div class="logo">
            <logo></logo>
          </div>

        </router-link>
        <router-link to="/drugs">Лекарства</router-link>
        <router-link to="/pharmacy">Аптеки</router-link>
      </b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav align="end" class="w-100">
          <b-row align-content="center" align-h="end" class="w-50">
            <div class="d-flex col-9 justify-content-between">
              <router-link to="/cart">
                <b-row class="text-center" align-v="center">

                  <b-button style="background-color: #2AB9C7;border:0;border-radius:50%;width:3.5rem;height: 3.5rem;">
                    <b-icon font-scale="2" icon="cart" variant="#fff"></b-icon>
                  </b-button>
                </b-row>

              </router-link>

              <v-select v-if="cities" class="header-button-outline" v-model="selectedCity"
                        :clearable="false"
                        :options="cities"></v-select>
            </div>
          </b-row>


        </b-navbar-nav>

      </b-collapse>
    </b-container>

    <!--    <div class="container-fluid">-->
    <!--      <div class="d-flex justify-content-between align-items-center row ">-->
    <!--        <div class="">-->


    <!--        </div>-->

    <!--        <div class="d-flex justify-content-between align-items-center flex-row col-lg-3">-->

    <!--        </div>-->


    <!--      </div>-->
    <!--    </div>-->


    <!--    <div class="nav-link">-->
    <!--      <router-link to="/cart" exact>-->
    <!--        <div class="cart-link">-->
    <!--          <div v-if="noItems > 0" class="cart-link__count">{{ noItems }}</div>-->
    <!--          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" aria-labelledby="shopicon" role="presentation"-->
    <!--               width="30" height="30">-->
    <!--            <title id="cart">-->
    <!--              Shopping Cart-->
    <!--            </title>-->
    <!--            <path fill="black"-->
    <!--                  d="M8.01 10c-1.104 0-2 .896-2 2 0 1.105.896 2 2 2h10.376l10.53 49.813c-.107 1.14.952 2.245 2.095 2.187h50c1.057.015 2.03-.943 2.03-2s-.973-2.015-2.03-2H32.637l-1.688-8H85.01c.896-.01 1.742-.69 1.938-1.562l7-30c.26-1.16-.748-2.43-1.937-2.438H23.76l-1.78-8.437c-.2-.884-1.063-1.57-1.97-1.563zm16.594 14H89.51l-6.093 26H30.104zM42.01 72c-4.946 0-9 4.053-9 9s4.054 9 9 9c4.948 0 9-4.053 9-9s-4.052-9-9-9zm28 0c-4.946 0-9 4.053-9 9s4.054 9 9 9c4.948 0 9-4.053 9-9s-4.052-9-9-9zm-28 4c2.786 0 5 2.215 5 5s-2.214 5-5 5c-2.784 0-5-2.215-5-5s2.216-5 5-5zm28 0c2.786 0 5 2.215 5 5s-2.214 5-5 5c-2.784 0-5-2.215-5-5s2.216-5 5-5z"/>-->
    <!--          </svg>-->
    <!--        </div>-->
    <!--      </router-link>-->
    <!--    </div>-->
  </b-navbar>
</template>

<script>
import index from '@/store/index'
import logo from '@/assets/logo'

export default {
  name: 'TopNavigation',
  components: {
    logo
  },
  data() {
    return {
      selectedCity: this.$store.state.selectedCity ? this.$store.state.selectedCity : 'Selected City'
    }
  },
  watch: {
    selectedCity: function (val) {
      this.$store.commit('setCity', val)
    }
  },
  computed: {
    noItems() {
      return this.$store.state.cartItems
    },
    cities() {
      return this.$store.state.cities.map(city => {
        return city.name
      })


    }
  }
}
</script>

<style lang="css">
nav {
  background-color: #FFFFFF;
}

/*nav {*/
/*  box-shadow: 1px 0rem 14px 0px #eee;*/
/*  width: 100%;*/
/*  padding: 24px;*/
/*  position: sticky;*/
/*  height: 6.8em;*/
/*  background-color: #fff;*/
/*  z-index: 99;*/
/*}*/

/*nav > a {*/
/*  font-size: 18px;*/
/*  color: #225195;*/
/*  text-decoration: none;*/
/*  !*margin-right: 50px;*!*/
/*  font-weight: 500;*/
/*  letter-spacing: 0.5px;*/
/*}*/

nav a:hover {
  opacity: 0.7;
}

nav a.router-link-active {
  color: #5044ff;
}

.logo {
  position: relative;
  /*top: -7px;*/
}

.logo svg {
  width: 4.2em;
  height: 4.2em;
}

@media (max-width: 600px) {
  nav {
    padding: 20px;
  }

  nav > a {
    margin-right: 20px;
  }
}

.nav-link {
  display: inline;
}

.cart-link {
  float: right;
  position: relative;
}

.cart-link__count {
  position: absolute;
  width: 20px;
  height: 20px;
  border-radius: 100%;
  top: -8px;
  right: -5px;
  background: #5044ff;
  color: #fff;
  font-size: 14px;
  font-weight: bold;
}
</style>
