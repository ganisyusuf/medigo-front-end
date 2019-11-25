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

class Dokter(object):
    def __init__(self, driver):
        self.driver = driver
    def setUp(self):
        self.driver = webdriver.Chrome(path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_tambah_dokter(self):
        driver = self.driver
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Poliklinik'])[1]/following::div[3]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Semua'])[2]/preceding::i[1]").click()
        #nama
        nama = driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Unggah Foto'])[1]/following::input[1]")
        nama.click()
        nama.clear()
        nama.send_keys("Ganis Maulia Yusuf Ganis Maulia Yusuf Ganis Maulia Yusuf Ganis Maulia Yusuf Ganis Maulia Yusuf ")
        nama = nama.get_attribute("value")
        length = int(len(nama))
        if(length <= 50):
                print("Value True for length Nama is {0}, Input: {1}".format(length, nama))
        else:
            print("Value False for length Nama is {0}, Input: {1}".format(length, nama))

        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='M'])[1]/following::input[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='M'])[1]/following::input[1]").clear()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='M'])[1]/following::input[1]").send_keys("23/04/1997")
        driver.find_element_by_xpath('//*[@id="detail-doctor"]/div/div[1]/div/div[2]/div/div[4]/div/div/div[1]/div[1]/div[1]').click()
        driver.find_element_by_xpath('//*[@id="app"]/div[6]/div/div/div[2]/a/div').click()

        #ktp
        ktp = driver.find_element_by_xpath('//*[@id="detail-doctor"]/div/div[1]/div/div[2]/div/div[5]/div/div/div[1]/div/input')
        ktp.send_keys("1234567891012345")
        ktp = ktp.get_attribute("value")
        length = int(len(ktp))

        if(ktp.isdigit() == True):
            if(length == 16):
                print("Value True for length KTP is {0}, Input: {1}".format(length, ktp))
            else:
                print("Value False for length KTP is {0}, Input: {1}".format(length, ktp))

        else:
            print("Value False for KTP checking, Input:  {0}".format(ktp))


        rata2 = driver.find_element_by_xpath('//*[@id="detail-doctor"]/div/div[1]/div/div[2]/div/div[6]/div/div/div[1]/div/input')
        rata2.click()
        rata2.send_keys("60ab")
        rata2 = rata2.get_attribute("value")
        if(rata2.isdigit() == True):
            rata2 = int(rata2)
            if(rata2 <= 600):
                print("Rata-rata konsultasi OK")
            else:
                print("Value False Rata-rata Konsultasi, Input: ",rata2)
        else:
            print("Value False for Rata-rata Konsultasi checking, Input: ",rata2)


        telpon = driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Kontak'])[1]/following::input[1]")
        telpon.click()
        telpon.clear()
        telpon.send_keys("0857324232334234234324344")
        telpon = telpon.get_attribute("value")
        length = int(len(telpon))

        if(length >= 10 and length <= 20):
            print("Value True for length Telepon is {0}, Input: {1}".format(length, telpon))
        else:
            print("Value False for length Telepon is {0}, Input: {1}".format(length, telpon))

       

        email = driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Kontak'])[1]/following::input[2]")
        email.click()
        email.clear()
        email.send_keys("ganisyusuf2397@gmail.com")
        email = email.get_attribute("value")
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if(re.search(regex,email)):  
            print("Valid Email")  
            
        else:  
            print("Invalid Email, Input: ",email)  

        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Spesialisasi'])[1]/following::input[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Gigi Umum (Tambahan)'])[1]/following::i[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Dokter Gigi'])[1]/following::i[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Dokter Umum'])[1]/following::i[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Poliklinik'])[3]/following::input[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Ubah Dokter'])[1]/following::i[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Akupuntur'])[1]/following::i[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Anak'])[1]/following::i[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='kembali'])[1]/following::div[2]").click()
        time.sleep(10)
        # driver.find_element_by_xpath('//*[@id="doctor"]/section/div[1]/div[1]/div/div[2]/div[1]/div[1]/input').click()
        # driver.find_element_by_xpath('//*[@id="doctor"]/section/div[1]/div[1]/div/div[2]/div[1]/div[1]/input').clear()
        # driver.find_element_by_xpath('//*[@id="doctor"]/section/div[1]/div[1]/div/div[2]/div[1]/div[1]/input').send_keys("ganis")
    