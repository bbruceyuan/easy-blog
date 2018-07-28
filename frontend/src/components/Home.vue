// Home vue

<template>
  <div>
      <p style="margin: 2em 0;">Blog Home Page</p>
      <Row type="flex" justify="center">
        <Col :xs='18' :md='18'>
          <Timeline>
            <TimelineItem v-for="item in posts.posts">
              <!-- 返回的时间就是一个字符串格式如'2018-07-27 22:50:19.920269'-->
              <p class="time">{{ item.timestap.split(' ') }}</p>
              <p class="content"><router-link :to="item.url">{{ item.title }}</router-link></p>
            </TimelineItem>
          </Timeline>
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
      this.$axios.get('/posts')
        .then(
          response => {
            this.posts = response.data
            this.$Spin.hide()
          }
        )
        .catch(
          err => {
            this.$Spin.hide()
            this.$Message.error('抱歉啊，没能获取到文章信息')
          }
        )
    }
  }
}
</script>

<style scoped>
    .time{
        font-size: 20px;
        font-weight: bold;
        display: flex;
        justify-content: flex-start;
    }
    .content{
        font-size: 15px;
        padding-left: 2em;
        display: flex;
        justify-content: flex-start;
    }
</style>