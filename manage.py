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

class Manage(object):
    def __init__(self, driver):
        self.driver = driver
    def setUp(self):
        self.driver = webdriver.Chrome(path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def berhasil_hapus(self):
        driver = self.driver
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Akupuntur'])[3]/following::div[3]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Kembali'])[1]/following::div[1]").click()
        cek = driver.find_elements_by_xpath('//*[@id="app"]/div[2]/nav/div/div[3]/div/div/div/div/div[2]/div/strong')
        if cek :
            print("Data berhasil delete")
        else:
            print("gagal")

    def mencari_nama(self):
        driver = self.driver
        driver.find_element_by_xpath("(//input[@type='text'])[6]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[6]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[6]").send_keys("ACHMAD FAUZI K. Sp.OT	")
        driver.find_element_by_xpath("(//input[@type='text'])[6]").send_keys(Keys.ENTER)
        if(driver.find_element_by_xpath('//*[@id="schedule"]/section/div[3]/div[1]/table/tbody/tr/td[1]').text == 'ACHMAD FAUZI K. Sp.OT	'):
            print("Data ditemukan")
        else:
            print("Data tidak diteukan")
            
    def berhasil_input(self):
        driver = self.driver
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Kelola Jadwal'])[2]/following::div[27]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Bedah Anak'])[1]/following::div[3]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[3]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='ABDUL MUTHOLIB RAMBE, Dr. Sp.A'])[1]/following::div[3]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Batal'])[2]/following::div[1]").click()
        cek = driver.find_elements_by_xpath('//*[@id="app"]/div[2]/nav/div/div[3]/div/div/div/div/div[2]/div/strong')
        if cek :
            print("Data berhasil input")
        else:
            print("gagal")
    
    def test_gagal_kelola(self):
        driver = self.driver
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Kelola Jadwal'])[2]/following::div[27]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Batal'])[2]/following::div[1]").click()
        print(driver.find_element_by_xpath('//*[@id="app"]/div[5]/div/div/div[2]/div[2]/div/div[2]/div/div/div').text)
        print(driver.find_element_by_xpath('//*[@id="app"]/div[5]/div/div/div[2]/div[3]/div/div[2]/div/div/div').text)