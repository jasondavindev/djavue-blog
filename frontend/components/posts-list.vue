<template>
  <v-container fluid grid-list-lg>
    <v-layout row wrap>
      <center-progress :condition="posts" size="100"></center-progress>
      <template v-for="post in posts">
        <v-flex xs12>
          <v-card color="white">
            <v-card-title primary-title>
              <div class="post-content">
                <div class="post-description">
                  <span class="post-title">{{ post.title }}</span>
                  <span class="post-author grey--text lighten-2">@{{ post.author.username }}</span>
                </div>
                <p class="subheading">{{ post.body | partBody }}</p>
              </div>
            </v-card-title>
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
    </v-layout>
  </v-container>
</template>

<script>
import AppApi from "~apijs";
import centerProgress from "~/components/center-progress-circular";

export default {
  components: {
    centerProgress
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
        this.posts = data.posts;
      } catch (error) {
      } finally {
        this.loading = false;
      }
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

<style>
.post-description {
  margin-bottom: 10px;
  line-height: 32px;
  display: inline-flex;
}
.post-description .post-title {
  font-size: 32px;
  font-weight: bold;
}
.post-description .post-author {
  font-size: 24px;
  margin-left: 5px;
}
</style>