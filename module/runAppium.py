#_*_coding:utf-8_*_
import os
import time
import platform

pc = platform.system()
print pc
def stop_appium():
    '''关闭appium服务'''
    if pc =='WIN':
        p = os.popen('netstat  -aon|findstr 4723')
        p0 = p.read().strip()
        if p0 != '' and 'LISTENING' in p0:
            p1 = int(p0.split('LISTENING')[1].strip()[0:4])  # 获取进程号
            os.popen('taskkill /F /PID {p1}')  # 结束进程
            print('appium server已结束')
    elif pc == 'Darwin':
        p = os.popen('lsof -i tcp:4723')
        p0 = p.read()
        if p0.strip() != '':
            p1 = int(p0.split('\n')[1].split()[1])  # 获取进程号
            os.popen('kill -9 {p1}')  # 结束进程
            print('appium server已结束')

def start_appium():
    '''开启appium服务'''
    stop_appium()    # 先判断端口是否被占用，如果被占用则关闭该端口号
    # 根据系统，启动对应的服务
    cmd_dict = {
                   'WIN':' start /b appium -a 127.0.0.1 -p 4723 --log xxx.log --local-timezone ',
               'Darwin':'appium -a 127.0.0.1 -p 4723 --log xxx.log --local-timezone  & '
    }
    os.system(cmd_dict[pc])
    time.sleep(3)  # 等待启动完成
    print('appium启动成功')
start_appium()