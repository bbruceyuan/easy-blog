<template>
  <div>
    <Card class="postContent">
      <p>
        我不知道这是什么东西
      </p>
      我不知道这是什么东西
      我不知道这是什么东西
      我不知道这是什么东西
      我不知道这是什么东西
      我不知道这是什么东西
      我不知道这是什么东西

    <p>{{ body }}</p>
    </Card>
  </div>
</template>

<script>
export default {
  // 名字不能和iview中有的冲突了，
  // 所以一开始起名content无效
  name: 'postContent',
  data: function() {	
    return {
      body: ''
    }
  },
  created () {
    this.fetchData()
  },
  methods: {
    fetchData () {
      // 显示一个加载界面
      this.$Spin.show()
      // 根据此时的param中的pid决定
      let url = this.$router.path
      this.$axios.get(url)
        .then(
          response => {
            this.body = response.data
            this.$Spin.hide()
          }
        )
        .catch(error => {
          // 只要有错，就返回到主界面
          this.$router.push('/')
          this.$Message.error('请求文章内容失败')
        })
    }
  }
}
</script>

<style scoped>

.postContent {
  display: flex;
  justify-content: left; 
  text-align: left;
}

</style>