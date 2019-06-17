<template>
  <v-flex xs12 v-if="comments && comments.length">
    <v-card color="white">
      <v-card-title class="pb-1">
        <p class="title ma-0">Comentários</p>
      </v-card-title>
      <v-card-text>
        <template v-for="(comment, index) in comments">
          <comment-component :comment="comment" :key="index"></comment-component>
        </template>
      </v-card-text>
    </v-card>
  </v-flex>
</template>

<script>
import AppApi from "~apijs";
import commentComponent from "~/components/comment";

export default {
  components: {
    commentComponent
  },

  props: ["comments"]
};
</script>

<style>
</style>