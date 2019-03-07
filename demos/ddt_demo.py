#_*_coding:utf-8_*_
import unittest
from ddt import ddt,data,unpack,file_data
##这个包是解析json的
from ddt_demo.mycode import has_three_elements,is_a_greeting
##单参数
# @ddt
# class DDtdome(unittest.TestCase):
#     @data(1,2,3,4,5,6,7)
#     def test_onePra(self,pras):
#         return pras+1
#         print pras+1
##复杂参数
# @ddt
# class DDtdemo(unittest.TestCase):
#     @data((1,2),(2,3),(3,4))
#     @unpack
#     def test_morepra(self,pra1,pra2):
#         print pra1+pra2
##json参数
@ddt
class FooTestCase(unittest.TestCase):

    @file_data('test_data_dict.json')
    def test_file_data_json_dict(self, value):
        self.assertTrue(has_three_elements(value))

if __name__ == '__main__':
    unittest.main