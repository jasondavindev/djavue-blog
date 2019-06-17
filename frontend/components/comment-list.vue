<template>
  <v-flex class="pa-0" xs12>
    <template v-for="(comment, index) in comments">
      <comment-component :comment="comment" :key="index"></comment-component>
    </template>
  </v-flex>
</template>

<script>
import AppApi from "~apijs";
import commentComponent from "~/components/comment";

export default {
  components: {
    commentComponent
  },

  props: ["comments"],

  data() {
    return {};
  }
};
</script>

<style>
</style>