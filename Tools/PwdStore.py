#coding:utf8

"""
    密码存储工具
"""
import argparse
from prompt_toolkit import prompt
import shlex
from prompt_toolkit.contrib.completers import WordCompleter
import mysql.connector
from mysql.connector import errorcode


class MyDataSource:
    config = {
        'host': '127.0.0.1',
        'port': 3306,
        'database': 'pwdstore',
        'charset': 'utf8',
        'use_unicode':True
    }

    def __init__(self) :
        #数据库初始化
        self._conn=None
        try:
            self._conn =mysql.connector.connect(**self.config)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
    @property
    def conn(self):
        return self._conn
#插入一条数据
def store(db,name,account,password):

    if not name:
        raise '账号所属不能为空'
    if not account:
        raise '账号不能为空'
    if not password:
        raise '密码不能为空'

    cursor = db.conn.cursor()
    cursor.execute('insert into account (name,account,password) values (%s, %s, %s)'
               , [name, account, password])
    print(f'插入行数{cursor.rowcount}')
    db.conn.commit()
    cursor.close()
#查询全部
def getAll(db):
    cursor = db.conn.cursor()
    cursor.execute('select * from account')
    rows=cursor.fetchall()
    print(f'所有账号为{rows}')
    cursor.close()
#初始化命令提示
def init_command():
    ShellCompleter = WordCompleter(['-a','-n','-p'],ignore_case=True)
    return ShellCompleter
#获取命令
def tokenize(cmd):
    cmd_list=shlex.split(cmd)
    cmd_map={}
    cmd_length=len(cmd_list)
    start=0
    while start<cmd_length:
        key=cmd_list[start]
        value=cmd_list[start+1]
        cmd_map[key]=value
        start=start+2
    return  cmd_map


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Terry's PWDTool")
    parser.add_argument('-n', metavar='name', dest='name',
                        help='账号所属')
    parser.add_argument('-a', metavar='account', dest='account',
                        help='账号')
    parser.add_argument('-p', metavar='password', dest='password',
                        help='密码')
    args = parser.parse_args()


    db=MyDataSource()
    #监听输入
    while True:
        cmd = prompt('>', completer=init_command())
        if 'exit'==cmd:
            break
        cmd_tokens = tokenize(cmd)
        name=cmd_tokens['-n']
        account=cmd_tokens['-a']
        password=cmd_tokens['-p']
        store(db,name,account,password)
        getAll(db)
    db.conn.close()

