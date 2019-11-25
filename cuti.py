# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import unittest, time, re
path = "Lib\chromedriver.exe"

class Cuti(object):
    def __init__(self, driver):
        self.driver = driver
    def setUp(self):
        self.driver = webdriver.Chrome(path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def berhasil_cuti(self):
        driver = self.driver
        driver.get("https://hc.staging.medigo.id/schedule/leave")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Aktif'])[2]/following::div[8]").click()
        driver.find_element_by_xpath("//input[@type='text']").click()
        driver.find_element_by_xpath("//input[@type='text']").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | //input[@type='text'] | ]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Bedah Urologi (Tambahan)'])[1]/following::div[6]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[3]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='M'])[1]/following::div[30]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[4]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[4]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[4]").send_keys("sakit")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Batal'])[1]/following::div[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Kembali'])[1]/following::div[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Kembali'])[1]/following::div[1]").click()
        cek = driver.find_elements_by_xpath('//*[@id="app"]/div[2]/nav/div/div[3]/div/div/div/div/div[2]/div/strong')
        if cek :
            print("Data berhasil input")
        else:
            print("gagal")
    
    def berhasil_delete(self):
        driver = self.driver
        driver.find_element_by_xpath("(//img[contains(@src,'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABIAAAASCAYAAABWzo5XAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAACcSURBVHgB7ZIxDsIwEAR3Tej9hPAyfhBE5TaU7iL/gJfBE9JDfOQkLIpwAQQNgpVOts/r0VlawtCyiesMdoR4PQtwdEB7SmF/z+8sUCbaAlERqEdYZ/lNEAW1rucUqHVte9NfNotNPJTHz0q/O6Swmp3obVVNFK1X7z820R/0jaBq2mI/ZtbPZUkTjUcTiQxb4dR4g7B3knf4HV0ApMcxFTciHWoAAAAASUVORK5CYII=')])[3]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Kembali'])[1]/following::div[1]").click()
        cek = driver.find_elements_by_xpath('//*[@id="app"]/div[2]/nav/div/div[3]/div/div/div/div/div[2]/div/strong')
        if cek :
            print("Data berhasil deleted")
        else:
            print("gagal")