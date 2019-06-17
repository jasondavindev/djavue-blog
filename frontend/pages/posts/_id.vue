<template>
  <post-component v-if="post" :post="post"></post-component>
</template>

<script>
import postComponent from "~/components/post";
import AppApi from "~apijs";

export default {
  components: {
    postComponent
  },

  data() {
    return {
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
        this.post = data.post;
      } catch (error) {}
    }
  }
};
</script>

<style>
</style>