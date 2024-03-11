from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import *
import selenium.common.exceptions
import time
# from NewCustomer import customerid


@when(u'Click on Edit customer')
def step_impl(context):
    context.driver.find_element(By.PARTIAL_LINK_TEXT, 'Edit Customer').click()
    time.sleep(5)


@then(u'verify Edit customer')
def step_impl(context):
    print("verify Edit customer")
    time.sleep(5)


@then(u'Fill details to edit')
def step_impl(context):
    # context.driver.find_element(By.NAME, 'cusid').send_keys(customerid)
    context.driver.find_element(By.NAME, 'cusid').send_keys('61033')
    # context.driver.find_element(By.NAME, 'cusid').send_keys('33686')
    # context.driver.find_element(By.NAME, 'cusid').send_keys('17119')
    context.driver.find_element(By.NAME, 'AccSubmit').click()
    context.driver.find_element(By.NAME, 'city').clear()
    context.driver.find_element(By.NAME, 'city').send_keys("nagpur")
    time.sleep(5)


@then(u'click on edit submit button')
def step_impl(context):
    context.driver.find_element(By.NAME, 'sub').click()
    context.driver.switch_to.alert.accept()
    time.sleep(5)
    context.driver.close()
