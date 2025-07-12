import requests
import requests
import xml.etree.ElementTree as ET




def get_crypto_price(symbol):
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    parameters = {
        'symbol': symbol,
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '1af90b71-a98c-413e-85dc-4cb25f7a7f6f', # Замените на свой API ключ
    }

    try:
        response = requests.get(url, headers=headers, params=parameters)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        price = data['data'][symbol]['quote']['USD']['price']
        resp = requests.get("https://www.cbr.ru/scripts/XML_daily.asp")
        test = ET.fromstring(resp.text)
        test_2 = test.findall('Valute')
        curs_usd_to_rub = 0
        for i in test_2:
            if i.get("ID") == "R01235":
                curs_usd_to_rub = float(i.find("Value").text.replace(",", "."))
        
        full_price = price * curs_usd_to_rub
        return round(full_price, 2)
    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")
        return None
    except (KeyError, IndexError) as e:
        print(f"Ошибка при обработке данных: {e}")
        return None

# Пример использования: