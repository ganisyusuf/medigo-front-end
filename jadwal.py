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
    
    def kelola_cek_dokter(self):
        driver = self.driver
        driver.find_element_by_xpath("(//input[@type='text'])[6]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[6]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[6]").send_keys("ABDI")
        driver.find_element_by_xpath("(//input[@type='text'])[6]").send_keys(Keys.ENTER)
        if(driver.find_element_by_xpath('//*[@id="schedule"]/section/div[2]/div/div[2]/div/table/tbody/tr/td[1]/div/div/div/div[1]') == 'ABDI'):
            print("Data berhasil ditemukan")
        else:
            print("Data tidak ditemukan")

    def kelola_jadwal_negative(self):
        driver = self.driver
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Jadwal Dokter'])[2]/following::i[5]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Andrologi'])[5]/following::div[3]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='MRN Pasien tidak ditemukan.'])[1]/following::div[15]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Kembali'])[1]/following::button[1]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[6]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[6]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[6]").send_keys("asdaw")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Email harus berupa alamat surel yang benar'])[1]/following::i[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Jaminan'])[1]/following::div[5]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='KTP'])[2]/following::div[10]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[8]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[8]").send_keys("125122331241251212421536712463812467123846123e8r6317864512738182834124312341231")
        print(driver.find_element_by_xpath('//*[@id="doctor"]/div/div[1]/div/section[1]/div[3]/div[2]/div[2]/div/div/div[2]/div/div/div').text)
        print(driver.find_element_by_xpath('//*[@id="doctor"]/div/div[1]/div/section[1]/div[3]/div[2]/div[4]/div/div/div[2]/div/div/div').text)

    def kelola_jadwal_berhasil(self):
        driver = self.driver
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Jadwal Dokter'])[2]/following::i[5]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='-'])[11]/following::div[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='MRN Pasien tidak ditemukan.'])[1]/following::strong[16]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Kembali'])[1]/following::div[1]").click()
        driver.find_element_by_xpath("//input[@type='text']").click()
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("Dicky Ucup")
        driver.find_element_by_xpath("(//input[@type='text'])[2]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys("23/12/1990")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Validasi'])[1]/following::div[4]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Validasi'])[1]/following::div[7]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='KITAS/KITAP'])[1]/following::div[6]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[5]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[5]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[5]").send_keys("08976256622")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Data Kontak'])[1]/following::div[23]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Jaminan'])[1]/following::div[6]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[8]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[8]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[8]").send_keys("3217673627184")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Atur ulang'])[2]/following::div[11]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Gigi Umum (Tambahan)'])[1]/following::div[6]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Batal'])[1]/following::div[2]").click()
        cek = driver.find_elements_by_xpath('//*[@id="app"]/div[2]/nav/div/div[3]/div/div/div/div/div[2]/div/strong')
        if cek :
            print("Data Berhasiil Didaftarkan")
        else:
            print("gagal")