<template>
  <v-layout row wrap>
    <v-flex xs12>
      <v-card color="white" width="100%">
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

    <v-flex xs12>
      <v-card color="white">
        <v-card-text>
          <v-text-field
            v-model="comment"
            ref="comment"
            :rules="[fieldRequired, logged]"
            label="Comentário"
            :counter="400"
            maxlength="400"
            textarea
          ></v-text-field>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            flat
            @click="submit"
            :loading="commenting"
            :disabled="commenting"
          >Comentar</v-btn>
        </v-card-actions>
      </v-card>
    </v-flex>

    <center-progress :condition="!comments" size="50"></center-progress>

    <v-flex xs12 v-if="comments && comments.length">
      <v-card color="white">
        <v-card-title class="pb-1">
          <p class="title ma-0">Comentários</p>
        </v-card-title>
        <v-card-text>
          <comment-list :comments="comments"></comment-list>
        </v-card-text>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
import AppApi from "~apijs";
import commentList from "~/components/comment-list";
import centerProgress from "~/components/center-progress-circular";

export default {
  components: {
    commentList,
    centerProgress
  },

  props: ["post"],

  data() {
    return {
      comment: "",
      comments: null,
      commenting: false,
      liked: false
    };
  },

  mounted() {
    this.getComments();
  },

  computed: {
    form() {
      return {
        comment: this.comment
      };
    }
  },

  methods: {
    submit() {
      if (!this.validateForm()) return;

      this.sendComment();
    },

    async sendComment() {
      this.commenting = true;

      try {
        const { data } = await AppApi.save_comment({
          comment: this.comment,
          post: this.post.id
        });
        this.comments.unshift(data);
      } catch (error) {
      } finally {
        this.commenting = false;
      }
    },

    async getComments() {
      try {
        const { data } = await AppApi.list_comments(this.post.id);
        this.comments = data.comments.sort((a, b) => b.created - a.created);
      } catch (error) {}
    },

    async like() {
      if (this.liked) return;

      try {
        const { data } = await AppApi.send_like(this.post.id);

        if (data.liked) this.post.likes++;
        this.liked = true;
      } catch (error) {}
    }
  }
};
</script>
