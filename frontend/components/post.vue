<template>
  <div class="post">
    <v-flex xs12>
      <v-card color="white">
        <v-card-title primary-title>
          <div class="post-content">
            <div class="post-description">
              <span class="post-title">{{ post.title }}</span>
              <span class="post-author grey--text lighten-2">@{{ post.author.username }}</span>
            </div>
            <p class="subheading">{{ post.body }}</p>
          </div>
        </v-card-title>
      </v-card>
    </v-flex>

    <v-flex xs12>
      <v-card color="white">
        <v-card-text>
          <v-text-field
            v-model="comment"
            ref="comment"
            :rules="[required, logged]"
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

    <v-flex xs12>
      <v-card color="white">
        <v-card-text>
          <v-progress-circular
            v-if="!comments.length"
            style="display: block; margin: 0 auto;"
            :size="50"
            indeterminate
            color="primary"
          ></v-progress-circular>
          <comment-list v-if="comments.length" :comments="comments"></comment-list>
        </v-card-text>
      </v-card>
    </v-flex>
  </div>
</template>

<script>
import AppApi from "~apijs";
import commentList from "~/components/comment-list";

export default {
  components: {
    commentList
  },

  props: ["post"],

  data() {
    return {
      comment: "",
      comments: [],
      commenting: false,
      formHasError: false
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
    required(value) {
      return !!value || "Preencha este campos";
    },

    logged() {
      return (
        !!this.$store.getters.logged_user ||
        "Você precisa estar logado para fazer um comentário"
      );
    },

    validate() {
      this.formHasError = false;

      Object.keys(this.form).forEach(prop => {
        if (!this.form[prop]) this.formHasError = true;

        this.$refs[prop].validate(true);
      });
    },

    submit() {
      this.validate();
      if (this.formHasError) return;

      this.sendComment();
    },

    async sendComment() {
      this.commenting = true;

      try {
        const { data } = await AppApi.save_comment({ comment: this.comment });
        this.comments.unshift(data);
      } catch (error) {
      } finally {
        this.commenting = false;
      }
    },

    async getComments() {
      try {
        const { data } = await AppApi.list_comments();
        this.comments = data.comments.sort((a, b) => b.created - a.created);
      } catch (error) {}
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