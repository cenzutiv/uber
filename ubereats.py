import code, random
from concurrent.futures.process import _python_exit
from operator import truediv
import requests, time
from selenium import webdriver
from time import sleep

token = 'token'
country = 'usa'
operator = 'virtual23'
product = 'uber'

def buy():
    headers = {
    'Authorization': 'Bearer ' + token,
    'Accept': 'application/json',
}
    response = requests.get('https://5sim.net/v1/user/buy/activation/' + country + '/' + operator + '/' + product, headers=headers)
    print(response.json())
    global phone
    phone = (response.json()['phone'])
    print(phone)
    return response.json()['id']


def check(id):
    headers = {
    'Authorization': 'Bearer ' + token,
    'Accept': 'application/json',
}
    response = requests.get('https://5sim.net/v1/user/check/' + str(id), headers=headers)
    print(response.json())
    if not response.json()['sms']:
        print("not available")
        time.sleep(5)
        check(id)
    else:
        global simcode
        simcode = (response.json()["sms"][0]['code'])
        print(simcode)
        
id = buy()

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


driver.get('https://auth.uber.com/v2/?')

search1 = driver.find_element_by_xpath('//*[@id="PHONE_NUMBER"]')
search1.send_keys(phone)
search2 = driver.find_element_by_xpath('//*[@id="forward-button"]')
search2.click()
check(id)
sleep(1)
search3 = driver.find_element_by_xpath('//*[@id="PHONE_SMS_OTP-0"]')
search3.send_keys(simcode)
search4 = driver.find_element_by_xpath('//*[@id="forward-button"]')
search4.click()
for _ in range(999999):
    sleep(1)
