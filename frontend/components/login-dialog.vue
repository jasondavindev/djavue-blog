<template>
  <v-dialog v-model="visible" max-width="500px">
    <v-card>
      <v-card-title>Iniciar sessão</v-card-title>
      <v-card-text>
        <v-container fluid>
          <v-text-field label="Nome de usuário" required v-model="username"/>
          <v-text-field
            label="Senha"
            type="password"
            required
            v-model="password"
            @keyup.enter="login()"
          />
          <small style="color: red;" v-if="error">Usuário ou senha incorretos!</small>
        </v-container>
      </v-card-text>
      <v-btn class="blue--text darken-1" flat @click="close()">Cancelar</v-btn>
      <v-btn
        class="blue--text darken-1"
        flat
        @click="login()"
        :loading="loading"
        :disabled="loading"
      >Entrar</v-btn>
    </v-card>
  </v-dialog>
</template>

<script>
import AppApi from "~apijs";

export default {
  data() {
    console.log("data");
    return {
      visible: false,
      loading: false,
      username: "",
      password: "",
      error: false
    };
  },
  methods: {
    open() {
      this.visible = true;
      console.log("Open");
    },

    close() {
      this.visible = false;
      console.log("Close");
    },

    async login() {
      this.loading = true;
      this.error = false;
      try {
        const { data } = await AppApi.login(this.username, this.password);

        if (data) {
          this.$store.commit("SET_LOGGED_USER", data);
          this.visible = false;
          console.log("logged");
          this.$router.push({ name: 'index' });
        } else {
          this.error = true;
        }
      } catch (error) {
      } finally {
        this.loading = false;
      }
    }
  }
};
</script>
