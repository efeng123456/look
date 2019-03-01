#coding=utf8
import os,subprocess
import re

import os
platformVersion = os.popen('adb shell getprop ro.build.version.release').read()
print(platformVersion)
devicesname1=os.popen('adb devices').read()
print (devicesname1.split('\n')[1]).split('   ')[0]

print devicesname1.split('\n')[1].split('\t')[0]