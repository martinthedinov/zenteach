import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import router from './router'
import AuthPlugin from './plugins/auth'
import store from './store'

Vue.config.productionTip = false
Vue.use(AuthPlugin)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
