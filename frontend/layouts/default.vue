<template>
  <v-app id="inspire">
    <toolbar :state="layout" />
    <v-content class="grey lighten-3">
      <v-container fluid grid-list-lg>
        <nuxt></nuxt>
      </v-container>
    </v-content>
    <le-footer />
    <v-snackbar :timeout="snack.timeout" :color="snack.color" bottom v-model="snack.visible">
      {{snack.text}}
      <v-btn dark flat @click.native="snack.visible = false">Close</v-btn>
    </v-snackbar>
  </v-app>
</template>

<script>
import { mapGetters } from "vuex";
import toolbar from "~/components/toolbar.vue";
import footer from "~/components/footer.vue";
export default {
  components: {
    toolbar,
    leFooter: footer
  },
  data: () => ({
    layout: {
      drawer: true
    }
  }),
  computed: {
    ...mapGetters(["snack"])
  }
};
</script>