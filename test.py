from appium import webdriver
from time import sleep

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10.0'
desired_caps['deviceName'] = 'Nexus 4 API 29'
desired_caps['appPackage'] = 'org.isoron.uhabits'
desired_caps['appActivity'] = 'org.isoron.uhabits.MainActivity'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
driver.implicitly_wait(5)
driver.find_element_by_id("org.isoron.uhabits:id/next").click()
driver.find_element_by_id("org.isoron.uhabits:id/next").click()
driver.find_element_by_id("org.isoron.uhabits:id/done").click()
driver.find_element_by_id("org.isoron.uhabits:id/actionCreateBooleanHabit").click()
driver.find_element_by_id("org.isoron.uhabits:id/tvName").send_keys("hello")
driver.find_element_by_id("org.isoron.uhabits:id/buttonSave").click()



sleep(5)