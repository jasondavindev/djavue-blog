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
          <v-text-field name="input-1" label="Comentário" textarea></v-text-field>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" flat @click="comment">Comentar</v-btn>
        </v-card-actions>
      </v-card>
    </v-flex>
  </div>
</template>

<script>
export default {
  props: ["post"],

  methods: {
    comment() {}
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