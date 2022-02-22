from appium import  webdriver
import time
desired_caps={}

desired_caps['platformName']='Android'
desired_caps['platformVersion']='8.0.0'
desired_caps['deviceName']='RJC5T17620013416'
desired_caps['appPackage']='com.app.meiyuan'  #测试包名 命令：aapt dump badging,在\build-tools\目录下运行
desired_caps['appActivity']='com.app.meiyuan.ui.welcome.SplashActivity'  #android独有launchable-activity:
desired_caps['noReset']='True'
desired_caps['unicodeKeyboard']='True'
desired_caps['resetKeyboard']='True'


print(driver.current_activity)    #打开手机设置
driver.current_activity('com.android.settings/.HWSettings')


#判断这个包是否安装了
# flag=driver.is_app_installed('com.app.meiyuan')
# print('删除前:%s'%flag)
# driver.remove_app('com.app.meiyuan')
#
# flag=driver.is_app_installed('com.app.meiyuan')
# print('删除后:%s'%flag)
#
#
# el1 = driver.find_element_by_id("com.app.meiyuan:id/search_button")
# el1.send_keys("素描")

driver =webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

# driver.close_app()
# time.sleep(2)
# print('app已关闭，准备开启')
# driver.launch_app()
# driver.background_app(2)  #后台启动