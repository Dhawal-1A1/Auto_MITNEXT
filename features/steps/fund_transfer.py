import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.common.exceptions


@given(u'Click on Fund Transfer')
def step_impl(context):
    context.driver.execute_script('window.scrollBy(0,300);')
    context.driver.find_element(By.PARTIAL_LINK_TEXT, 'Fund Transfer').click()


@given(u'Enter Account Details')
def step_impl(context):
    context.driver.find_element(By.NAME, 'payersaccount').send_keys('132670')
    # context.driver.find_element(By.NAME, 'payeeaccount').send_keys('132671')
    context.driver.find_element(By.NAME, 'payeeaccount').send_keys('132672')
    context.driver.find_element(By.NAME, 'ammount').send_keys('18012')
    context.driver.find_element(By.NAME, 'desc').send_keys('TEST PURPOSE')
    time.sleep(2)


@given(u'Click Submit Button')
def step_impl(context):
    context.driver.find_element(By.NAME, 'AccSubmit').click()
    time.sleep(7)


@given(u'Click on Logout Button')
def step_impl(context):
    context.driver.find_element(By.PARTIAL_LINK_TEXT, 'Log out').click()

time.sleep(3)
