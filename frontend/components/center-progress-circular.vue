<template>
  <v-progress-circular
    v-if="!condition"
    style="display: block; margin: 0 auto;"
    :size="size"
    indeterminate
    color="primary"
  ></v-progress-circular>
</template>

<script>
export default {
  props: ['condition', 'size']
};
</script>