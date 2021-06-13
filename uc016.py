from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
from PIL import Image, ImageChops
import unittest

class Uc016 (unittest.TestCase):
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
        self.driver.reset()
        self.prepare_test_data_of_two_habit()

    def prepare_test_data_of_two_habit(self):
        self.driver.find_element_by_id("org.isoron.uhabits:id/next").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/next").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/done").click()

        self.driver.find_element_by_id("org.isoron.uhabits:id/actionCreateBooleanHabit").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/tvName").send_keys("hello 1 will archive")
        self.driver.find_element_by_id("org.isoron.uhabits:id/buttonSave").click()

        self.driver.find_element_by_id("org.isoron.uhabits:id/actionCreateBooleanHabit").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/tvName").send_keys("hello 2")
        self.driver.find_element_by_id("org.isoron.uhabits:id/buttonSave").click()

    def test_uatc022_filter_habit(self):
        willArchiveHabit = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView")
        self.actions.long_press(willArchiveHabit)
        self.actions.perform()
        sleep(1)
        self.driver.find_element_by_accessibility_id("More options").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout").click()
        self.driver.find_element_by_accessibility_id("Filter").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.CheckBox").click()

        actualVal = willArchiveHabit.text
        self.assertEqual('hello 1 will archive', actualVal)
        sleep(5)
    
if __name__ == '__main__':
    unittest.main()




