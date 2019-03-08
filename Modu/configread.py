#_*_coding:utf-8_*_
import json

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
       # print(load_dict)["username"]
        return load_dict["username"],load_dict["password"],load_dict["mailaddress"]
print getconf()[0],getconf()[1],getconf()[2]
