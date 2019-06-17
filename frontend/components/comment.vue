<template>
  <v-flex class="pl-0 pr-0 pt-3 pb-3">
    <p class="title mb-2">
      {{ comment.author.first_name }} {{ comment.author.last_name }}
      <span
        class="grey--text"
      >@{{ comment.author.username }}</span>
    </p>
    <p class="body-1 mb-1">{{ comment.comment }}</p>
  </v-flex>
</template>

<script>
export default {
  props: ["comment"]
};
</script>

<style>
</style>