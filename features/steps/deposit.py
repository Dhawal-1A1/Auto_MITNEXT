import time
from behave import *
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By


@then(u'Click on Deposit')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div[3]/div/ul/li[8]/a').click()
    time.sleep(4)


@then(u'Enter Account Number, Amount and Discription')
def step_impl(context):
    context.driver.find_element(By.NAME, 'accountno').send_keys("132645")
    context.driver.find_element(By.NAME, 'ammount').send_keys("5000")
    context.driver.find_element(By.NAME, 'desc').send_keys("fees")


@then(u'Click on deposit submit button')
def step_impl(context):
    context.driver.find_element(By.NAME, 'AccSubmit').click()
    time.sleep(4)
