#coding=utf-8

import configparser,importlib,os,sys
from os import path
importlib.reload(sys)

d = path.dirname(__file__)  #返回当前文件所在的目录
parent_path = os.path.dirname(d) #获得d所在的目录,即d的父级目录
# proDir = os.path.split(os.path.realpath(__file__))[0]
cf_env = "env.ini"

proDir = os.path.join(parent_path,"config")
configPath = os.path.join(proDir, cf_env)

class ReadEnv():
    def __init__(self):

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath, encoding='utf-8')

    def get_env(self, name):
        value = self.cf.get("env", name)
        return value

    def set_env(self,name):

        self.cf.set("env", "env", name)

        try:
            with open(configPath, "w+") as f:
                self.cf.write(f)
        except ImportError:
            pass




