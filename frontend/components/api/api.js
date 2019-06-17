import axios from '~/helpers/axios';

axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.xsrfCookieName = 'csrftoken';

const get = (url, params) => axios.get(url, { params });
const axios_delete = url => axios.delete(url);
const post = (url, params) => {
	var fd = new FormData();
	params = params || {};
	Object.keys(params).map(k => {
		fd.append(k, params[k]);
	});
	return axios.post(url, fd);
};

export default {
	/** user */
	login: (username, password) => post('/api/login', { username, password }),
	logout: () => post('/api/logout'),
	whoami: () => get('/api/whoami'),
	create_account: user => post('/api/signup', user),

	/** post */
	create_post: _post => post('/api/posts', _post),
	list_post: post => get(`/api/posts/${post}`),
	list_posts: () => get('/api/posts'),
    delete_post: post => axios_delete(`/api/posts/${post}`),
    get_my_posts: () => get('/api/my-posts'),

	/** comment */
	save_comment: comment => post('/api/comments', comment),
	list_comments: post => get(`/api/posts/${post}/comments`),
};
