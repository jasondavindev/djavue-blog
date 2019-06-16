<template>
  <v-container fluid grid-list-lg>
    <center-progress :condition="!posts" size="100"></center-progress>

    <v-layout row wrap justify-center v-if="posts && !posts.length">
      <v-flex xs12 md8 lg6>
        <v-card>
          <v-card-text>
            <p class="text-xs-center grey--text subheading">Ops! Você não possúi posts :-(</p>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>

    <v-layout row wrap>
      <template v-for="post in posts">
        <v-flex xs12>
          <v-card color="white">
            <v-card-title primary-title>
              <p class="display-1">{{ post.title }}</p>
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
    </v-layout>
    <delete-post ref="delete_post_dialog" @deleted-post="deletedPost"></delete-post>
  </v-container>
</template>

<script>
import AppApi from "~apijs";
import centerProgress from "~/components/center-progress-circular";
import deletePost from "~/components/delete-post";

export default {
  components: {
    centerProgress,
    deletePost
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
        const { data } = await AppApi.list_posts();
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