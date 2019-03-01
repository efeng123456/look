import os

platformVersion = os.popen('adb shell getprop ro.build.version.release').read()
print platformVersion
print os.popen('adb devices').read().split('\n')[1].split('\t')[0]