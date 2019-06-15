<template>
  <v-footer height="auto" color="primary lighten-1">
    <v-layout justify-center row wrap>
      <v-flex info py-3 text-xs-center white--text xs12>
        &copy;{{ new Date().getFullYear() }} —
        <strong>Djavue</strong>
      </v-flex>
    </v-layout>
  </v-footer>
</template>

<script>
export default {
  props: ["state"]
};
</script>