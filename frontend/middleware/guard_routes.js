export default function({ route, store, redirect }) {
	const routeName = route.name;
	const safeRoutes = ['create-post'];
	const logged = !!store.getters.logged_user;

	if (!logged && safeRoutes.includes(routeName)) {
		return redirect({ name: 'index' });
	}
}
