import aiohttp


json_data = [
    {
        "USD_in": "3.2650", "USD_out": "3.3050", "EUR_in": "3.4600", "EUR_out": "3.5300", "RUB_in": "3.4300",
        "RUB_out": "3.4900", "GBP_in": "0.0000", "GBP_out": "0.0000", "CAD_in": "0.0000", "CAD_out": "0.0000",
        "PLN_in": "0.0000", "PLN_out": "0.0000", "SEK_in": "0.0000", "SEK_out": "0.0000", "CHF_in": "0.0000",
        "CHF_out": "0.0000", "USD_EUR_in": "0.9270", "USD_EUR_out": "1.0600", "USD_RUB_in": "93.6000",
        "USD_RUB_out": "0.0104", "RUB_EUR_in": "0.0098", "RUB_EUR_out": "99.2000", "JPY_in": "0.0000",
        "JPY_out": "0.0000", "CNY_in": "4.5200", "CNY_out": "4.6200", "CNY_EUR_in": "0.0000",
        "CNY_EUR_out": "0.0000", "CNY_USD_in": "0.1370", "CNY_USD_out": "7.0800", "CNY_RUB_in": "0.0000",
        "CNY_RUB_out": "0.0000", "CZK_in": "0.0000", "CZK_out": "0.0000", "NOK_in": "0.0000", "NOK_out": "0.0000",
        "filial_id": "1246", "sap_id": "50000081",
        "info_worktime": "Пн |Вт 10 00 19 00 |Ср 10 00 19 00 |Чт 10 00 19 00 |Пт 10 00 19 00 |Сб 10 00 16 00 |Вс |",
        "street_type": "бул.", "street": "Шевченко", "filials_text": "Отделение 510\/173", "home_number": "12",
        "name": "Минск", "name_type": "г."
        },
    {
        "USD_in": "3.2650", "USD_out": "3.3050", "EUR_in": "3.4600", "EUR_out": "3.5300", "RUB_in": "3.4300",
        "RUB_out": "3.4900", "GBP_in": "0.0000", "GBP_out": "0.0000", "CAD_in": "0.0000", "CAD_out": "0.0000",
        "PLN_in": "0.0000", "PLN_out": "0.0000", "SEK_in": "0.0000", "SEK_out": "0.0000", "CHF_in": "0.0000",
        "CHF_out": "0.0000", "USD_EUR_in": "0.9270", "USD_EUR_out": "1.0600", "USD_RUB_in": "93.6000",
        "USD_RUB_out": "0.0104", "RUB_EUR_in": "0.0098", "RUB_EUR_out": "99.2000", "JPY_in": "0.0000",
        "JPY_out": "0.0000", "CNY_in": "4.5200", "CNY_out": "4.6200", "CNY_EUR_in": "0.0000",
        "CNY_EUR_out": "0.0000", "CNY_USD_in": "0.1370", "CNY_USD_out": "7.0800", "CNY_RUB_in": "0.0000",
        "CNY_RUB_out": "0.0000", "CZK_in": "0.0000", "CZK_out": "0.0000", "NOK_in": "0.0000", "NOK_out": "0.0000",
        "filial_id": "1246", "sap_id": "50000081",
        "info_worktime": "Пн |Вт 10 00 19 00 |Ср 10 00 19 00 |Чт 10 00 19 00 |Пт 10 00 19 00 |Сб 10 00 16 00 |Вс |",
        "street_type": "бул.", "street": "Центральная", "filials_text": "Отделение 110\/122", "home_number": "33",
        "name": "Пинск", "name_type": "г."
        }
    ]


def separate_filial(data_json: list, flag: bool = True) -> dict:

    result = {}

    for data in data_json:
        flag = True
        cur_in = {}
        cur_out = {}
        service_info = {}
        for name, cost in data.items():
            if name != 'filial_id' and flag:
                if name.split('_')[-1] == 'in':
                    if cost != 0:
                        cur_in[f'{name}'] = cost
                elif name.split('_')[-1] == 'out':
                    if cost != 0:
                        cur_out[f'{name}'] = cost
            elif name == 'filial_id':
                flag = False
            elif not flag:
                service_info[name] = cost

        result[data['filial_id'] + ': ' + data['name']] = {
            'in': cur_in,
            'out': cur_out,
            'info': service_info
        }

    return result


def city_list(json: dict) -> list:
    cities = list()
    for i in json:
        city = i['name']
        print(city)
        cities.append(city)
    return cities

city_list(json_data)

async def get_currency() -> separate_filial:
    # BelaBank api url here
    url = ''  # 'https://belarusbank.by/api/kursExchange'

    with aiohttp.ClientSession() as session:
        response = await session.get(url=url)

    return separate_filial(response.json())
