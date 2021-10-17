<template>
  <div class="container">
      <div class="title">
          <h2>青年大学习订阅器</h2>
          <i>v0.1</i>
      </div>
      <div class="form">
          <el-input v-model="info.QQ_Email" placeholder="输入QQ"></el-input>
          <el-input v-model="info.name" placeholder="输入姓名(选填)"></el-input>
          <h6>填了会自动打上姓名水印（v0.2中实现）</h6>
          <el-input v-model="info.stu_id" placeholder="输入学号(选填)"></el-input>
          <h6>填了会自动打上学号水印（v0.2中实现）</h6>
          
      </div>
      <div class="confirm">
          <el-button type="primary" @click="subs" >订阅</el-button>
      </div>
      <div class="note">

          <p>如果有不显示图片的情况
              <i>这不是腾讯公司的官方邮件。 为了保护邮箱安全，内容中的图片未被显示。 显示图片 信任此发件人的图片</i>
              点击显示图片
          </p>
      </div>
      <div class="test">
          <el-button type="success" @click="testSend" round>测试发送</el-button>
          <h6>如果能收到邮件就说明成功，不成功加qq:1063474837</h6>
      </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            info:{
                name:'',
                stu_id:"",
                QQ_Email:""
            },
            qq:{
                QQ_Email:""
            }


        }

    },
     methods: {
       subs(){
            if(this.$data.info.QQ_Email){
                axios.post("http://1.116.61.49:3200/subscribe",this.$data.info).then(res=>{
                    console.log(res)
                    this.$data.qq=this.$data.info
                    console.log( "@@",this.$data.qq)
                    if(res.data.code==200){
                        
 
                        alert("订阅成功每周一下午15点发送")
                    }
                })
                .catch(err=>{
                    console.log(err)
                })
            }
            else{
                alert("QQ邮箱必填")
            }
        },
        testSend(){

                 axios.post("http://1.116.61.49:3200/sendtest",this.$data.info).then(res=>{
                console.log(res)
                if(res.data.code==203){
                    alert("发送成功，查看你的QQ邮箱")
                }
             })
            

        }
            
        },
}
</script>

<style >
.container{
    background-color: #A2D2FF;
    width:64.1875rem;
    height: 30.0625rem;
    margin:20px ;
    border-radius: 10px;
    box-shadow: 0 5px 12px 1px rgba(0, 0, 0, 0.1)
}
/* .form{

} */
.form .el-input__inner{
    margin-top:30px ;
    border-radius: 5px;
    width: 15.25rem;
    height: 2.8rem;
}
.form h6{
    margin: 0;
    color: #75787a;
}
.confirm{
    margin-top: 30px;
}
.note{
    padding: 10px;
    font-size: 10px;
    color: rgb(151, 91, 91);
}
.note i{
    color: rgb(0, 0, 0);
}
</style>