<template>
  <v-container grid-list-md>
    <v-layout justify-center>
      <v-flex xs12 sm10 md8 lg6>
        <v-card>
          <v-card-title>Sign Up</v-card-title>
          <v-card-text>
            <v-container fluid>
              <v-text-field ref="username" label="Username" :rules="[fieldRequired]"></v-text-field>
              <v-text-field ref="firtname" label="First name" :rules="[fieldRequired]"></v-text-field>
              <v-text-field ref="lastname" label="Last name" :rules="[fieldRequired]"></v-text-field>
              <v-text-field ref="email" label="E-mail" :rules="[fieldRequired]"></v-text-field>
              <v-text-field
                ref="password"
                label="Password"
                type="password"
                :rules="[fieldRequired]"
              ></v-text-field>
            </v-container>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="primary" flat @click="submit">Sign up</v-btn>
          </v-card-actions>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  methods: {
    submit() {
      console.log(this.validateForm());
    }
  }
};
</script>
