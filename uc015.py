from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import unittest
import pathlib

class Uc015 (unittest.TestCase):
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
        self.prepare_backup_file()

    def prepare_backup_file(self):
        self.driver.find_element_by_id("org.isoron.uhabits:id/next").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/next").click()
        self.driver.find_element_by_id("org.isoron.uhabits:id/done").click()
        
    def scroll_to_bottom(self):
        self.driver.swipe(150, 1000, 150, 100, 500)
        self.driver.swipe(150, 1000, 150, 100, 500)
        self.driver.swipe(150, 1000, 150, 100, 500)

    def test_uatc020_restore_data(self):
        self.driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="More options"]').click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView").click()
        self.scroll_to_bottom()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[4]/android.widget.RelativeLayout").click()
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="Loop Habits Backup.db"]').click()
        restoreMessage = self.driver.find_element_by_id('org.isoron.uhabits:id/snackbar_text').text
        self.assertEqual('Habits imported successfully.', restoreMessage)
        actualVal = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView").text
        self.assertEqual('hello', actualVal)

    def test_uatc021_restore_fail(self):
        self.driver.push_file("/sdcard/Download/loop_habits_backup.db", str(pathlib.Path().absolute()).replace("\\", "/")+"/LoopHabitsBackup.db")
        self.driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="More options"]').click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView").click()
        self.scroll_to_bottom()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[4]/android.widget.RelativeLayout").click()
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="loop_habits_backup.db"]').click()
        restoreMessage = self.driver.find_element_by_id('org.isoron.uhabits:id/snackbar_text').text
        self.assertEqual('File not recognized.', restoreMessage)
        actualVal = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView[2]").text
        self.assertEqual('You have no active habits', actualVal)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()





