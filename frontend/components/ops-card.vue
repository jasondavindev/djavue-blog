<template>
  <v-flex xs12 md8 lg6 offset-md2 offset-lg3 v-if="condition">
    <v-card>
      <v-card-text>
        <p class="text-xs-center grey--text subheading mb-0">{{ message }}</p>
      </v-card-text>
    </v-card>
  </v-flex>
</template>

<script>
export default {
  props: ["message", "condition"]
};
</script>
