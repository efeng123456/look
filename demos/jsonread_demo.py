#_*_coding:utf-8_*_
import json

# test_dict = {'bigberg': [7600, {1: [['iPhone', 6300], ['Bike', 800], ['shirt', 300]]}]}
# print(test_dict)
# print(type(test_dict))
# #dumps 将数据转换成字符串
# json_str = json.dumps(test_dict)
# print(json_str)
# print(type(json_str))

with open("./config.json",'r') as load_f:
    load_dict = json.load(load_f)
    print(load_dict)
#load_dict['smallberg'] = [8200,{1:[['Python',81],['shirt',300]]}]

# with open("../config/record.json","w") as dump_f:
#     json.dump(load_dict,dump_f)