# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
import time


valid_name = "Al"
valid_surname = "Czz"
valid_telephone = "49551234567"
invalid_email = "aaaca_gmail.pl"
valid_password = "qwerty1"


class WizzairReg(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(20)

    def test_check_reg(self):
        self.driver.get("https://wizzair.com/pl-pl#/")

        login_btn = self.driver.find_element_by_xpath(
            '//button[@data-test="navigation-menu-signin"]'
        )
        login_btn.click()
        reg_btn = self.driver.find_element_by_xpath(
            '//*[@id="login-modal"]/form/div/p/button'
        )
        reg_btn.click()
        name_field = self.driver.find_element_by_xpath(
            '//input[@data-test="registrationmodal-first-name-input"]'
        )
        name_field.send_keys(valid_name)
        surname_field = self.driver.find_element_by_xpath(
            '//input[@data-test="registrationmodal-last-name-input"]'
        )
        surname_field.send_keys(valid_surname)

        gender_switch = self.driver.find_element_by_xpath(
            '//label[@for="register-gender-male"]'
        )
        self.driver.execute_script("arguments[0].click()", gender_switch)

        tel_field = self.driver.find_element_by_xpath(
            '//input[@data-test="booking-register-phone"]'
        )
        tel_field.send_keys(valid_telephone)

        email_field = self.driver.find_element_by_xpath(
            '//input[@data-test="booking-register-email"]'
        )
        email_field.send_keys(invalid_email)

        pass_field = self.driver.find_element_by_xpath(
            '//input[@data-test="booking-register-password"]'
        )
        pass_field.send_keys(valid_password)

        country_field = self.driver.find_element_by_css_selector(
            "input[data-test=booking-register-country]"
        )
        country_field.click()
        country_to_choose = self.driver.find_element_by_xpath(
            '//*[@class="register-form__country-container__locations"]/label[164]'
        )
        country_to_choose.location_once_scrolled_into_view
        country_to_choose.click()

        policy_checkbox = self.driver.find_element_by_xpath(
            '//label[@for="registration-privacy-policy-checkbox"]'
        )
        policy_checkbox.click()

        error_notice = self.driver.find_element_by_css_selector(
            "#regmodal-scroll-hook-4 > div.rf-input__error > span > span"
        )

        self.assertEqual(error_notice.text, u'Nieprawidłowy adres e-mail')

        assert error_notice.is_displayed()

        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
