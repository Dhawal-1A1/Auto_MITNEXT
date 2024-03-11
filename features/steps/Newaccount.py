from behave import *
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.common.exceptions
from selenium.webdriver.support.select import Select


@then(u'enter on New Account button')
def step_impl(context):
    # context.driver.find_element(By.LINK_TEXT,'New Account').click()
    context.driver.find_element(By.XPATH, '/html/body/div[3]/div/ul/li[5]/a').click()
    time.sleep(5)


@when(u'click on customer id')
def step_impl(context):
    context.driver.find_element(By.NAME, 'cusid').send_keys('61033')


@then(u'Select account type')
def step_impl(context):
    acc = context.driver.find_element(By.NAME, 'selaccount')
    drop = Select(acc)
    drop.select_by_index(1)


@then(u'Enter the initial deposit')
def step_impl(context):
    context.driver.find_element(By.NAME, 'inideposit').send_keys('1000')


@then(u'Click on new account submit button')
def step_impl(context):
    context.driver.find_element(By.NAME, 'button2').click()
    time.sleep(10)

