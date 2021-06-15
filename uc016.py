from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
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

    def prepare_test_data_for_ISP(self):
        self.driver.find_element_by_id("org.isoron.uhabits:id/next").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/next").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/done").click()

        self.driver.find_element_by_id("org.isoron.uhabits:id/actionCreateBooleanHabit").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/tvName").send_keys("吃藥")
        self.driver.find_element_by_id("org.isoron.uhabits:id/buttonSave").click()
        element = self.driver.find_element_by_xpath('//android.widget.LinearLayout[./android.widget.TextView[@text="吃藥"]]/android.widget.LinearLayout/android.view.View[1]')
        self.actions.long_press(element)
        self.actions.perform()

        self.driver.find_element_by_id("org.isoron.uhabits:id/actionCreateBooleanHabit").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/tvName").send_keys("餵狗")
        self.driver.find_element_by_id("org.isoron.uhabits:id/buttonSave").click()
        element = self.driver.find_element_by_xpath('//android.widget.LinearLayout/android.widget.TextView[@text="餵狗"]')
        self.actions.long_press(element)
        self.actions.perform()
        self.driver.find_element_by_accessibility_id("More options").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout").click()
        

        self.driver.find_element_by_id("org.isoron.uhabits:id/actionCreateBooleanHabit").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/tvName").send_keys("洗澡")
        self.driver.find_element_by_id("org.isoron.uhabits:id/buttonSave").click()
        
        self.driver.find_element_by_id("org.isoron.uhabits:id/actionCreateBooleanHabit").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/tvName").send_keys("運動")
        self.driver.find_element_by_id("org.isoron.uhabits:id/buttonSave").click()
        element = self.driver.find_element_by_xpath('//android.widget.LinearLayout[./android.widget.TextView[@text="運動"]]/android.widget.LinearLayout/android.view.View[1]')
        self.actions.long_press(element)
        self.actions.perform()
        element = self.driver.find_element_by_xpath('//android.widget.LinearLayout/android.widget.TextView[@text="運動"]')
        self.actions.long_press(element)
        self.actions.perform()
        self.driver.find_element_by_accessibility_id("More options").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout").click()
        

    def test_uatc022_filter_habit(self):
        self.prepare_test_data_of_two_habit()
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

    def test_uatc022_filter_habit_ISP(self):
        self.prepare_test_data_for_ISP()
        sleep(1)

        elements = self.driver.find_elements_by_xpath('//android.widget.LinearLayout/android.widget.TextView')
        self.assertEqual('吃藥', elements[0].text)
        self.assertEqual('洗澡', elements[1].text)

        self.driver.find_element_by_accessibility_id("Filter").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.CheckBox").click()
        self.driver.find_element_by_accessibility_id("Filter").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.CheckBox").click()
        
        elements = self.driver.find_elements_by_xpath('//android.widget.LinearLayout/android.widget.TextView')
        self.assertEqual('餵狗', elements[0].text)
        self.assertEqual('洗澡', elements[1].text)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()




