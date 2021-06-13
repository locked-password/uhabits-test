from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
from PIL import Image, ImageChops
import unittest

class Uc003 (unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['automationName'] = 'UiAutomator2'
        # desired_caps['platformVersion'] = '10.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'org.isoron.uhabits'
        desired_caps['appActivity'] = 'org.isoron.uhabits.MainActivity'
        desired_caps['fullReset'] = False
        desired_caps['noReset'] = True
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)
        self.actions = TouchAction(self.driver)

    def test_uatc003_add_habit(self):
        self.driver.reset()
        self.driver.find_element_by_id("org.isoron.uhabits:id/next").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/next").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/done").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/actionCreateBooleanHabit").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/tvName").send_keys("")
        self.driver.find_element_by_id("org.isoron.uhabits:id/buttonSave").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/tvName").send_keys("hello")
        self.driver.find_element_by_id("org.isoron.uhabits:id/buttonPickColor").click()
        self.driver.find_element_by_xpath("//android.widget.FrameLayout[@content-desc=\"Color 2\"]/android.widget.ImageView").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/tvDescription").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/tvDescription").send_keys("this is message")
        self.driver.find_element_by_id("org.isoron.uhabits:id/spinner").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[5]").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/tvReminderTime").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/done_button").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/buttonSave").click()

        self.driver.close_app()
        self.driver.launch_app()
        actualVal = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView").text
        assert 'hello' == actualVal
        sleep(5)
    
    def test_uatc004_add_habit(self):
        self.driver.reset()
        self.driver.find_element_by_id("org.isoron.uhabits:id/next").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/next").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/done").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/actionCreateBooleanHabit").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/tvName").send_keys("")
        self.driver.find_element_by_id("org.isoron.uhabits:id/tvDescription").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/tvDescription").send_keys("this is message")
        self.driver.find_element_by_id("org.isoron.uhabits:id/tvReminderTime").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/done_button").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/buttonSave").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/tvName").send_keys("hello")
        self.driver.find_element_by_id("org.isoron.uhabits:id/spinner").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[5]").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/buttonSave").click()
        self.driver.close_app()
        self.driver.launch_app()
        actualVal = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView").text
        assert 'hello' == actualVal
        sleep(5)

    def test_uatc005_add_habit(self):
        self.driver.reset()
        self.driver.find_element_by_id("org.isoron.uhabits:id/next").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/next").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/done").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/actionCreateBooleanHabit").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/tvName").send_keys("hello")
        self.driver.find_element_by_id("org.isoron.uhabits:id/buttonPickColor").click()
        self.driver.find_element_by_xpath("//android.widget.FrameLayout[@content-desc=\"Color 2\"]/android.widget.ImageView").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/buttonSave").click()
 
        self.driver.close_app()
        self.driver.launch_app()
        actualVal = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView").text
        assert 'hello' == actualVal
        sleep(5)

if __name__ == '__main__':
    unittest.main()




