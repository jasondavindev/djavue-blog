<template>
  <v-toolbar color="info" dark fixed app clipped-right>
    <v-toolbar-title @click.stop="toIndex">Djavue Blog</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-btn
      outline
      round
      dark
      :ripple="false"
      :to="{ name: 'create-post' }"
      v-if="currentUser"
    >Postar</v-btn>
    <v-btn v-if="!currentUser" flat dark ripple @click.stop="goToSignUp()">Cadastrar</v-btn>
    <v-btn v-if="!currentUser" flat dark ripple @click.stop="openLoginDialog()">Entrar</v-btn>
    <v-menu v-if="currentUser" offset-y>
      <v-btn icon slot="activator" class="ma-0 ml-3">
        <v-avatar size="36px">
          <img src="https://graph.facebook.com/4/picture?width=300&height=300" />
        </v-avatar>
      </v-btn>
      <v-card class="no-padding">
        <v-list two-line>
          <v-list-tile avatar>
            <v-list-tile-avatar>
              <v-avatar>
                <img src="https://graph.facebook.com/4/picture?width=300&height=300" />
              </v-avatar>
            </v-list-tile-avatar>
            <v-list-tile-content>
              <v-list-tile-title>{{currentUser.first_name}} {{currentUser.last_name}}</v-list-tile-title>
              <v-list-tile-sub-title>{{currentUser.email}}</v-list-tile-sub-title>
            </v-list-tile-content>
          </v-list-tile>
        </v-list>
        <v-divider></v-divider>
        <v-list>
          <v-list-tile @click="viewMyPosts">
            <v-list-tile-content>
              <v-list-tile-title>Meus posts</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
          <v-list-tile @click="logout">
            <v-list-tile-content>
              <v-list-tile-title>Sair</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
        </v-list>
      </v-card>
    </v-menu>
    <login-dialog ref="loginDialog" />
  </v-toolbar>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import loginDialog from "~/components/login-dialog.vue";
import Snacks from "~/helpers/Snacks";
import { AUTH_LOGOUT } from "~/store/actions.type";

export default {
  components: {
    loginDialog
  },
  computed: {
    ...mapGetters(["currentUser"])
  },

  props: ["state"],

  methods: {
    ...mapActions([AUTH_LOGOUT]),

    openLoginDialog() {
      this.$refs.loginDialog.open();
    },

    goToSignUp() {
      this.$router.push({ name: "signup" });
    },

    logout() {
      this[AUTH_LOGOUT]().then(() => this.toIndex());
    },

    toIndex() {
      this.$router.push({ name: "index" });
    },

    viewMyPosts() {
      this.$router.push({ name: "my-posts" });
    }
  }
};
</script>