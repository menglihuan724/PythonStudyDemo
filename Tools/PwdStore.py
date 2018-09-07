#coding:utf8

"""
    密码存储工具
"""
import argparse
from prompt_toolkit import prompt
import mysql.connector
from mysql.connector import errorcode


class MyDataSource:
    config = {
        'host': '127.0.0.1',
        'user': 'root',
        'password': '297234',
        'port': 3306,
        'database': 'pwdstore',
        'charset': 'utf8'
    }

    def __init__(self) :
        #数据库初始化
        self.conn=None
        try:
            self.conn =mysql.connector.connect(host='130.24.38.26',user='root',password='297234'
                                          ,database= 'pwdstore',use_unicode=True,charset= "utf8")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
    @property
    def connection(self):
        return self.conn
#插入一条数据
def store(db,name,account,password):

    if not name:
        raise '账号所属不能为空'
    if not account:
        raise '账号不能为空'
    if not password:
        raise '密码不能为空'

    cursor = db.connection().cursor()
    cursor.execute('insert into account (name,account,password) values (%s, %s, %s)'
               , [args.name, args.account, args.password])
    print(f'插入行数{cursor.rowcount}')
    db.connection().commit()
    cursor.close()
#查询全部
def getAll(db):
    cursor = db.connection().cursor()
    cursor.execute('select * from account')
    rows=cursor.fetchall()
    print(f'所有账号为{rows}')
    cursor.close()



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Terry's PWDTool")
    parser.add_argument('-n', metavar='name', dest='name',
                        help='账号所属')
    parser.add_argument('-a', metavar='account', dest='account',
                        help='账号')
    parser.add_argument('-p', metavar='password', dest='password',
                        help='密码')
    args = parser.parse_args()


    #db=MyDataSource()
    #一直监听一个输入
    while True:
        user_input = prompt('>')
        print(user_input)
        print(args)
        #sorted(db,args.name,args.account,args.password)

    # cursor = conn.cursor()
    # cursor.execute('insert into account (name,account,password) values (%s, %s, %s)'
    #            , [args.name, args.account, args.password])
    # print(f'插入行数{cursor.rowcount}')
    # conn.commit()
    # cursor.close()

    # cursor = conn.cursor()
    # cursor.execute('select * from account')
    # rows=cursor.fetchall()
    # print(f'所有账号为{rows}')
    # cursor.close()

    #conn.close()