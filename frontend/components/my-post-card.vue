<template>
  <v-flex>
    <v-card color="white">
      <v-card-title primary-title class="pb-0">
        <v-flex xs12 class="ma-0 pa-0">
          <p class="subheading mb-2">
            {{ post.author.first_name }} {{ post.author.last_name }}
            <span
              class="grey--text"
            >@{{ post.author.username }}</span>
          </p>
        </v-flex>
        <p class="display-1">{{ post.title }}</p>
      </v-card-title>
      <v-card-text>
        <p class="subheading">{{ post.body | partBody }}</p>
      </v-card-text>
      <v-divider light></v-divider>
      <v-card-actions>
        <v-btn
          flat
          color="primary"
          :to="{ name: 'posts-id', params: {id: post.id }}"
        >Continuar lendo</v-btn>
      </v-card-actions>
    </v-card>
  </v-flex>
</template>

<script>
export default {
  props: ['post'],

  filters: {
    partBody(value) {
      if (value.length > 300) {
        return `${value.substr(0, 300)}...`;
      }

      return value;
    }
  }
};
</script>
