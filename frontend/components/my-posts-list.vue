<template>
  <v-layout row wrap>
    <ops-card message="Ops! Você não possui posts :-(" :condition="posts && !posts.length"></ops-card>
    <center-progress :condition="!posts" size="60"></center-progress>

    <template v-for="post in posts">
      <v-flex xs12>
        <v-card color="white">
          <v-card-title primary-title>
            <v-flex xs12 class="ma-0 pa-0">
              <p class="display-1">{{ post.title }}</p>
            </v-flex>
            <p class="subheading">{{ post.body | partBody }}</p>
          </v-card-title>
          <v-divider light></v-divider>
          <v-card-actions>
            <v-btn
              flat
              color="primary"
              :to="{ name: 'posts-id', params: { id: post.id }}"
            >Continuar lendo</v-btn>
            <v-spacer></v-spacer>
            <v-icon class="mr-3" color="primary" @click="openDeleteDialog(post.id)">delete</v-icon>
          </v-card-actions>
        </v-card>
      </v-flex>
    </template>
    <delete-post ref="delete_post_dialog" @deleted-post="deletedPost"></delete-post>
  </v-layout>
</template>

<script>
import AppApi from "~apijs";
import centerProgress from "~/components/center-progress-circular";
import deletePost from "~/components/delete-post";
import opsCard from "~/components/ops-card";

export default {
  components: {
    centerProgress,
    deletePost,
    opsCard
  },

  data() {
    return {
      posts: null,
      loading: false
    };
  },

  mounted() {
    this.getPosts();
  },

  methods: {
    async getPosts() {
      this.loading = true;

      try {
        const { data } = await AppApi.get_my_posts();
        this.posts = data.posts.sort((a, b) => b.created - a.created);
      } catch (error) {
      } finally {
        this.loading = false;
      }
    },

    openDeleteDialog(post) {
      this.$refs.delete_post_dialog.setPost(post);
      this.$refs.delete_post_dialog.open();
    },

    deletedPost(postId) {
      this.posts = this.posts.filter(post => post.id !== postId);
    }
  },

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