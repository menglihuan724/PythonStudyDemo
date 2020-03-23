################################
#!/usr/bin/python3             # ##     ##  #   #       ######### ######## #########
# -*-coding:utf-8-*-           # # #   # #   # #            #     #        #       #
# @By: tiantian520         # #  # #  #    #   ####      #     #        #########
# @Time:　2020/01/04 20:22:18  # #   #   #    #             #     ######## #
################################
 
import socket
import re
import threading
import time
 
lock = threading.Lock()
threads = list()
ports_list = list()
 
 
def judge_hostname_or_ip(target_host):
    """判断输入的是域名还是IP地址"""
    result = re.match(
        r"^(\d|[1-9]\d|1\d\d|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.(\d|[1-9]\d|1\d\d|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\."
        "(\d|[1-9]\d|1\d\d|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.(\d|[1-9]\d|1\d\d|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$",
        target_host)
 
    if result:
        # print(result.group())
        return result.group()
    else:
        try:
            socket.setdefaulttimeout(1)
            IP = socket.gethostbyname(target_host)
            return IP
        except Exception as e:
            print("请正确输入网址或者ip地址...", e)
            exit()
 
 
def parse_port(ports):
    """把连接符-传输过来的值解析为对应的数字   端口范围1-65535"""
    if ports:
        try:
            res = re.match(r'(\d+)-(\d+)', ports)
            if res:
                if int(res.group(2)) > 65535:
                    print("末尾端口输入有误!!....请新输入")
                    exit()
                return range(int(res.group(1)), int(res.group(2)))
        except:
            print("端口解析错误.....请正确输入端口范围")
            exit()
    else:
        return [19, 21, 22, 23, 25, 31, 42, 53, 67, 69, 79, 80, 88, 99, 102, 110, 113, 119, 220, 443]
 
 
def test_port(host, port):
    """测试端口是否开启"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        lock.acquire()   # 加线程锁
        print("{}, {}端口打开".format(host, port))
        ports_list.append(port)
    except:
        lock.acquire()
    finally:
        lock.release()
        s.close()
 
 
def main():
    ip = judge_hostname_or_ip(input("请输入域名或者IP:"))
    l = parse_port(input("请输入端口范围如: 1-1024 [不输入直接回车默认扫描常见端口]:"))
 
    t1 = time.time()
    # 每个套接字的最大超时时间
    socket.setdefaulttimeout(3)
    # 开启线程来测试
    for port in l:
        t = threading.Thread(target=test_port, args=(ip, port))
        threads.append(t)    # 添加到等待线程列表里面
        t.start()
 
    for t in threads:
        t.join()    # 等待线程全部执行完毕
 
    t2 = time.time()
    print("总共耗时:", t2 - t1)
    print("IP:{}, 有{},共{}个端端口打开".format(ip, ports_list, len(ports_list)))
 
 
if __name__ == '__main__':
    main()
