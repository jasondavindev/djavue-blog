import Vuex from 'vuex';

import AuthModule from '~/store/modules/auth.module.js';
import SnackModule from '~/store/modules/snack.module.js';

export default () =>
  new Vuex.Store({
    modules: {
      AuthModule,
      SnackModule,
    },
    actions: {
      nuxtServerInit({ commit }, { req }) {},
    },
  });
