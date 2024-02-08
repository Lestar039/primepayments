import hashlib

import requests

from settings.secrets import Secret

payment_creds = Secret().payment_creds()


async def create_pay_link(user_data: dict) -> str:

    url = 'https://pay.primepayments.ru/API/v1/'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = {
        'action': 'initPayment',
        'project': payment_creds.get("project_number"),
        'sum': user_data.get("price"),
        'currency': 'RUB',
        'innerID': user_data.get("user_id") + "" + user_data.get("comment"),
        'email': user_data.get("user_email"),
        'payWay': '1',
        'returnLink': 1,
    }
    concat_params = payment_creds.get("secret_one") + data['action'] + str(data['project']) + str(data['sum']) + data[
        'currency'] + str(
        data['innerID']) + data['email'] + data['payWay']
    hash_object = hashlib.md5(concat_params.encode())
    result_hash = hash_object.hexdigest()
    data['sign'] = result_hash
    response = requests.post(url=url, headers=headers, data=data)
    data = response.json()
    return data['result']


def my_hash(secret_data: str):
    hash_object = hashlib.md5((secret_data).encode())
    hash_object.hexdigest()
    return hash_object


def check_hash(secret_data: dict) -> str:
    sing = payment_creds.get("secret_one") + str(secret_data.get("orderID")) + str(
        secret_data.get("payWay")) + secret_data.get(
        "innerID") + str(
        secret_data.get("sum")) + str(secret_data.get("webmaster_profit"))
    hash_object = hashlib.md5(sing.encode())
    result_hash = hash_object.hexdigest()
    return result_hash


if __name__ == '__main__':
    data = {
        'action': 'initPayment',
        'project': 2,
        'sum': 1000,
        'currency': 'RUB',
        'innerID': "12" + "" + "bla bla bla",
        'email': "test@test@com",
        'payWay': '1',
        'returnLink': 1,
    }
    concat_params = payment_creds.get("secret_one") + data['action'] + str(data['project']) + str(data['sum']) + data['currency'] + str(
        data['innerID']) + data['email'] + data['payWay']
    hash_object = hashlib.md5(concat_params.encode())
    result_hash = hash_object.hexdigest()

    my_hash(result_hash)

    test_answer_sign_data = {
        "action": "order_payed",
        "project": 2,
        "orderID": 12,
        "date_pay": '2023-11-11',
        "payWay": 1,
        "payed_from": 1234,
        "innerID": "bla bla bla",
        "sum": 1000,
        "currency": "RUB",
        "email": "test@test.com",
        "webmaster_profit": 999,
        "sign": "1039e970525d33234c234dc7e0800202"
    }
