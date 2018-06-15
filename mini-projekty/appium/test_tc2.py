"""TC2: Test notyfikacji (powiadomien)

Warunki poczatkowe:
 Aplikacja "API Demos" jest zainstalowana

Kroki:
 1. Uruchom aplikację "API Demos"
 2. Rozwin powiadomienia

Wynik oczekiwany:
 Jest powiadomienie o tytule "USB debugging connected" z trescia "Touch to disable USB debugging."
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

    def test_open_notification(self):
        self.driver.open_notifications()
        sleep(2)
        elements = self.driver.find_elements_by_class_name("android.widget.TextView")
        title = False
        body = False

        for el in elements:
            if el.text == "USB debugging connected":
                title = True
            elif el.text == "Touch to disable USB debugging.":
                body = True

        self.assertTrue(title)
        self.assertTrue(body)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieAplikacji)
    unittest.TextTestRunner(verbosity=2).run(suite)
