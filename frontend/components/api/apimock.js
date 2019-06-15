let logged_user = null;

function mockasync(data) {
	return new Promise((resolve, reject) => {
		setTimeout(() => resolve({ data: data }), 600);
	});
}

const api = {
	login(username, password) {
		if (password) {
			logged_user = {
				username: username,
				first_name: 'Django',
				last_name: 'Bot',
				email: 'bot@mail.com',
				notifications_enabled: true,
				permissions: {
					ADMIN: username == 'admin',
					STAFF: username == 'admin',
				},
			};
		}
		return mockasync(logged_user);
	},
	logout() {
		logged_user = null;
		return mockasync({});
	},
	whoami() {
		return mockasync(
			logged_user
				? {
						authenticated: true,
						user: logged_user,
					}
				: { authenticated: false }
		);
	},
	add_todo() {},
	list_todos() {},
	list_posts() {
		return mockasync({
			posts: [
				{
					title: 'My first post',
					body: 'This is my first post',
					author: {
						username: 'bot',
						first_name: 'Django',
						last_name: 'Bot',
					},
					created: Date.now(),
				},
				{
					title: 'Random post',
					body: 'Random content',
					author: {
						username: 'bot',
						first_name: 'Django',
						last_name: 'Bot',
					},
					created: Date.now(),
				},
			],
		});
	},
	create_post(post) {
		return mockasync(
			Object.assign(
				{
					data: post,
				},
				{
					created: Date.now(),
					author: {
						username: logged_user.username,
						first_name: logged_user.first_name,
						last_name: logged_user.last_name,
					},
				}
			)
		);
	},
};

export default api;
