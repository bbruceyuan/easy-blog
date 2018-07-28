<template>
  <div class="commentBox">
    <Row type="flex" justify="center">
      <Col :sm="24" :md="24" :lg="24" :xs="24">
        <Card>
          <p slot="title">
            <Icon type="compose" />
            &nbsp;&nbsp;&nbsp;评论
          </p>
          <Form ref="formData" 
            :model="formData" 
            :rules="ruleFormData" 
            >
            <FormItem prop='comment'>
              <Input v-model="formData.comment" 
                type="textarea"
                :autosize="{minRows: 4, maxRows: 10}"
                @click="handleSubmit('formData', formData)"
                placeholder="请输入你的评论"></Input>
            </FormItem>
            <FormItem>
              <Row type='flex' justify='end'>
                <p style="margin-right: 2em;"><router-link to="/register" style="margin-left: 2em;">注册</router-link></p>
                <Button @click="handleSubmit('formData', formData)">提交</Button>
              </Row>
            </FormItem>
          </Form>
        </Card>
      </Col>
    </Row>
  </div>
</template>

<script>
export default {
  name: 'commentBox',
  data: function() {	
    return {
      formData: {
        comment: ''
      },
      // 前端验证规则
      ruleFormData: {
        comment: [
          {
            required: true, 
            message: '评论不能为空', 
            trigger: 'blur'
          }
        ]
      }
    }
  },
  methods: {
    handleSubmit (name, form) {
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

.commentBox {
  margin-top: 4em;
}

</style>