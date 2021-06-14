from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import unittest

class Uc011 (unittest.TestCase):
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

    def test_uatc013_edit_habit(self):
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView").click()
        self.driver.find_element_by_accessibility_id("Edit").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/tvName").send_keys("")
        self.driver.find_element_by_id("org.isoron.uhabits:id/buttonPickColor").click()
        self.driver.find_element_by_xpath("//android.widget.FrameLayout[@content-desc=\"Color 2\"]/android.widget.ImageView").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/tvDescription").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/tvDescription").send_keys("this is message")
        self.driver.find_element_by_id("org.isoron.uhabits:id/spinner").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[5]").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/tvReminderTime").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/done_button").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/buttonSave").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/tvName").send_keys("edited hello")
        self.driver.find_element_by_id("org.isoron.uhabits:id/buttonSave").click()
        self.driver.find_element_by_accessibility_id("Navigate up").click()

        actualVal = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView").text
        self.assertEqual('edited hello', actualVal)

    def test_uatc013_edit_habit_ISP(self):
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView").click()
        self.driver.find_element_by_accessibility_id("Edit").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/buttonPickColor").click()
        self.driver.find_element_by_xpath("//android.widget.FrameLayout[@content-desc=\"Color 1\"]/android.widget.ImageView").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/tvDescription").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/tvDescription").send_keys("每次三顆")
        self.driver.find_element_by_id("org.isoron.uhabits:id/tvName").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/tvName").clear()
        self.driver.find_element_by_id("org.isoron.uhabits:id/buttonSave").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/tvName").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/tvName").send_keys("吃藥")
        self.driver.find_element_by_id("org.isoron.uhabits:id/spinner").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[5]").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/denominator").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/denominator").clear()
        self.driver.find_element_by_id("org.isoron.uhabits:id/denominator").send_keys("3")
        self.driver.find_element_by_id("org.isoron.uhabits:id/tvReminderTime").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/done_button").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/tvReminderDays").click()
        self.driver.find_element_by_xpath('//android.widget.CheckedTextView[@text="Saturday"]').click()
        self.driver.find_element_by_xpath('//android.widget.CheckedTextView[@text="Sunday"]').click()
        self.driver.find_element_by_xpath('//android.widget.CheckedTextView[@text="Tuesday"]').click()
        self.driver.find_element_by_xpath('//android.widget.CheckedTextView[@text="Wednesday"]').click()
        self.driver.find_element_by_xpath('//android.widget.CheckedTextView[@text="Thursday"]').click()
        self.driver.find_element_by_xpath('//android.widget.CheckedTextView[@text="Friday"]').click()
        self.driver.find_element_by_id("android:id/button1").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/buttonSave").click()
        self.driver.find_element_by_accessibility_id("Navigate up").click()

        actualVal = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView").text
        self.assertEqual('吃藥', actualVal)
    
    def test_uatc014_edit_habit(self):
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView").click()
        self.driver.find_element_by_accessibility_id("Edit").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/buttonPickColor").click()
        self.driver.find_element_by_xpath("//android.widget.FrameLayout[@content-desc=\"Color 2\"]/android.widget.ImageView").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/spinner").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[5]").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/buttonSave").click()
        
        actualVal = self.driver.find_element_by_id("org.isoron.uhabits:id/frequencyLabel").text
        self.assertEqual('3 times in 7 days', actualVal)

    def test_uatc015_edit_habit(self):
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView").click()
        self.driver.find_element_by_accessibility_id("Edit").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/tvDescription").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/tvDescription").send_keys("this is edited message")
        self.driver.find_element_by_id("org.isoron.uhabits:id/tvReminderTime").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/done_button").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/buttonSave").click()

        messageActualVal = self.driver.find_element_by_id("org.isoron.uhabits:id/questionLabel").text
        reminderActualVal = self.driver.find_element_by_id("org.isoron.uhabits:id/reminderLabel").text
        self.assertEqual('this is edited message', messageActualVal)
        self.assertEqual('08:00', reminderActualVal)

if __name__ == '__main__':
    unittest.main()




