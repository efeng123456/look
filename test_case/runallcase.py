
#coding:utf-8
import unittest,os,sys,time
import HTMLTestRunner
from Modu.sendmails import sendmails

def data_dirs():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIRS = (
        os.path.join(BASE_DIR,''),
    )
    d=''.join(DATA_DIRS)
    return d

def suite_all():
    dir_case=unittest.defaultTestLoader.discover(
        data_dirs(),
        pattern='test_*.py',
        top_level_dir=None
    )
    return dir_case

def suite_class(file_name):
    dir_case=unittest.defaultTestLoader.discover(
        data_dirs(),
        pattern=file_name,
        top_level_dir=None
    )
    return dir_case


def getNowTime():
    return time.strftime("%Y-%m-%d %H_%M_%S",time.localtime(time.time()))

def runAutomation():
    """
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIRS = (os.path.join(BASE_DIR,'Report'), )
    dir_report =''.join(DATA_DIRS)
    #print dir_report
    curr_time = str(getNowTime())
    os.makedirs(dir_report + "\\" + curr_time)
    #filename = dir_report + "\\" + curr_time + '\\TestReport.html'
    filename = dir_report + "\\" + curr_time + '\\TestReport.html'
   """
    CUR_PATH = r'/Users/fengerqiang/PycharmProjects/rongxuntong/reports'
    def del_file(path):
        ls = os.listdir(path)
        for i in ls:
            c_path = os.path.join(path, i)
            if os.path.isdir(c_path):
                del_file(c_path)
            else:
                os.remove(c_path)

    del_file(CUR_PATH)
    curr_time = str(getNowTime())

    files1 = '..//reports/TestReport'+curr_time+'.html'
    #print filename
    #print "filename : "+filename
    fp=open(files1,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'融讯通UI测试报告',
        description=u'融讯通UI测试报告详细的信息')
    runner.run(suite_all())
    sendmails(files1)
    #runner.run(suite_define())



if __name__=='__main__':
    runAutomation()


    """
    suite=unittest.TestSuite()#测试套件
    suite.addTest(test_meituan_xml.test_meituan('testcase_file_xml'))
    unittest.TextTestRunner(verbosity=2).run(suite)
    """
