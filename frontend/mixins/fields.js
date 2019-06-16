import Vue from 'vue';

const emailReg = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

Vue.mixin({
	methods: {
		fieldRequired(value) {
			return !!value || 'Preencha este campo';
		},

		logged() {
			return (
				!!this.$store.getters.logged_user || 'Você precisa estar logado para fazer um comentário'
			);
		},

		isEmail(value) {
			return emailReg.test(value) || 'Preencha um e-mail válido';
		},

		validateForm() {
			return Object.keys(this.$refs).every(ref => this.$refs[ref].validate(true) === true);
		},

		strongPassword(value) {
			return (value && value.length >= 5) || 'Senha deve conter pelo menos 5 caracteres';
		}
	},
});
