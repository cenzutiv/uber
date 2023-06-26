from operator import truediv
import requests, time

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
    print(response.json()['phone'])
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
        print(response.json()["sms"][0]['code'])
id = buy()
check(id)
