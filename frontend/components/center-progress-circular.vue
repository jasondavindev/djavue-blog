<template>
  <v-container v-if="!condition">
    <v-layout justify-center>
      <v-progress-circular
        :size="size"
        indeterminate
        color="primary"
      ></v-progress-circular>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  props: ["condition", "size"]
};
</script>