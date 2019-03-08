# _*_ coding:utf-8 _*_
import time
import json
def getNowTime():
    return time.strftime("%Y-%m-%d %H_%M_%S",time.localtime(time.time()))

# def readfiles():
#
#     curr_time = str(getNowTime())
#     filename = './Tes'+curr_time+'.txt'
#     print filename
#     print "filename : "+filename
#     fp=open('','r+')
# readfiles()
# # for i in range(1000):
# #     readfiles()
# #     time.sleep(2)
# def readfiles():
#     f = open('..//conf/conf.txt','r')
#     print type(f)
#     print  f.read()
#     # print 1111111
#     a = f.readlines()
#     print type(a)
#     # for i in range(len(f.readlines())):
#     #     print f.readlines()[i]
#     f.close()
# readfiles()


# test_dict = {'bigberg': [7600, {1: [['iPhone', 6300], ['Bike', 800], ['shirt', 300]]}]}
# print(test_dict)
# print(type(test_dict))
# #dumps 将数据转换成字符串
# json_str = json.dumps(test_dict)
# print(json_str)
# print(type(json_str))
def getconf():
    with open("..//conf/config.json",'r') as load_f:
        load_dict = json.load(load_f)
        print(load_dict)["username"]

