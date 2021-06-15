from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import unittest

class Uc002 (unittest.TestCase):
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

    def test_uatc002_record_habit(self):
        self.driver.reset()
        self.driver.find_element_by_id("org.isoron.uhabits:id/next").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/next").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/done").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/actionCreateBooleanHabit").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/tvName").send_keys("hello")
        self.driver.find_element_by_id("org.isoron.uhabits:id/buttonSave").click()
        self.driver.close_app()
        self.driver.launch_app()
        incorrectDate = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.View[1]")
        correctDate = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.View[2]")

        self.actions.long_press(incorrectDate)
        self.actions.perform()

        self.actions.long_press(incorrectDate)
        self.actions.perform()
        self.actions.long_press(correctDate)
        self.actions.perform()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()