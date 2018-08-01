// Home vue

<template>
  <div>
    <Row type="flex" justify="center">
      <Col :xs='18' :md='18'  offset='2'>
        <h1 class='homeTitle'>Blog Home Page</h1>
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
          class="homeTitle"
          show-total />
      </Col>
    </Row>
  </div>
</template>

<script>

export default {
  name: 'home',
  mounted () {
    // 这里仅仅试一下在mounted 和 created获取数据有什么区别
    this.fetchData()
  },
  data () {
    return {
      testNumber: 0,
      posts: {}
    }
  },
  methods: {
    fetchData () {
      this.$Spin.show()
      this.$axios.get('/api/posts')
        .then(
          response => {
            this.posts = response.data
            this.$Spin.hide()
          }
        )
        .catch(
          () => {
            this.$Spin.hide()
            this.$Message.error('抱歉啊，没能获取到文章信息')
          }
        )
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
.homeTitle {
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

<style>
.ivu-timeline-item {
  padding: 0 0 25px 0;
  line-height: 16px;
}
</style>
