from behave import *
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.common.exceptions


@then(u'Click on Edit Account button')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT,'Edit Account').click()
    time.sleep(5)

@when(u'Enter the Account No')
def step_impl(context):
    context.driver.find_element(By.NAME,'accountno').send_keys('132647')


@then(u'Click on edit account submit button')
def step_impl(context):
    context.driver.find_element(By.NAME, 'AccSubmit').click()
    time.sleep(5)

