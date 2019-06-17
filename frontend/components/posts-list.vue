<template>
  <v-layout row wrap>
    <ops-card message="Ops! Não encontramos nenhum post :-(" :condition="posts && !posts.length"></ops-card>
    
    <center-progress :condition="!posts" size="60"></center-progress>
    
    <v-flex xs12 md4 lg3 order-md2 v-if="populars && populars.length">
      <most-popular :posts="populars"></most-popular>
    </v-flex>

    <v-flex xs12 md8 lg9 order-md1 class="pa-0">
      <template v-for="post in posts">
        <my-post-card :post="post" :key="post.id"></my-post-card>
      </template>
    </v-flex>
  </v-layout>
</template>

<script>
import AppApi from "~apijs";
import centerProgress from "~/components/center-progress-circular";
import opsCard from "~/components/ops-card";
import mostPopular from "~/components/most-popular";
import myPostCard from "~/components/my-post-card";

export default {
  components: {
    centerProgress,
    opsCard,
    mostPopular,
    myPostCard
  },

  data() {
    return {
      posts: null,
      populars: null,
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
        this.setPopulars();
      } catch (error) {
      } finally {
        this.loading = false;
      }
    },

    setPopulars() {
      this.populars = this.posts
          .filter(post => post.likes > 0)
          .sort((a, b) => b.likes - a.likes)
          .slice(0, 5);
    }
  },
};
</script>
