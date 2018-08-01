## 关于vue的使用笔记
对于vue-cli3.0,如果要打包的话，即npm run build, 那么我们应该讲vue.config.js中的注释去掉，不然会与flask产生矛盾。（这点和cli2.0不一样，所以值得注意，不然会导致包导入出问题), 还有一些别的关于flask的问题就看app包中init文件