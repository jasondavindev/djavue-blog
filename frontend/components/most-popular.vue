<template>
  <v-card>
    <v-card-title>
      <p class="title mb-0">Mais populares</p>
    </v-card-title>
    <v-card-text class="pa-0">
      <template v-for="(popular, index) in posts">
        <v-list-tile class="post" :key="popular.id" @click="readPost(popular.id)">
          <p class="body-1 ma-0 mr-2 grey--text">{{index + 1}}</p>
          <p class="body-1 ma-0">{{ popular.title }}</p>
        </v-list-tile>
      </template>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  props: ["posts"],

  methods: {
    readPost(id) {
      this.$router.push({ name: "posts-id", params: { id } });
    }
  }
};
</script>