# _*_ coding:utf-8 _*_
import time
def getNowTime():
    return time.strftime("%Y-%m-%d %H_%M_%S",time.localtime(time.time()))

def readfiles():

    curr_time = str(getNowTime())
    filename = './Tes'+curr_time+'.txt'
    #print filename
    #print "filename : "+filename
    fp=open(filename,'wb')
for i in range(1000):
    readfiles()
    time.sleep(2)