from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
from PIL import Image, ImageChops
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
        sleep(1)
        self.driver.find_element_by_id("org.isoron.uhabits:id/next").click()
        sleep(1)
        self.driver.find_element_by_id("org.isoron.uhabits:id/done").click()
        sleep(1)
        self.driver.find_element_by_id("org.isoron.uhabits:id/actionCreateBooleanHabit").click()
        sleep(1)
        self.driver.find_element_by_id("org.isoron.uhabits:id/tvName").send_keys("hello")
        sleep(1)
        self.driver.find_element_by_id("org.isoron.uhabits:id/buttonSave").click()
        sleep(1)
        self.driver.close_app()
        sleep(1)
        self.driver.launch_app()
        sleep(1)
        incorrectDate = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.View[1]")
        sleep(1)
        correctDate = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.View[2]")
        sleep(1)

        self.actions.long_press(incorrectDate)
        self.actions.perform()
        sleep(1)

        self.actions.long_press(incorrectDate)
        self.actions.perform()
        sleep(1)
        self.actions.long_press(correctDate)
        self.actions.perform()
        sleep(1)

        incorrectDate.screenshot("./uatc002/incorrectDate.png")
        correctDate.screenshot("./uatc002/correctDate.png")

        assert ImageChops.difference(Image.open("./uatc002/correctDate.png"), Image.open("./uatc002/expected_explicit_check.png")).getbbox() is None
        # assert ImageChops.difference(Image.open("./incorrectDate.png"), Image.open("./expected_unchecked.png")).getbbox() is None
        assert ImageChops.difference(Image.open("./uatc002/correctDate.png"), Image.open("./uatc002/expected_unchecked.png")).getbbox() is None

        # print(incorrectDate.get_attribute("className"))
        # print(incorrectDate.get_attribute("checked"))
        # print(incorrectDate.get_attribute("contentDescription"))
        # print(incorrectDate.get_attribute("resourceId"))
        # print(incorrectDate.get_attribute("selected"))
        # print(incorrectDate.get_attribute("text"))

        # print("-----------------------------")

        # print(correctDate.get_attribute("className"))
        # print(correctDate.get_attribute("checked"))
        # print(correctDate.get_attribute("contentDescription"))
        # print(correctDate.get_attribute("resourceId"))
        # print(correctDate.get_attribute("selected"))
        # print(correctDate.get_attribute("text"))

        # actualVal = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView").text
        # assert 'hello' == actualVal
        sleep(5)

if __name__ == '__main__':
    unittest.main()