from appium import  webdriver

desired_caps={}

desired_caps['platformName']='Android'
desired_caps['platformVersion']='8.0.0'
desired_caps['deviceName']='RJC5T17620013416'
desired_caps['appPackage']='com.app.meiyuan'  #测试包名 命令：aapt dump badging,在\build-tools\目录下运行
desired_caps['appActivity']='com.app.meiyuan.ui.welcome.SplashActivity'  #android独有launchable-activity:
desired_caps['noReset']='True'
desired_caps['unicodeKeyboard']='True'
desired_caps['resetKeyboard']='True'

driver =webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
