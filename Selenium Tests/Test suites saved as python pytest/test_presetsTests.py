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

class TestPresetsTests():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_presetTestchangingpresetsactuallychangesstates(self):
    self.driver.get("http://localhost:8080/")
    self.driver.set_window_size(1294, 1400)
    self.driver.find_element(By.CSS_SELECTOR, ".column:nth-child(2) #recent-image").click()
    self.driver.find_element(By.CSS_SELECTOR, ".column:nth-child(3) > a img").click()
    self.driver.find_element(By.CSS_SELECTOR, ".icon").click()
    self.driver.find_element(By.ID, "recent-image").click()
    self.driver.find_element(By.CSS_SELECTOR, ".column:nth-child(3) > a img").click()
  
  def test_presetcreatenewpresetwithcustomname(self):
    self.driver.get("http://localhost:8080/")
    self.driver.set_window_size(1294, 1400)
    self.driver.find_element(By.CSS_SELECTOR, ".column:nth-child(1) > a img").click()
    self.driver.find_element(By.CSS_SELECTOR, "a > .icon").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".column:nth-child(3) img")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".column:nth-child(2) > a img").click()
    self.driver.find_element(By.CSS_SELECTOR, "a > .icon").click()
    self.driver.find_element(By.CSS_SELECTOR, ".column:nth-child(4) > a img").click()
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
    self.driver.find_element(By.XPATH, "//input[@type=\'text\']").click()
    self.driver.find_element(By.ID, "load").click()
    self.driver.find_element(By.CSS_SELECTOR, ".icon").click()
    self.driver.find_element(By.CSS_SELECTOR, ".column:nth-child(3) > a img").click()
    self.driver.find_element(By.CSS_SELECTOR, ".is-success").click()
    self.driver.find_element(By.CSS_SELECTOR, ".farbtastic-overlay").click()
    self.driver.find_element(By.CSS_SELECTOR, ".farbtastic-overlay").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".b-slider-thumb")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".b-slider-thumb")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".b-slider-thumb")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.CSS_SELECTOR, ".b-slider-thumb").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".farbtastic-overlay")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".farbtastic-overlay")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".farbtastic-overlay")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.CSS_SELECTOR, ".farbtastic-overlay").click()
    self.driver.find_element(By.CSS_SELECTOR, ".button:nth-child(5)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".button:nth-child(5)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".button:nth-child(5)").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".button:nth-child(5)")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".icon").click()
    self.driver.find_element(By.ID, "button-text").click()
    self.driver.find_element(By.CSS_SELECTOR, ".input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".input").send_keys("Test Preset")
    self.driver.find_element(By.CSS_SELECTOR, ".is-primary > span").click()
    self.driver.find_element(By.CSS_SELECTOR, ".column:nth-child(4) #recent-image").click()
  
  def test_presetSelectingPresets(self):
    self.driver.get("http://localhost:8080/")
    self.driver.set_window_size(1294, 1400)
    self.driver.find_element(By.ID, "recent-image").click()
    self.driver.find_element(By.CSS_SELECTOR, ".column:nth-child(2) #recent-image").click()
    self.driver.find_element(By.ID, "recent-image").click()
  
