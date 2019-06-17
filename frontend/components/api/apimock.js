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
	list_posts() {
		return mockasync({
			posts: [
				{
					id: 1,
					title: 'My first post',
					body:
						'Travelling alteration impression six all uncommonly. Chamber hearing inhabit joy highest private ask him our believe. Up nature valley do warmly. Entered of cordial do on no hearted. Yet agreed whence and unable limits. Use off him gay abilities concluded immediate allowance.',
					author: {
						username: 'bot',
						first_name: 'Django',
						last_name: 'Bot',
					},
					created: Date.now(),
				},
				{
					id: 2,
					title: 'Random post',
					body:
						'Sing long her way size. Waited end mutual missed myself the little sister one. So in pointed or chicken cheered neither spirits invited. Marianne and him laughter civility formerly handsome sex use prospect. Hence we doors is given rapid scale above am. Difficult ye mr delivered behaviour by an. If their woman could do wound on. You folly taste hoped their above are and but.',
					author: {
						username: 'bot',
						first_name: 'Django',
						last_name: 'Bot',
					},
					created: Date.now() + 1000,
				},
			],
		});
	},
	list_post(post) {
		return mockasync({
			post: {
				id: post,
				title: 'My first post',
				body:
					'Travelling alteration impression six all uncommonly. Chamber hearing inhabit joy highest private ask him our believe. Up nature valley do warmly. Entered of cordial do on no hearted. Yet agreed whence and unable limits. Use off him gay abilities concluded immediate allowance.',
				author: {
					username: 'bot',
					first_name: 'Django',
					last_name: 'Bot',
				},
				created: Date.now(),
			},
		});
	},
	get_my_posts() {
		return mockasync({
			posts: [
				{
					id: 1,
					title: 'My first post',
					body:
						'Travelling alteration impression six all uncommonly. Chamber hearing inhabit joy highest private ask him our believe. Up nature valley do warmly. Entered of cordial do on no hearted. Yet agreed whence and unable limits. Use off him gay abilities concluded immediate allowance.',
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
			Object.assign(post, {
				created: Date.now(),
				author: {
					username: logged_user.username,
					first_name: logged_user.first_name,
					last_name: logged_user.last_name,
				},
				id: 1,
			})
		);
	},
	list_comments(post) {
		return mockasync({
			comments: [
				{
					author: {
						username: 'johncena',
						first_name: 'John',
						last_name: 'Cena',
					},
					comment: 'Oh yeah!',
					created: Date.now(),
				},
				{
					author: {
						username: 'therock',
						first_name: 'Dwayne',
						last_name: 'Johnson',
					},
					comment: 'Easy peasy lemon squeezy!',
					created: Date.now() + 1000,
				},
			],
		});
	},
	save_comment(comment) {
		return mockasync(
			Object.assign(
				{
					created: Date.now(),
					author: {
						username: logged_user.username,
						first_name: logged_user.first_name,
						last_name: logged_user.last_name,
					},
				},
				comment
			)
		);
	},
	create_account(user) {
		return mockasync({
			username: user.username,
			first_name: user.firstname,
			last_name: user.lastname,
			email: user.email,
		});
	},
	delete_post(post) {
		return mockasync({
			deleted: true,
			post,
		});
	},
};

export default api;
