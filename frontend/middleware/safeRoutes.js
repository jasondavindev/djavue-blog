export const authenticatedRoutes = ['create-post', 'my-post'];

export const isAuthenticatedRoute = (routeName) => authenticatedRoutes.includes(routeName);

export const isAuthenticated = (store) => store.getters.isAuthenticated === true;

export const redirectToIndex = (redirect) => redirect({ name: 'index' });

export default ({ route, store, redirect }) => {
  if (isAuthenticatedRoute(route.name) && !isAuthenticated(store)) {
    return redirectToIndex(redirect);
  }
};
