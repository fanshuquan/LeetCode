import json

import requests

BASE_URL = 'http://qq5623071.com/index.php/'


def get_demo_user_token():
    url = BASE_URL + 'webcenter/Register_web/getDemoUserToken'
    print('url:{}'.format(url))
    r = requests.get(url)
    return r


def join_demo_user_do():
    url = BASE_URL + 'webcenter/Register_web/joinDemoUserDo'
    print('url:{}'.format(url))
    payload = {
        "lotteryId": "bj_10",
        "numberPostion": 3
    }
    r = requests.post(url, data=json.dumps(payload))
    print(r.json())


def get_json():
    url = BASE_URL + 'lottery/lottery/get_json'
    print('url:{}'.format(url))
    payload = {
        "lotteryId": "bj_10",
        "numberPostion": 3
    }
    # cookies = get_demo_user_token().cookies
    phpsessid = get_demo_user_token().cookies['PHPSESSID']
    cookies = dict(PHPSESSID=phpsessid)
    r = requests.post(url, cookies=cookies, data=json.dumps(payload))

    obj = r.json()['Obj']
    print(obj)

    # 上一期
    pre_period_number = obj['PrePeriodNumber']

    # 上一期结果
    pre_result = obj['PreResult']

    # 这一期
    current_period = obj['CurrentPeriod']

    # 余额
    balance = obj['Balance']


def bet():
    url = BASE_URL + 'get_json'
    print('url:{}'.format(url))
    payload = {
        "lotteryId": "bj_10",
        "numberPostion": 3
    }
    r = requests.post(url, data=json.dumps(payload))


if __name__ == '__main__':
    # get_demo_user_token()
    get_json()
