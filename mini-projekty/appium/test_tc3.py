"""TC3: Test notyfikacji (powiadomien)

Warunki poczatkowe:
 Aplikacja "API Demos" jest zainstalowana

Kroki:
 1. Uruchom aplikacje "API Demos"
 2. Kliknij "App"
 3. Kliknij "Notification"
 4. Kliknij "IncomingMessage"
 5. Kliknij "SHOW APP NOTIFICATION"
 6. Rozwin powiadomienia

Wynik oczekiwany:
 Jest powiadomienie o tytule "Joe"
"""
import os
import unittest
from appium import webdriver
from time import sleep


def path(p):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), p))


class TestowanieAplikacji(unittest.TestCase):

    def setUp(self):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "6.0",
            "deviceName": "HTC One A9s",
            "app": path("ApiDemos-debug.apk"),
            "appPackage": "io.appium.android.apis",
            "appActivity": "io.appium.android.apis.ApiDemos",
        }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_open_notification_2(self):

        btn_app = self.driver.find_element_by_xpath(
            '//android.widget.TextView[@text="App"]'
        )
        btn_app.click()

        btn_notification = self.driver.find_element_by_xpath(
            '//android.widget.TextView[@text="Notification"]'
        )
        btn_notification.click()

        btn_incomingmessage = self.driver.find_element_by_xpath(
            '//android.widget.TextView[@text="IncomingMessage"]'
        )
        btn_incomingmessage.click()

        sleep(2)

        btn_show_app_notification = self.driver.find_element_by_xpath(
            '//android.widget.Button[@text="Show App Notification"]'
        )
        btn_show_app_notification.click()

        self.driver.open_notifications()

        notifications = self.driver.find_elements_by_class_name(
            "android.widget.TextView"
        )

        title = False

        for notification in notifications:
            if notification.text == "Joe":
                title = True
                notification.click()

        msg = self.driver.find_element_by_id("io.appium.android.apis:id/message")
        print("\nMessage from Joe:\n\n\t", msg.text, "\n")

        sleep(2)

        self.assertTrue(title)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieAplikacji)
    unittest.TextTestRunner(verbosity=2).run(suite)
