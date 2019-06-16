<template>
  <v-list two-line subheader class="pb-0">
    <v-subheader>Comentários</v-subheader>
    <template v-for="(comment, index) in comments">
      <comment-component :comment="comment" :key="index"></comment-component>
    </template>
  </v-list>
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