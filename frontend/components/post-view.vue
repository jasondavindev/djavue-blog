<template>
  <v-layout row wrap>
    <!-- Card do post -->
    <post-card v-if="post" :post="post"></post-card>

    <!-- Card para comentar -->
    <act-comment-card v-if="post" @add-comment="addComment" :postId="post.id"></act-comment-card>

    <center-progress :condition="!comments" size="50"></center-progress>

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

export default {
  components: {
    commentList,
    centerProgress,
    postCard,
    actCommentCard
  },

  data() {
    return {
      comments: null,
      post: null
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
