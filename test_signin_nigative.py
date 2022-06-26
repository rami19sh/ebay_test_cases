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

class TestNigative():
  def setup_method(self, method):
    chrome_driver_binary = r'.\drivers\chromedriver'
    self.driver=webdriver.Chrome(chrome_driver_binary)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_nigative(self):
    self.driver.get("https://www.ebay.com/")
    self.driver.set_window_size(1552, 840)
    self.driver.find_element(By.LINK_TEXT, "Sign in").click()
    self.driver.find_element(By.ID, "userid").click()
    self.driver.find_element(By.ID, "userid").send_keys("rami-sdsmd@jsdksd.sdsd")
    time.sleep(5)
    self.driver.find_element(By.ID, "signin-continue-btn").click()
    time.sleep(5)
    element = self.driver.find_element(By.ID, "signin-continue-btn")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    #actions.move_to_element(element, 0, 0).perform()
    error_msg=self.driver.find_element(By.CSS_SELECTOR,"#errormsg").text
    time.sleep(5)
    assert "Oops, that's not a match."==error_msg


  def test_nigative2(self):
    self.driver.get("https://www.ebay.com/")
    self.driver.set_window_size(1552, 840)
    self.driver.find_element(By.LINK_TEXT, "Sign in").click()
    self.driver.find_element(By.ID, "userid").click()
    self.driver.find_element(By.ID, "userid").send_keys("rami192.com")
    time.sleep(3)
    self.driver.find_element(By.ID, "signin-continue-btn").click()
    time.sleep(3)
    element = self.driver.find_element(By.ID, "signin-continue-btn")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    #actions.move_to_element(element, 0, 0).perform()
    error_msg=self.driver.find_element(By.CSS_SELECTOR,"#errormsg").text
    time.sleep(3)
    assert "Oops, that's not a match."==error_msg
  
