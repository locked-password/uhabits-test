from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import unittest

class Uc010 (unittest.TestCase):
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
        self.prepare_test_data_of_one_habit()

    def prepare_test_data_of_one_habit(self):
        self.driver.find_element_by_id("org.isoron.uhabits:id/next").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/next").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/done").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/actionCreateBooleanHabit").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/tvName").send_keys("hello")
        self.driver.find_element_by_id("org.isoron.uhabits:id/buttonSave").click()

    def habit_detail_scroll_to_bottom(self):
        self.driver.swipe(150, 1000, 150, 100, 1000)
        self.driver.swipe(150, 1000, 150, 100, 1000)

    def test_uatc012_record_habits_of_days_ago_calendar(self):
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView").click()
        self.habit_detail_scroll_to_bottom()
        self.driver.find_element_by_id("org.isoron.uhabits:id/edit").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/parentPanel")
        self.actions.tap(x=218, y=911).perform()
        self.actions.tap(x=218, y=911).perform()
        self.actions.tap(x=213, y=1013).perform()
        self.driver.find_element_by_id("android:id/button1").click()
        # TODO assert

if __name__ == '__main__':
    unittest.main()




