"""TC5: Test ustawień WiFi

Warunki początkowe:
 Aplikacja "API Demos" jest zainstalowana

Kroki:
 1. Uruchom aplikację "API Demos"
 2. Kliknij "Preference"
 3. Kliknij "3. Preference dependencies"
 4. Jeżeli checkbox WiFi jest nie zanaczony to zaznacz i przejdź do pkt 5
    Jeżeli checkbox WiFi jest zaznaczony to przejdź do pkt 5
 5. Kliknij "WiFi settings"
 6. Wprowadź hasło "12345"
 7. Kliknij "OK"
 8. Kliknij "Wstecz" (przycisk Android)
 9. Kliknij "3. Preference dependencies".

Wynik oczekiwany:
 Checkbox "WiFi" jest zaznaczony.
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
            "unicodeKeyboard": "True",
            "resetKeyboard": "True",
        }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_pref_wifi(self):

        btn_pref = self.driver.find_element_by_xpath(
            '//android.widget.TextView[@text="Preference"]'
        )
        btn_pref.click()

        sleep(2)

        btn_pref_dep = self.driver.find_element_by_xpath(
            '//android.widget.TextView[@text="3. Preference dependencies"]'
        )
        btn_pref_dep.click()

        sleep(2)

        cb_wifi = self.driver.find_element_by_android_uiautomator(
            "new UiSelector().checkable(true)"
        )

        def cb_wifi_is_checked():
            if "true" in cb_wifi.get_attribute("checked"):
                return True

        if not cb_wifi_is_checked():
            cb_wifi.click()

        btn_wifi_settings = self.driver.find_element_by_xpath(
            '//android.widget.TextView[@text="WiFi settings"]'
        )

        btn_wifi_settings.click()

        txt_wifi_settings = self.driver.find_element_by_id("android:id/edit")

        txt_wifi_settings.send_keys("12345")

        btn_ok = self.driver.find_element_by_id("android:id/button1")

        btn_ok.click()

        self.driver.keyevent(4)

        btn_pref_dep.click()

        self.assertTrue(cb_wifi_is_checked())

        sleep(2)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieAplikacji)
    unittest.TextTestRunner(verbosity=2).run(suite)
