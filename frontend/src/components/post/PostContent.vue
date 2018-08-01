<template>
  <div>
    <Card>
      <p slot="title">{{ postData.title }}</p>
      <div class="postContent">
        <p v-html="postData.body_html" ></p>
      </div>
      <Tag v-for="item in postData.tags" 
        :key="item" 
        :name="item" 
        size="small"
        type="border"
      >
        {{ item }}
      </Tag>
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
      postData: ''
    }
  },
  mounted () {
    this.fetchData()
  },
  methods: {
    fetchData () {
      // 显示一个加载界面
      // this.$Spin.show()
      // 根据此时的param中的pid决定
      let url = this.$route.path
      // console.log(url)
      this.$axios.get(url)
        .then(
          response => {
            // console.log(response.data)
            this.postData = response.data
            // this.$Spin.hide()
          }
        )
        .catch(() => {
          // 只要有错，就返回到主界面
          this.$router.push('/')
          this.$Message.error('请求文章内容失败')
        })
    }
  }
}
</script>

<style>

.postContent {
  text-align: left;
  line-height: 2em;
  margin-bottom: 2em;
  text-indent: 2em;
}
.postContent p, div, pre, ul, code, blockquote{
  margin-bottom: 1.5em;
}
.postContent  h1, h2, h3, h4 {
  margin-bottom: 0.5em;
}
</style>

<style scoped>
.ivu-card {
  font-size: 16px;
}
.ivu-card-head p, .ivu-card-head-inner {
  font-size: 18px;
  height: 25px;
}
</style>
