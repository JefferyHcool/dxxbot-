import pymysql
import json
import traceback

class ConnectDB():
    def __init__(self):
        pass

    def connectTomysql(self):
        self.connect = pymysql.connect(host='1.116.61.49', port=3306, user='DXX', password='HJW123456', db="dxx",
                                  charset='utf8', cursorclass=pymysql.cursors.DictCursor)
        # 在上面host中输入你的IP地址，在password中输入你的数据库密码。
        self.cursor = self.connect.cursor()  # 获取游标
    def read(self):
        self.connectTomysql()
        sql="SELECT * FROM dxx.USERS;"
        self.cursor.execute(sql)
        self.results = self.cursor.fetchall()
        # print(self.results)
        return self.results
    def write(self,QQ_email,stu_id,name):
        s=self.read()
        # print(s)
        re=self.read()
        x=0
        for i in re:
            if i["QQ_email"]==QQ_email:
                x=1
        if x!=1:
            sql="INSERT INTO `dxx`.`USERS` (`QQ_email`, `stu_id`, `name`) VALUES ('{}', '{}', '{}');".format(QQ_email,stu_id,name)
            self.cursor.execute(sql)
            self.connect.commit()
            self.connect.close()
            self.read()


