<template>
  <v-layout row justify-center>
    <v-dialog v-model="visible" max-width="290">
      <v-card>
        <v-card-title class="headline">Excluir post</v-card-title>
        <v-card-text>Você tem certeza que deseja remover este post?</v-card-text>
        <v-card-actions v-if="!loading">
          <v-btn color="info" flat="flat" @click.native="close">Cancelar</v-btn>
          <v-spacer></v-spacer>
          <v-btn color="info" flat="flat" @click.native="deletePost">Sim</v-btn>
        </v-card-actions>
        <v-card-actions v-if="loading">
          <center-progress :condition="loading" size="60"></center-progress>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-layout>
</template>

<script>
import AppApi from "~apijs";
import centerProgress from "~/components/center-progress-circular";

export default {
  components: {
    centerProgress
  },

  data() {
    return {
      post: null,
      visible: false,
      loading: false
    };
  },

  methods: {
    setPost(post) {
      this.post = post;
    },

    open() {
      this.visible = true;
    },

    close() {
      this.visible = false;
    },

    async deletePost() {
      const postId = this.post;
      this.loading = true;

      try {
        const { data } = await AppApi.delete_post(postId);
        data.deleted && this.emitDeletedPost(data.post);
      } catch (error) {
      } finally {
        this.loading = false;
      }
    },

    emitDeletedPost(post) {
      this.$emit("deleted-post", post);
      this.close();
    }
  }
};
</script>