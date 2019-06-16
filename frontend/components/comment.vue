<template>
  <v-list-tile avatar>
    <v-list-tile-content>
      <v-list-tile-title>@{{ comment.author.username }}</v-list-tile-title>
      <v-list-tile-sub-title>{{ comment.comment }}</v-list-tile-sub-title>
    </v-list-tile-content>
  </v-list-tile>
</template>

<script>
export default {
  props: ["comment"]
};
</script>

<style>
</style>