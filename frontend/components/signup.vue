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
            @click="createAccount"
            :loading="registering"
            :disabled="registering"
          >Cadastrar</v-btn>
        </v-card-actions>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
import { mapActions } from "vuex";
import { AUTH_REGISTER, AUTH_SET_ERROR } from "~/store/actions.type";
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
      error: false
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
    ...mapActions([AUTH_REGISTER, AUTH_SET_ERROR]),

    createAccount() {
      this.validAccount()
        .then(this[AUTH_REGISTER])
        .then(() => this.$router.push({ name: "index" }))
        .catch(error => {
          this[AUTH_SET_ERROR](error);
          this.error = true;
        })
        .finally(() => (this.registering = false));
    },

    validAccount() {
      return new Promise((resolve, reject) => {
        if (!this.validateForm()) {
          return reject("INVALID ACCOUNT DATA");
        }

        this.registering = true;
        resolve(this.form);
      });
    },

    validUser(value) {
      if (value && /\W/g.test(value)) {
        return "Insira um usuário com somente letras e números";
      }

      return true;
    }
  }
};
</script>
