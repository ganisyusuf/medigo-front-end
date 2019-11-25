# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC

import unittest, time, re

class Login(object):
    def __init__(self, driver):
        self.driver = driver
    
    def test_login_success(self,user,passw):
        driver = self.driver
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Masuk'])[2]/following::input[1]").clear()
        username = driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Masuk'])[2]/following::input[1]")
        username.send_keys(user)
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Masuk'])[2]/following::input[2]").clear()
        password = driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Masuk'])[2]/following::input[2]")
        password.send_keys(passw)
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Lupa Password?'])[1]/following::button[1]").click()
        try:
            element = WebDriverWait(driver, 30)
            element.until(EC.presence_of_element_located((By.ID, '__layout')))
            cek = driver.find_elements_by_xpath('//*[@id="app"]/div[2]/nav/div/div[3]/div/div/div/div/div[2]/div/strong')

            if cek :
                print("Login Success")
            else:
                print("Login gagal")
        except TimeoutException:
            print("Timeout, Loading took too much")

    def test_login_failed(self,user,passw):
        driver = self.driver
        username = driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Masuk'])[2]/following::input[1]")
        username.clear()
        username.send_keys(user)
        password = driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Masuk'])[2]/following::input[2]")
        password.clear()
        password.send_keys(passw)
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Lupa Password?'])[1]/following::button[1]").click()
        time.sleep(2)
        cek = driver.find_elements_by_xpath('//*[@id="app"]/div[2]/nav/div/div[3]/div/div/div/div/div[2]/div/strong')

        if cek :
            print("Login Success")
        else:
            print("Login gagal")

       
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
