import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.common.exceptions


@given(u'Launch Browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@given(u'Navigate to url')
def step_impl(context):
    context.driver.get('https://demo.guru99.com/v4')


@given(u'Enter UserID and Password')
def step_impl(context):
    context.driver.find_element(By.NAME, 'uid').send_keys('mngr556434')
    context.driver.find_element(By.NAME, 'password').send_keys('detUrEp')


@when(u'Click on Login button')
def step_impl(context):
    context.driver.find_element(By.NAME, 'btnLogin').click()


@then(u'Verify Manager id')
def step_impl(context):
    try:
        if context.driver.find_element(By.XPATH,
                                       '/html/body/table/tbody/tr/td/table/tbody/tr[3]/td').text == 'Manger Id : mngr556434':
            print('Manager id verified')
    except selenium.common.exceptions.NoSuchElementException:
        print('Wrong or different Manager id')


@when(u'Click on New Customer')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "New Customer").click()


@then(u'Fill Details')
def step_impl(context):
    context.driver.find_element(By.NAME, "name").send_keys("Karan")
    context.driver.find_element(By.NAME, "dob").send_keys("02/02/2002")
    context.driver.find_element(By.NAME, "addr").send_keys("Nagpur")
    context.driver.find_element(By.NAME, "city").send_keys("Mumbai")
    context.driver.find_element(By.NAME, "state").send_keys("Maharashtra")
    context.driver.find_element(By.NAME, "pinno").send_keys("440034")
    context.driver.find_element(By.NAME, "telephoneno").send_keys("9636323502")
    context.driver.find_element(By.NAME, "emailid").send_keys("gkuna4ls123@gmail.com")
    context.driver.find_element(By.NAME, "password").send_keys("gkuna4l123")
    time.sleep(5)


# global customerid

@then(u'Click on Submit button')
def step_impl(context):
    context.driver.find_element(By.NAME, "sub").click()
    time.sleep(5)
    customerid = context.driver.find_element(By.XPATH, '//*[@id="customer"]/tbody/tr[4]/td[2]').text

# print(customerid)
