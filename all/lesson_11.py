'''import requests # бібліотека для роботи

res_monobank = requests.get('https://api.monobank.ua/bank/currency')

print(res_monobank.status_code)

res_monobank.json()[:5:]

#for obj in res_monobank.json():
#    print(f'Object is {obj}, \nType is{type(obj)}', end = '\n\n')

my_currencies = {
    980: '🇺🇦',
    840: '🇺🇸',
    978: "🇪🇺",
    # 826: '🇬🇧',
}

my_rates = []
for obj in res_monobank.json():
    #print(obj.keys())
    if obj['currencyCodeA'] in my_currencies and  obj not in my_rates:
        my_rates.append(obj)

# print(my_rates)

for obj in my_rates:
    # print(obj)
    print(f"Країна: {my_currencies[obj['currencyCodeA']]} Купівля {obj['rateBuy']} Продаж: {obj['rateSell']}")
'''

'''import requests

resp = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5') # Отримати 

match resp.status_code:
    case 200:
        print('All okey, move on')
    case 429:
        print('Try later, more request')
    case _:
        print(resp.status_code)
'''

'''import requests

resp = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5') # Отримати

print(resp.status_code)

match resp.status_code:
    case 200:
        print('All okey, move on')
    case 429:
        print('Try later, more request')
    case _:
        print(resp.status_code)

my_currencies = {
    "USD": '🇺🇸',
    'EUR': "🇪🇺",
}

for obj in resp.json():
    print(f'Object is {obj}, \nType is{type(obj)}', end = '\n\n')

my_rates = []
for obj in resp.json():
    #print(obj.keys())
    if obj['ccy'] in my_currencies and obj not in my_rates:
        my_rates.append(obj)

print(my_rates)

for obj in my_rates:
    print(f"Країна: {my_currencies[obj['ccy']]} Купівля {obj['buy']} Продаж: {obj['sale']}")
'''

import requests

my_currencies = {
    840: 'USA',
    978: 'EURO',
    826: 'GBR',
    985: 'PLN',
    208: 'DKK'
}

resp = requests.get('https://api.monobank.ua/bank/currency')

print(resp.status_code)

print(resp.json())


'''my_rates = []
for obj in resp.json():
    if obj['currencyCodeA']:
        my_rates.append(obj)

print(my_rates)
'''
'''def exchange_api(url: str, my_currencies: dict):
    resp = requests.get(url)

    match resp.status_code:
        case 200:
            print('All okey')
        case 429:
            print('Try later')
        case _:
            print(resp.status_code)
    
    '''

'''#### Вивезти з API(приватбанка) курс валют для:
1. USA
2. EURO
3. GBR
4. PLN
5. Свою валюту

* Написати Test
* Вивезти курс валюти від користувача
* Робити перевірки на status code
* Написати це функцію'''

