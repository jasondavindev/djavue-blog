<template>
  <v-layout row wrap justify-center>
    <v-flex xs12 sm10 md8 lg6>
      <v-card class="pa-3">
        <v-card-title>
          <p class="title">Fazer cadastro</p>
        </v-card-title>
        <v-card-text>
          <v-text-field
            v-model="username"
            ref="username"
            label="Nome de usuário"
            :rules="[fieldRequired, validUser]"
          ></v-text-field>
          <v-text-field
            v-model="firstname"
            ref="firstname"
            label="Primeiro nome"
            :rules="[fieldRequired]"
          ></v-text-field>
          <v-text-field
            v-model="lastname"
            ref="lastname"
            label="Último nome"
            :rules="[fieldRequired]"
          ></v-text-field>
          <v-text-field
            v-model="email"
            ref="email"
            label="E-mail"
            :rules="[fieldRequired, isEmail]"
          ></v-text-field>
          <v-text-field
            v-model="password"
            ref="password"
            label="Senha"
            type="password"
            :rules="[fieldRequired, strongPassword]"
          ></v-text-field>
          <span v-if="error" class="red--text">Não foi possível criar sua conta</span>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            flat
            @click="submit"
            :loading="registering"
            :disabled="registering"
          >Cadastrar</v-btn>
        </v-card-actions>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
import AppApi from "~apijs";

export default {
  data() {
    return {
      username: null,
      firstname: null,
      lastname: null,
      email: null,
      password: null,
      registering: false,
      error: false,
    };
  },

  computed: {
    form() {
      return {
        username: this.username,
        firstname: this.firstname,
        lastname: this.lastname,
        email: this.email,
        password: this.password
      };
    }
  },

  methods: {
    validUser(value) {
      if (value && /\W/g.test(value)) {
        return "Insira um usuário com somente letras e números";
      }

      return true;
    },

    submit() {
      this.validateForm() && this.createAccount(this.form);
    },

    async createAccount(user) {
      this.registering = true;

      try {
        const { data } = await AppApi.create_account(user);
        this.validAccount(data);
      } catch (error) {
      } finally {
        this.registering = false;
      }
    },

    validAccount(data) {
      if (data.created) {
        this.redirectToIndex();
      } else {
        this.error = true;
      }
    },

    redirectToIndex() {
      this.$router.push({ name: "index" });
    }
  }
};
</script>
