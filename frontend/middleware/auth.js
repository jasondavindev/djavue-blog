import { AUTH_SET_USER, AUTH_UNSET_USER, AUTH_CHECK } from '~/store/actions.type';

export default function(ctx) {
  if (ctx.store.getters.currentUser === null) {
    return ctx.store.dispatch(AUTH_CHECK).then((response) => {
      if (response.data.authenticated) {
        ctx.store.dispatch(AUTH_SET_USER, response.data.user);
      } else {
        ctx.store.dispatch(AUTH_UNSET_USER);
      }
    });
  }
}
