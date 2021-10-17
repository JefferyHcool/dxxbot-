from datetime import timedelta

import flask
# from flask_cors import *
import connectDB
from flask import Flask, request, jsonify, session, Response,Config,make_response
import sendEmail
from flask_cors import *
import json
app = Flask(__name__)
db=connectDB.ConnectDB()
CORS(app, supports_credentials=True)
@app.route("/subscribe",methods=['POST'])
def sub():
        re = request.get_json()
        qq=re["QQ_Email"]
        name=re["name"]
        stu_id=re["stu_id"]
        db.write(qq,stu_id,name)
        print('''{:=^18}\n邮箱：{}\n姓名：{}\n学号：{}'''.format("新用户订阅",qq,name,stu_id))

        return jsonify(msg='订阅成功',code=200)
@app.route("/send",methods=['GET'])
def send():
        sm=sendEmail.sendEmail()
        sm.send()
        return jsonify(msg="发送成功",code=201)
@app.route("/sendtest",methods=['POST'])
def sendtest():
        re = request.get_json()
        print(re)
        qq = re["QQ_Email"]
        sm=sendEmail.sendEmail()
        sm.testsend(qq)
        print("发送成功QQ是{}".format(qq))
        return jsonify(msg="发送成功",code=203)
@app.route("/setSend",methods=['POST'])
def setSend():
        re=request.get_json()
        add=re["QQ_Email"]
        subject=re['subject']
        content=re["Content"]
        sm=sendEmail.sendEmail()
        sm.setSend(add,subject=subject,contents=content)
        return jsonify(code=204,meg="发送自定义消息成功")
if __name__ == '__main__':
    app.run(host="0.0.0.0", port="3200", debug=True)
