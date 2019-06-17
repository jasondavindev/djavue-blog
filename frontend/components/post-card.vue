<template>
  <v-flex xs12>
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
        <p class="subheading">{{ post.body }}</p>
      </v-card-text>
      <v-card-actions>
        <div class="like-button ma-0">
          <v-btn flat fab color="pink darken-2" @click="like">
            <v-icon>favorite</v-icon>
          </v-btn>
          <span class="body-2 pink--text darken-2">{{ post.likes }}</span>
        </div>
      </v-card-actions>
    </v-card>
  </v-flex>
</template>

<script>
import AppApi from "~apijs";

export default {
  data() {
    return {
      liked: false
    };
  },

  props: ["post"],

  methods: {
    like() {
      if (this.liked) return;
      this.sendLike(this.post.id);
    },

    async sendLike(postId) {
      try {
        const { data } = await AppApi.send_like(postId);
        this.saveLike(data);
      } catch (error) {}
    },

    saveLike(data) {
      if (data.liked) this.increaseLikes();
      this.liked = true;
    },

    increaseLikes() {
      this.post.likes++;
    }
  }
};
</script>
