<template>
  <v-layout row wrap>
    <!-- Card mensagem de erro -->
    <ops-card :condition="error" message="Ops! Post não encontrado ;-("></ops-card>

    <!-- Card do post -->
    <post-card v-if="post" :post="post"></post-card>

    <!-- Card para comentar -->
    <act-comment-card v-if="post" @add-comment="addComment" :postId="post.id"></act-comment-card>

    <center-progress :condition="!comments && !error" size="50"></center-progress>

    <!-- Card de comentarios -->
    <comment-list :comments="comments"></comment-list>
  </v-layout>
</template>

<script>
import AppApi from "~apijs";
import commentList from "~/components/comment-list";
import centerProgress from "~/components/center-progress-circular";
import postCard from "~/components/post-card";
import actCommentCard from "~/components/action-comment-card";
import opsCard from "~/components/ops-card";

export default {
  components: {
    commentList,
    centerProgress,
    postCard,
    actCommentCard,
    opsCard
  },

  data() {
    return {
      comments: null,
      post: null,
      error: false
    };
  },

  mounted() {
    this.getPost(this.$route.params.id);
  },

  methods: {
    async getPost(id) {
      try {
        const { data } = await AppApi.list_post(id);
        this.setPost(data);
      } catch (error) {}
    },

    async getComments() {
      try {
        const { data } = await AppApi.list_comments(this.post.id);
        this.sortCommentsByDate(data.comments);
      } catch (error) {}
    },

    setPost({ post }) {
      if (!post) {
        return this.error = true;
      }

      this.post = post;
      this.getComments();
    },

    addComment(comment) {
      this.comments.unshift(comment);
    },

    sortCommentsByDate(comments) {
      this.comments = comments.sort((a, b) => b.created - a.created);
    }
  }
};
</script>
