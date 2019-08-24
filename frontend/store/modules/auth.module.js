import ApiService from '~apijs';
import {
  AUTH_LOGIN,
  AUTH_LOGOUT,
  AUTH_REGISTER,
  AUTH_CHECK,
  AUTH_VALIDATE_LOGIN,
  AUTH_VALIDATE_REGISTER,
  AUTH_SET_ERROR,
  AUTH_SET_USER,
  AUTH_UNSET_USER,
} from '~/store/actions.type';

const state = {
  errors: null,
  user: null,
  isAuthenticated: false,
};

const getters = {
  currentUser(state) {
    return state.user;
  },

  isAuthenticated(state) {
    return state.isAuthenticated;
  },
};

const actions = {
  [AUTH_LOGIN]({ commit, dispatch }, credentials) {
    return ApiService.login(credentials.username, credentials.password)
      .then(({ data }) => dispatch(AUTH_VALIDATE_LOGIN, data))
      .then((data) => commit('setAuth', data));
  },

  [AUTH_REGISTER]({ commit, dispatch }, credentials) {
    return ApiService.createAccount(credentials).then(({ data }) => dispatch(AUTH_VALIDATE_REGISTER, data));
  },

  [AUTH_LOGOUT]({ commit }) {
    return ApiService.logout().then(() => commit('logout'));
  },

  [AUTH_CHECK]({ commit }) {
    return ApiService.whoami().catch(({ response }) => commit('setErrors', response.data.errors));
  },

  [AUTH_VALIDATE_LOGIN](context, data) {
    return new Promise((resolve, reject) => {
      if (data === null) {
        return reject('INVALID USER');
      }

      resolve(data);
    });
  },

  [AUTH_VALIDATE_REGISTER](context, data) {
    return new Promise((resolve, reject) => {
      if (data.created === false) {
        return reject('NOT CREATED');
      }

      resolve(data);
    });
  },

  [AUTH_SET_ERROR]({ commit }, error) {
    return commit('setErrors', error);
  },

  [AUTH_SET_USER]({ commit }, user) {
    return commit('setAuth', user);
  },

  [AUTH_UNSET_USER]({ commit }) {
    return commit('unsetAuth');
  },
};

const mutations = {
  setAuth(state, user) {
    state.errors = null;
    state.user = user;
    state.isAuthenticated = true;
  },

  setErrors(state, error) {
    return (state.errors = error);
  },

  logout(state) {
    state.isAuthenticated = false;
    state.user = null;
    state.errors = null;
  },

  unsetAuth(state) {
    state.errors = null;
    state.user = null;
    state.isAuthenticated = false;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
