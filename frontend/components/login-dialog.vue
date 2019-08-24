<template>
  <v-dialog v-model="visible" max-width="500px">
    <v-card>
      <v-container fluid>
        <v-card-title>
          <p class="title">Iniciar sessão</p>
        </v-card-title>
        <v-card-text>
          <v-text-field label="Nome de usuário" required v-model="username" />
          <v-text-field
            label="Senha"
            type="password"
            required
            v-model="password"
            @keyup.enter="login()"
          />
          <small style="color: red;" v-if="error">Usuário ou senha incorretos!</small>
        </v-card-text>
        <v-card-actions>
          <v-btn class="blue--text darken-1" flat @click="close()">Cancelar</v-btn>
          <v-spacer></v-spacer>
          <v-btn
            class="blue--text darken-1"
            flat
            @click="login()"
            :loading="loading"
            :disabled="loading"
          >Entrar</v-btn>
        </v-card-actions>
      </v-container>
    </v-card>
  </v-dialog>
</template>

<script>
import AppApi from "~apijs";
import { mapActions, mapGetters } from "vuex";
import { AUTH_LOGIN, AUTH_SET_USER } from "~/store/actions.type";

export default {
  data() {
    return {
      visible: false,
      loading: false,
      username: "",
      password: "",
      error: false
    };
  },

  computed: {
    ...mapGetters(["currentUser"])
  },

  methods: {
    ...mapActions([AUTH_LOGIN]),

    open() {
      this.visible = true;
    },

    close() {
      this.visible = false;
    },

    login() {
      this.loading = true;
      this.error = false;

      const { username, password } = this;

      this[AUTH_LOGIN]({ username, password })
        .then(user => {
          this.close();
          this.$router.push({ name: "index" });
        })
        .catch(error => (this.error = true))
        .finally(() => (this.loading = false));
    }
  }
};
</script>
