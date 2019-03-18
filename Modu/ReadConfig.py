#coding=utf-8

import configparser,importlib,os,sys
from os import path
from Modu.ReadEnv import ReadEnv


d = path.dirname(__file__)  #返回当前文件所在的目录
parent_path = os.path.dirname(d) #获得d所在的目录,即d的父级目录
# proDir = os.path.split(os.path.realpath(__file__))[0]

env = str(ReadEnv().get_env('env'))
if env == 'sit':
    cf_env = "cf-sit.ini"
elif env == 'test1' or env == 'fat':
    cf_env = "cf-fat.ini"
else:
    cf_env = "cf-uat.ini"

proDir = os.path.join(parent_path,'config')
configPath = os.path.join(proDir, cf_env)

class ReadConfig():
    def __init__(self):

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath,encoding='utf-8')

    def get_user(self, name):
        value = self.cf.get("user", name)
        return value


    def get_email(self, name):
        value = self.cf.get("email", name)
        return value

    def get_sqldb(self, name):
        value = self.cf.get("SqlServserDatabase", name)
        return value

    def get_mysqldb(self, name):
        value = self.cf.get("mySqlDatabase", name)
        return value


