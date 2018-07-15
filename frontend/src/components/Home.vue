// Home vue

<template>
  <div>
      <p>Home page</p>
      <!-- <p>New Test from flask : {{testNumber}}</p>
      <button @click="getTest">New Test</button>
      <Button @click="getTest" type="primary">New Test</Button> -->
      <Row type="flex" justify="start">
        <Col span="8">col-12</Col>
        <Col span="4">
          <Timeline>
            <TimelineItem color="green">
              <p class="time">1976年</p>
              <p class="content">「更大的世界」</p>
              <p class="content">「Vue 与 Flask 
                的最佳哈哈哈哈哈哈哈啊哈和福建大厦附近啊圣诞节水电费卡上就付款实科技副驾驶的发生可到付件凯撒的积分卡水电费是大家发空间践」</p>
              <p class="content">「更大的世界」</p>
              <p class="content">「Vue 与 sFlask 的最佳实践」</p>
              <p class="content">「更大的世界」</p>
              <p class="content">「Vue 与 Flask 的最佳实践」</p>
              <p class="content">「更大的世界」</p>
              <p class="content">「Vue 与 Flask 的最佳实践」</p>
            </TimelineItem>
            <TimelineItem>
              <p class="time">1984年</p>
              <p class="content">「2018 年终总结」</p>
              <p class="content">「更大的世界」</p>
              <p class="content">「Vue 与 Flask 的最佳实践」</p>
              <p class="content">「更大的世界」</p>
              <p class="content">「Vue 与 Flask 的最佳实践」</p>
            </TimelineItem>
            <TimelineItem>
              <p class="time">2007年</p>
              <p class="content">发布 iPhone</p>
            </TimelineItem>
            <TimelineItem>
              <p class="time">2010年</p>
              <p class="content">发布 iPad</p>
            </TimelineItem>
            <TimelineItem>
              <p class="time">2011年10月5日</p>
              <p class="content">史蒂夫·乔布斯去世</p>
            </TimelineItem>
          <Timeline>
        <TimelineItem color="green">发布1.0版本</TimelineItem>
        <TimelineItem color="green">发布2.0版本</TimelineItem>
        <TimelineItem color="red">严重故障</TimelineItem>
        <TimelineItem color="blue">发布3.0版本</TimelineItem>
    </Timeline>
          </Timeline>
        </Col>
      </Row>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'home',
  mounted () {
    console.log(this.testNumber)
    // this.$Spin.show()
    // setTimeout(() => {
    //   this.$Spin.hide()
    // }, 1500)
  },
  data () {
    return {
      testNumber: 0
    }
  },
  methods: {
    getNumberFromBackend () {
      const path = '/api/test'
      axios.get(path)
        .then(response => {
          this.testNumber = response.data.random_number
        })
        .catch(error => {
          console.log(error)
        })
    },
    getTest () {
      this.testNumber = this.getNumberFromBackend()
    },
    created () {
      this.getTest()
    }
  }
}
</script>

<style scoped>
    .time{
        font-size: 20px;
        font-weight: bold;
    }
    .content{
        font-size: 15px;
        padding-left: 5px;
    }
</style>
