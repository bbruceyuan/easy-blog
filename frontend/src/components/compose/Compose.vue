<template>
  <div class="compose">
    <Card>
      <p slot="title">写文章</p>
      <Form ref="formData" 
        :model="formData" 
        label-position="right"
        :rules="ruleFormData"
        >
        <FormItem prop="title">
          <Input v-model="formData.title" placeholder="标题"></Input>
        </FormItem>
        <FormItem prop="content">
          <Input v-model="formData.content"
            type="textarea" 
            :autosize="{minRows: 12, maxRows: 50}"
            placeholder="文章内容，支持markdown"></Input>
        </FormItem>
        <FormItem prop="categories">
          <Tag v-for="item in formData.categories" 
            :key="item" :name="item" 
            closable @on-close="handleCloseCategory">
            {{ item }}
          </Tag>
          <Input v-model="categoryName" 
            placeholder="添加类别" 
            size="small"
            clearable
            style="width: 100px"
            @on-enter='handleAddCatogory'
            >
          </Input>
        </FormItem>
        <FormItem prop="tags">
          <Tag v-for="item in formData.tags" 
            :key="item" :name="item" 
            closable @on-close="handleCloseTag">
            {{ item }}
            </Tag>
          <Input v-model="tagName" 
            placeholder="添加标签" 
            size="small"
            clearable
            style="width: 100px"
            @on-enter='handleAddTag'></Input>
        </FormItem>
        <FormItem>
          <Row type='flex' justify='end'>
            <Button @click="handleSubmit('formData', formData)">提交</Button>
          </Row>
        </FormItem>
      </Form>
    </Card>
  </div>
</template>

<script>
export default {
  name: 'compose',
  data: function() {	
    return {
      tagName: '',
      categoryName: '',
      formData: {
        title: '',
        content: '',
        tags: [],
        categories: []
      },
      ruleFormData: {
        title: [{
          required: true, 
          message: '标题不能为空', 
          trigger: 'blur'
        }],
        content: [{
          required: true, 
          message: '文章内容不能为空', 
          trigger: 'blur'
        }]
      }
    }
  },
  methods: {
    handleSubmit (name, data) {
      // 和以前的几乎一样
    this.$refs[name].validate((valid) => {
      if (valid) {
        const formData = data
        this.$axios.post('/api/posts', formData)
          .then(response => {
            // console.log(response.data)
            const post_json = response.data
            // 获取当前post的url地址
            const url = post_json['url']
            const url_arr = url.split('/')
            const uid = url_arr[url_arr.length - 1]
            this.$Message.info('文章发表成功')
            // this.$refs[name].resetFields()
            this.$router.push({ path: `/posts/${uid}` })
          })
          .catch(error => {
            this.$Message.error('发生了一些错误')
          })
      } else {
        this.$Message.error('文章怎么能是空的呢？')
      }
    })
    },

    handleAddCatogory () {
      this.formData.categories.push(this.categoryName)
      this.categoryName = ''
    },

    handleAddTag () {
      this.formData.tags.push(this.tagName)
      this.tagName = ''
    },

    handleCloseTag (event, name) {
      const index = this.formData.tags.indexOf(name)
      this.formData.tags.splice(index, 1)
    },

    handleCloseCategory(event, name) {
      const index = this.formData.categories.indexOf(name)
      this.formData.categories.splice(index, 1)
    }
  }
}
</script>

<style scoped>
.compose {
  margin-top: 2em;
}
</style>