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

class Doctor(object):
    def __init__(self, driver):
        self.driver = driver
    def setUp(self):
        self.driver = webdriver.Chrome(path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_tambah_gagal(self):
        driver = self.driver
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='kembali'])[1]/following::div[2]").click()
        print(driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Unggah Foto'])[1]/following::div[9]").text)
        print(driver.find_element_by_xpath('//*[@id="detail-doctor"]/div/div[1]/div/div[2]/div/div[3]/div/div[2]/div/div[2]/div/div/div').text)
        print(driver.find_element_by_xpath('//*[@id="detail-doctor"]/div/div[1]/div/div[2]/div/div[4]/div/div/div[2]/div/div/div').text)
        
        # Test Tambah gagal Input salah
        driver.find_element_by_xpath("(//input[@type='text'])[2]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys("Ganis Ucup Ganis Ucup Ganis Ucup Ganis Ucup Ganis Ucup Ganis Ucup Ganis Ucup Ganis Ucup Ganis Ucup Ganis Ucup Ganis Ucup Ganis Ucup Ganis Ucup Ganis Ucup Ganis Ucup Ganis Ucup")
        driver.find_element_by_xpath("(//input[@type='text'])[3]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='M'])[1]/following::i[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Nama tidak boleh lebih dari 50 karakter'])[1]/following::li[4]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Jan'])[1]/following::div[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='M'])[1]/following::div[11]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='M'])[1]/following::div[47]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Spesialis Kedokteran Okupasi'])[1]/following::div[6]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[5]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[5]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[5]").send_keys("02618856782198763")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='M'])[1]/following::div[40]").click()
        print(driver.find_element_by_xpath('//*[@id="detail-doctor"]/div/div[1]/div/div[2]/div/div[2]/div/div/div[2]/div/div/div').text)

        # Kelebihan input rata2
        driver.find_element_by_xpath("(//input[@type='text'])[6]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[6]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[6]").send_keys("900")
        print(driver.find_element_by_xpath('//*[@id="detail-doctor"]/div/div[1]/div/div[2]/div/div[6]/div/div/div[2]/div/div/div').text)

        # Salah input rata2 
        driver.find_element_by_xpath("(//input[@type='text'])[6]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[6]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[6]").send_keys("asd")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Atur ulang'])[1]/following::div[2]").click()
        print(driver.find_element_by_xpath('//*[@id="detail-doctor"]/div/div[1]/div/div[2]/div/div[6]/div/div/div[2]/div/div/div').text)

        # Salah format email
        driver.find_element_by_xpath("(//input[@type='text'])[8]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[8]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[8]").send_keys("aku")
        print(driver.find_element_by_xpath('//*[@id="detail-doctor"]/div/div[1]/div/div[4]/div/div[2]/div/div/div[2]/div/div/div').text)

        # Salah format telepon
        driver.find_element_by_xpath("(//input[@type='text'])[7]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[7]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[7]").send_keys("123")
        print(driver.find_element_by_xpath('//*[@id="detail-doctor"]/div/div[1]/div/div[4]/div/div[1]/div/div/div[2]/div/div/div').text)

        # Input nomor Hp > 20 karakter
        driver.find_element_by_xpath("(//input[@type='text'])[7]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[7]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[7]").send_keys("98712645126783987612747891")
        print(driver.find_element_by_xpath('//*[@id="detail-doctor"]/div/div[1]/div/div[4]/div/div[1]/div/div/div[2]/div/div/div').text)

    def test_tambah_berhasil(self):
        driver = self.driver
        driver.find_element_by_xpath("(//input[@type='text'])[2]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys("Maulia Yusufs")
        driver.find_element_by_xpath("(//input[@type='text'])[3]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[3]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[3]").send_keys("12/08/1997")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='M'])[1]/following::div[47]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Spesialis Kedokteran Okupasi'])[1]/following::div[6]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[5]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[5]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[5]").send_keys("09876543456789")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='M'])[1]/following::div[40]").click()
        cek = driver.find_elements_by_xpath('//*[@id="app"]/div[2]/nav/div/div[3]/div/div/div/div/div[2]/div/strong')
        if cek:
            print("Daftar berhasil")
        else:
            print("Daftar gagal")
    
    def test_cek(self):
        driver = self.driver
        driver.find_element_by_xpath("(//input[@type='text'])[2]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys("Abdi")
        driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys(Keys.ENTER)
        if(driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Status'])[1]/following::td[1]").text == 'Abdi'):
            print("Data sukses didaftarkan")
        else:
            print("Gagal")
       