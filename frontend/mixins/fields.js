import Vue from 'vue';

Vue.mixin({
	methods: {
		fieldRequired(value) {
			return !!value || 'Preencha este campo';
		},
		
		logged() {
      return (
        !!this.$store.getters.logged_user ||
        "Você precisa estar logado para fazer um comentário"
      );
		},
		
		validateForm() {
      return Object.keys(this.$refs).every(ref => this.$refs[ref].validate(true) === true);
    },
	},
});
