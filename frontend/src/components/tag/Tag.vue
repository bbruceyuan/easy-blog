<template>
  <div class="tagCard">
    <Card 
      class="card" 
      :bordered='false'
      dis-hover
    >
      <p slot="title" style="font-size: 22px; height: 25px;">tags</p>
      
      <Button v-for="item in tags" 
        :key="item" 
        :name="item" 
        shape="circle"
        size="large"
        style="font-size: 20px;"
        v-on:click="handleClick(item)"
      >
        {{ item }}
      </Button>

    </Card>
  </div>
</template>

<script>
export default {
  name: 'tag',
  data: function() {	
    return {
      tags: []
    }
  },
  mounted () {
    this.fetchData()
  },
  methods: {
    fetchData () {
      this.$axios.get('/api/tags')
        .then(
          response => {
            this.tags = response.data
          }
        )
        .catch(
          () => {
            this.$Message.error('获取标签失败')
          }
        )
    },
    //点击标签的时候，就应该获取所有当前标签的所有post
    handleClick (item) {
      this.$Message.info("todo, please wait for completing by author")
    } 
  }
}
</script>

<style scoped>

.tagCard {
  margin-top: 2em;
}

.card {
  font-size: 20px;
}

</style>

<style>
.ivu-card-body {
  padding-top: 3em;
}
.ivu-card-head p, .ivu-card-head-inner {
  height: 25px;
}
</style>
