<template>
  <div>
    <Timeline>
      <TimelineItem v-for="item in posts.posts">
        <!-- 返回的时间就是一个字符串格式如'2018-07-27 22:50:19.920269'-->
        <p class="time">
          {{ item.timestamp.split(' ')[0] }}
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <router-link :to="item.url" class="content">{{ item.title }}</router-link>
        </p>
      </TimelineItem>
    </Timeline>
    <Page 
      :total="posts.count" 
      @on-change='handleChangePage'
      class="page"
      show-total />
  </div>
</template>

<script>
// 这个组件完成度不高，后面应该抽象成home, tag, category中公共的timeline组件
// todo, 暂定计划就是作为tag, 和category的公共组件，home懒得改了
export default {
  name: 'myTimeLine',
  data: function() {	
    return {}
  },
  mounted () {
    this.fetchData()
  },
  methods: {
    fetchData () {

    },

    // 处理页码改变的方法
    handleChangePage (current) {
      // 用不上后端返回的东西next, 和 prev路由了
      const page = current
      this.$axios.get(`/api/posts?page=${page}`)
        .then(
          response => {
            this.posts = response.data
            this.$Message.success(`换到第${page}页成功`)
          }
        )
        .catch(
          () => {
            this.$$Message.error('换页失败，请重试！')
          }
        )
      // this.$router.push('/' + this.posts.next)
    }
  }
}
</script>

<style scoped>
.page {
  margin-bottom: 1em;
  display: flex;
  justify-content: flex-start;
}
.time{
  font-size: 14px;
  display: flex;
  justify-content: flex-start;

}
.content {
  font-size: 16px;
  font-weight: bold;
}
</style>