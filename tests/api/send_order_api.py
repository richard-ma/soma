import requests


if __name__ == "__main__":
    url = 'http://127.0.0.1:5000/api/stripe'
    data = {
        'url': 'http://www.hello.com',
        'merkey': '5bab7d89abf98da08f662c481e6617cc',
        'mode': 'mode_value',
        'cardNumberKeyValue': 'cardNumberKeyValue_value',
        'expireMonth': 'expireMonth_value',
        'expireYear': 'expireYear_value',
        'cvv': 'cvv_value',
        'orderid': 'orderid_value',
        'wtype': 'wtype_value',
        'total': '33',
        'currency': 'gbp',
        'firstname': 'firstname_value',
        'username': 'username_value',
        'email': 'email_value',
        'telephone': 'telephone_value',
        'country': 'country_value',
        'state': 'state_value',
        'city': 'city_value',
        'zipcode': 'zipcode_value',
        'address': 'address_value',
        'ip': 'ip_value',
        'useragent1': 'useragent1_value',
        'useragent2': 'useragent2_value',
        'comment': 'comment_value',
        'goodsname': {
            'price': 'price_value',
            'name': 'name_value',
            'attr': 'attr_value',
            'qty': 'qty_value',
        }
    }

    response = requests.post(url, data=data)
    print(response.text)