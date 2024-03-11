import time
from behave import *
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By


@then(u'Click on \'Withdrawal\'')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div[3]/div/ul/li[9]/a').click()


@when(u'Enter Account Number, Amount and Description withdrawl')
def step_impl(context):
    context.driver.find_element(By.NAME, 'accountno').send_keys("132645")
    context.driver.find_element(By.NAME, 'ammount').send_keys("3000")
    context.driver.find_element(By.NAME, 'desc').send_keys("fees")


@then(u'Click on withdrawl Submit button')
def step_impl(context):
    context.driver.find_element(By.NAME, 'AccSubmit').click()
    time.sleep(4)
