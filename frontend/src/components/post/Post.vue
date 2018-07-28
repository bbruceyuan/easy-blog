<template>
  <div>
    <post-content></post-content>
    <comment-box></comment-box>
  </div>
</template>

<script>

import PostContent from './PostContent.vue'
import CommentBox from './CommentBox.vue'

export default {
  name: 'post',
  data: function() {	
    return {}
  },
  methods: {},
  components: {
    PostContent,
    CommentBox
  }
}
</script>

<style scoped>

</style>