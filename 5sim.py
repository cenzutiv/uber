from operator import truediv
import requests, time

token = 'eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTg5MDAzNzMsImlhdCI6MTYyNzM2NDM3MywicmF5IjoiMzI1OGQ1ODdhNzBlNTg4NjY1Y2NjNmQwZWU2ZDFlMWUiLCJzdWIiOjY4ODk0MX0.mSe5JUm9D67n7CZrmKtupB9CrMhaNg5yvhP8oUC2GrrFkUYvtwh6Vfrou9hyFTu0ql1L5BdLUxH0IdqPAX6QBof68htdWo7j-BBEM_j57vlOlhEHKRTJM01gen4abdABCiErE3tWSj4tAQVSOt0SdvI2sb3ArwAVgt-zl0Q4s58zKL5-WQYxiJyYaAQmJrClA_Df9nxpik3Vw_ERbOQk76vd3Tzd1sHZ41cvvYwoVWRfqD1jJUx41ZbFFZwBs6zMnsr0hOJI1yzmoDxADlcutPHaSV2lhI8-fDRtKgOiG7yT6f_SrMuNFSRHMRBiJBGTlCMMHTZSd-Ms-lHZJqrjcA'
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