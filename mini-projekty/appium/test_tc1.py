"""TC1: Test instalacji aplikacji

Warunki poczatkowe:
 Aplikacja "API Demos" jest zainstalowana

Kroki:
 1. Uruchom aplikacje "API Demos"

Wynik oczekiwany:
 Aplikacja "API Demos" jest zainstalowana i uruchamia sie
"""
import os
import unittest
from appium import webdriver


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

    def test_is_app_installed(self):
        self.assertTrue(self.driver.is_app_installed("io.appium.android.apis"))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieAplikacji)
    unittest.TextTestRunner(verbosity=2).run(suite)
