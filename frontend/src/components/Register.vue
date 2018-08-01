<template>
  <div id="register">
    <Row type="flex" justify="center">
      <i-col :sm="16" :md="16" :lg="16" :xs="22">
      <Card>
        <p slot="title">
          <Icon slot="prepend" type="ios-person-add-outline"></Icon>
          &nbsp;&nbsp;&nbsp;注册
        </p>
        <Form ref="formData" :model="formData" :rules="ruleFormData">
          <FormItem prop="username">
            <i-input type="text"
                   v-model="formData.username" placeholder="用户名" size="large"
                   @on-enter="handleSubmit('formData', formData)">
            <Icon slot="prepend" type="person"></Icon>
            </i-input>
          </FormItem>
          <FormItem prop="email">
            <i-input type="text"
                   v-model="formData.email" placeholder="邮箱" size="large"
                   @on-enter="handleSubmit('formData', formData)">
            <Icon slot="prepend" type="email"></Icon>
            </i-input>
          </FormItem>
          <FormItem prop="password">
            <i-input type="password"
                   v-model="formData.password" placeholder="密码" size="large"
                   @on-enter="handleSubmit('formData', formData)">
            <Icon slot="prepend" type="locked"></Icon>
            </i-input>
          </FormItem>
          <FormItem prop="checkPassword">
            <i-input type="password"
                   v-model="formData.checkPassword" placeholder="确认密码" size="large"
                   @on-enter="handleSubmit('formData', formData)">
            <Icon slot="prepend" type="locked"></Icon>
            </i-input>
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

export default {
  name: 'register',
  data () {
    const validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('Please enter your password'));
      } else {
        if (this.formData.checkPassword !== '') {
          // 对第二个密码框单独验证
          this.$refs.formData.validateField('checkPassword');
        }
        callback();
      }
    }
    const validatePassCheck = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('Please enter your password again'));
      } else if (value !== this.formData.password) {
        callback(new Error('The two input passwords do not match!'));
      } else {
        callback();
      }
    }
    // todo, 邮箱的验证还需要写
    return {
      formData: {
        'username': '',
        'password': '',
        'checkPassword': '',
        'email': ''
      },
      ruleFormData: {
        username: [
          {required: true, message: '请填写用户名', trigger: 'blur'}
        ],
        password: [
          {required: true, validator: validatePass, trigger: 'blur'},
          { type: 'string', min: 4, message: '密码长度不能小于4位', trigger: 'blur' }
        ],
        checkPassword: [
          { validator: validatePassCheck, trigger: 'blur' }
        ]
        // 邮箱的验证
      }
    }
  },
  methods: {
    handleSubmit (name, form) {
      this.$refs[name].validate((valid) => {
        if (valid) {
          // 获取user数据
          let user = {
            username: form.username,
            password: form.password,
            email: form.email
          }

          this.$axios.post('/register', user)
            .then(response => {
              this.$Message.success('注册成功')
              let data = response.data
              this.$Message.success(data.username + '注册成功')
              this.$router.push('/login')
            })
            .catch(() => {
              // 这里的error其实是一个对象, todo,　后面考虑
              this.$Message.error({
                content: '账号已经存在，请换一个用户名或者邮箱，具体信息提示是后期功能',
                duration: 2.5
              })
              this.$refs[name].resetFields()
            })
        } else {
          this.$Message.error('表单验证失败！')
        }
      })
    }
  }
}

</script>

<style scoped>

#register {
  margin-top: 4em;
}

</style>

