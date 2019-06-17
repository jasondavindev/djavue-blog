<template>
  <v-flex xs12>
    <v-card color="white">
      <v-card-text>
        <v-text-field
          v-model="comment"
          ref="comment"
          :rules="[fieldRequired, logged]"
          label="Comentário"
          :counter="400"
          maxlength="400"
          textarea
        ></v-text-field>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          color="primary"
          flat
          @click="submit"
          :loading="commenting"
          :disabled="commenting"
        >Comentar</v-btn>
      </v-card-actions>
    </v-card>
  </v-flex>
</template>

<script>
import AppApi from "~apijs";

export default {
  props: ["postId"],

  data() {
    return {
      comment: null,
      commenting: false
    };
  },

  methods: {
    submit() {
      this.validateForm() && this.sendComment();
    },

    async sendComment() {
      this.commenting = true;

      try {
        const { data } = await AppApi.save_comment({
          comment: this.comment,
          post: this.postId
        });

        this.addComment(data);
      } catch (error) {
      } finally {
        this.commenting = false;
      }
    },

    addComment(comment) {
      this.$emit("add-comment", comment);
    }
  }
};
</script>
