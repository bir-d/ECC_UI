# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestDisplayPageTests():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_displaysplaycontentfromurl(self):
    self.driver.get("http://localhost:8080/")
    self.driver.set_window_size(1294, 1400)
    self.driver.find_element(By.CSS_SELECTOR, ".column:nth-child(4) > a img").click()
    self.driver.find_element(By.CSS_SELECTOR, ".input_fields > #url .input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".input_fields > #url .input").send_keys("http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerEscapes.mp4")
    self.driver.find_element(By.ID, "screen_1").click()
    self.driver.execute_script("window.scrollTo(0,0)")
  
  def test_displaysplayandchangecontentwithfilebrowser(self):
    self.driver.get("http://localhost:8080/")
    self.driver.set_window_size(1294, 1400)
    self.driver.find_element(By.CSS_SELECTOR, ".column:nth-child(4) > a img").click()
    self.driver.find_element(By.XPATH, "//input[@type=\'text\']").click()
    self.driver.find_element(By.XPATH, "//input[@type=\'text\']").send_keys("1")
    self.driver.find_element(By.ID, "load").click()
    self.driver.find_element(By.XPATH, "//input[@type=\'text\']").click()
    self.driver.find_element(By.XPATH, "//input[@type=\'text\']").send_keys("2")
    self.driver.find_element(By.ID, "load").click()
    element = self.driver.find_element(By.ID, "load")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.XPATH, "(//input[@type=\'text\'])[2]").click()
    self.driver.find_element(By.XPATH, "(//input[@type=\'text\'])[2]").send_keys("1")
    self.driver.find_element(By.XPATH, "(//button[@id=\'load\'])[2]").click()
    self.driver.find_element(By.XPATH, "(//input[@type=\'text\'])[2]").click()
    self.driver.find_element(By.XPATH, "(//input[@type=\'text\'])[2]").send_keys("2")
    self.driver.find_element(By.XPATH, "(//button[@id=\'load\'])[2]").click()
    self.driver.find_element(By.ID, "load").click()
  
