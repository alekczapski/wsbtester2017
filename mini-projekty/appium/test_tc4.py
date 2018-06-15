"""TC4: Test aplikacji "Contact Manager"

Warunki poczatkowe:
 Aplikacja "Contact Manager" jest zainstalowana

Kroki:
 1. Uruchom aplikacje "Contact Manager"
 2. Kliknij "Add Contact"
 3. Wprowadz "Contact Name" - "Tester WSB"
 4. Wprowadz "Contact Phone" - "+48555666789"
 5. Wprowadz "Contact Email" - "tester@wsb.pll"
 6. Kliknij "Save"

Wynik oczekiwany:
 Aplikacja "Contact Manager" przechodzi do ekranu poczatkowego, kontakt zostal dodany.
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
            "app": path("ContactManager.apk"),
            "appPackage": "com.example.android.contactmanager",
            "appActivity": "com.example.android.contactmanager.ContactManager",
            "unicodeKeyboard": "True",
            "resetKeyboard": "True",
        }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_add_contact(self):
        contact_name = "Tester WSB"
        contact_tel = "+48555666789"
        contact_email = "tester@wsb.pll"

        btn_add_contact = self.driver.find_element_by_accessibility_id("Add Contact")
        btn_add_contact.click()

        textfields = self.driver.find_elements_by_class_name("android.widget.EditText")
        textfields[0].send_keys(contact_name)
        textfields[1].send_keys(contact_tel)
        textfields[2].send_keys(contact_email)

        sleep(2)

        self.assertEqual(textfields[0].text, contact_name)
        self.assertEqual(textfields[1].text, contact_tel)

        btn_save = self.driver.find_element_by_id(
            "com.example.android.contactmanager:id/contactSaveButton"
        )
        btn_save.click()

        testerWSB_on_list = False

        while True:

            contacts = self.driver.find_elements_by_class_name(
                "android.widget.TextView"
            )

            last_contact = contacts[-1].text

            for c in contacts:
                # print(c.text)
                if c.text == contact_name:
                    testerWSB_on_list = True

            if testerWSB_on_list:
                break

            self.driver.swipe(500, 850, 500, 200)

            next_contacts = self.driver.find_elements_by_class_name(
                "android.widget.TextView"
            )

            next_last_contact = next_contacts[-1].text

            if next_last_contact == last_contact:
                break

        self.assertTrue(testerWSB_on_list)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieAplikacji)
    unittest.TextTestRunner(verbosity=2).run(suite)
