<template>
  <div id="login">
    <Row type="flex" justify="center">
      <i-col :sm="16" :md="12" :lg="8" :xs="22">
      <Card>
        <p slot="title">
          <Icon slot="prepend" type="log-in"></Icon>
           &nbsp;&nbsp;&nbsp;登录
        </p>
        <Form ref="formData" :model="formData" :rules="ruleFormData">
          <FormItem prop="username">
            <i-input type="text"
                   v-model="formData.username" placeholder="用户名" size="large"
                   @on-enter="handleSubmit('formData', formData)">
              <Icon slot="prepend" type="person"></Icon>
            </i-input>
          </FormItem>
          <FormItem prop="password">
            <i-input type="password"
                   v-model="formData.password" placeholder="密码" size="large"
                   @on-enter="handleSubmit('formData', formData)">
              <Icon slot="prepend" type="locked"></Icon>
            </i-input>
          </FormItem>
          <FormItem prop="remember" label="记住密码">
            <!--todo-->
            <!--我认为这里的label的size是需要修改的-->
            <Row type="flex" justify="start">
              <i-col span="3" >
                <i-switch size="large" v-model="formData.remember">
                  <span slot="open">Yes</span>
                  <span slot="close">No</span>
                </i-switch>
              </i-col>
            </Row>
          </FormItem>
          <FormItem>
            <Button type="info" @click="handleSubmit('formData', formData)" long>登录</Button>
          </FormItem>
        </Form>
      </Card>
      </i-col>
    </Row>
  </div>
</template>
<script>

import ISwitch from '../../node_modules/iview/src/components/switch/switch.vue'
import ICol from '../../node_modules/iview/src/components/grid/col.vue'

export default {
  components: {
    ICol,
    ISwitch},
  name: 'Login',
  data () {
    return {
      formData: {
        username: '',
        password: '',
        remember: false
      },
      ruleFormData: {
        username: [
          {required: true, message: '请填写用户名', trigger: 'blur'}
        ],
        password: [
          {required: true, message: '请填写密码', trigger: 'blur'},
          {type: 'string', min: 4, message: '密码长度不能小于4位', trigger: 'blur'}
        ]
      }
    }
  },
  methods: {
    handleSubmit (name, form) {
      // form中的remember需要经过一下特殊的处理，我好想还不知道该怎么做 todo
      this.$refs[name].validate((valid) => {
        if (valid) {
          this.$axios.defaults.auth = {
            username: form.username,
            password: form.password
          }
          this.$axios.defaults.baseURL = 'http://127.0.0.1:5000'
          // 这里需要是用axios进行一下post
          const msg = this.$Message.loading('I am logging...')
          msg()
          console.log('I am here')
          this.$axios.post('/login', form)
            .then(
              response => {
                console.log(response)
                let data = response.data
                console.log(data)
                this.$Message.success('success login')
              }
            )
            .catch(error => {
              console.log('something wrong')
              if (error === 'Unauthorized Access') {
                this.$Message.error('账户名/密码有误!')
              }
            })
        } else {
          this.$Message.error('invalid form fields')
        }
      })
    }
  }
}

</script>

<style scoped>

</style>
