import random
import datetime 
import unittest
import HtmlTestRunner
import collections
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from datetime import date, timedelta
import unittest, time, re
from login import * 
from doctor import *
from cuti import *
from libur import *
from manage import *

path = "Lib\chromedriver.exe"
class TestingMedigo(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        chrome_options.add_experimental_option("prefs",prefs)
        self.driver = webdriver.Chrome(path, chrome_options=chrome_options)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(60)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login_success(self):
        driver = self.driver
        url = "https://hc.staging.medigo.id/login"
        driver.get(url)
        login = Login(driver)
        # login.test_login_failed('admintest007g','admintest007h')
        # driver.get(url)
        login.test_login_success('admintest007','admintest007')
        # dokter = Dokter(driver)
        # dokter.test_tambah_dokter()
        driver.get('https://hc.staging.medigo.id/doctor/create')
        doktor = Doctor(driver)
        doktor.test_tambah_gagal()
        driver.get('https://hc.staging.medigo.id/doctor/create')
        doktor.test_tambah_berhasil()
        driver.get('https://hc.staging.medigo.id/doctor/create')
        doktor.test_cek()
        
        url = 'https://hc.staging.medigo.id/schedule/holiday'
        driver.get(url)
        libur = Libur(driver)
        libur.test_liburan_berhasil()
        libur.test_hapus_liburan()
        libur.test_tidak_diisi_liburan()
        
        url = 'https://hc.staging.medigo.id/schedule/leave'
        driver.get(url)
        cuti = Cuti(driver)
        cuti.berhasil_cuti()
        cuti.berhasil_delete()

        url = 'https://hc.staging.medigo.id/schedule/manage'
        driver.get(url)
        manage = Manage(driver)
        manage.test_gagal_kelola()
        driver.get(url)
        manage.berhasil_input()
        driver.get(url)
        manage.berhasil_hapus()

        utl = 'https://hc.staging.medigo.id/schedule/summary'
        driver.get(url)
        jadwal = Jadwal(driver)
        jadwal.kelola_jadwal_negative()
        utl = 'https://hc.staging.medigo.id/schedule/summary'
        driver.get(url)
        jadwal.kelola_cek_dokter()
        utl = 'https://hc.staging.medigo.id/schedule/summary'
        driver.get(url)
        jadwal.kelola_jadwal_berhasil()

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
