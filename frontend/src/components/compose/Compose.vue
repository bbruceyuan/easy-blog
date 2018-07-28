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
      formData: {
        title: '',
        content: ''
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
        // 这里需要把Formdata处理一下，因为这里只有表单的内容
        // 所以我们还需要加上user，评论时间之类的
        this.$Message.info('这个功能暂时还没加上，敬请期待')
        this.$refs[name].resetFields()
      } else {
        this.$Message.error('评论框不能为空')
      }
    })
    }
  }
}
</script>

<style scoped>
.compose {
  margin-top: 2em;
}
</style>