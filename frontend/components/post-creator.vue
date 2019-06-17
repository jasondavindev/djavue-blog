<template>
  <v-flex xs12>
    <v-card color="white pa-3">
      <v-card-title primary-title>
        <p class="title">Criar post</p>
      </v-card-title>
      <v-card-text>
        <v-flex xs12 clas="pa-0">
          <v-text-field
            v-model="title"
            ref="title"
            label="Título"
            :rules="[fieldRequired]"
            maxlength="60"
          ></v-text-field>
          <v-text-field v-model="body" ref="body" label="Texto" :rules="[fieldRequired]" textarea></v-text-field>
        </v-flex>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          flat
          color="primary"
          :loading="creating"
          :disabled="creating"
          @click.stop="submit"
        >Postar</v-btn>
      </v-card-actions>
    </v-card>
  </v-flex>
</template>

<script>
import AppApi from "~apijs";

export default {
  data() {
    return {
      title: null,
      body: null,
      creating: false
    };
  },

  computed: {
    form() {
      return {
        title: this.title,
        body: this.body
      };
    }
  },

  methods: {
    submit() {
      if (!this.validateForm()) return;
      this.submitPost();
    },

    async submitPost() {
      this.creating = true;

      try {
        const { data } = await AppApi.create_post(this.form);
        this.redirectToPost(data.id);
      } catch (error) {
      } finally {
        this.creating = false;
      }
    },

    redirectToPost(id) {
      this.$router.push({ name: "posts-id", params: { id } });
    }
  }
};
</script>

<style>
</style>