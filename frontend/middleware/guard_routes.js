export default function({ route, store, redirect }) {
	const routeName = route.name;
	const safeRoutes = ['create-post', 'my-posts'];
	const logged = !!store.getters.logged_user;

	if (logged && routeName === 'signup') {
		return redirect({ name: 'index' });
	}

	if (!logged && safeRoutes.includes(routeName)) {
		return redirect({ name: 'index' });
	}
}
