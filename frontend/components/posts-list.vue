<template>
  <v-container fluid grid-list-lg>
    <v-layout row wrap justify-center v-if="posts && !posts.length">
      <v-flex xs12 md8 lg6>
        <v-card>
          <v-card-text>
            <p class="text-xs-center grey--text subheading mb-0">Ops! Não encontramos nenhum post :-(</p>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>

    <v-layout row wrap>
      <center-progress :condition="!posts" size="60"></center-progress>
      <template v-for="post in posts">
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
        this.posts = data.posts.sort((a, b) => b.created - a.created);
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
