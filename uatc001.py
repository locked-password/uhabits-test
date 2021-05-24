from appium import webdriver
from time import sleep

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
# desired_caps['platformVersion'] = '10.0'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'org.isoron.uhabits'
desired_caps['appActivity'] = 'org.isoron.uhabits.MainActivity'
desired_caps['fullReset'] = False
desired_caps['noReset'] = True
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
driver.implicitly_wait(5)

driver.reset()
driver.find_element_by_id("org.isoron.uhabits:id/next").click()
driver.find_element_by_id("org.isoron.uhabits:id/next").click()
driver.find_element_by_id("org.isoron.uhabits:id/done").click()
driver.find_element_by_id("org.isoron.uhabits:id/actionCreateBooleanHabit").click()
driver.find_element_by_id("org.isoron.uhabits:id/tvName").send_keys("hello")
driver.find_element_by_id("org.isoron.uhabits:id/buttonSave").click()
driver.close_app()
driver.launch_app()
actualVal = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView").text
assert 'hello' == actualVal
sleep(5)