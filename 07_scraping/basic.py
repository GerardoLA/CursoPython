# pip3 install requests -> instalas la dependencia para hacer peticiones
import requests
import re
url = 'https://www.apple.com/es/shop/buy-mac/macbook-air/'

response = requests.get(url)

if response.status_code == 200:
    print('La petición fue exitosa')
    html = response.text
    # print(html)

    # regular expresion para encontrar el precio
    price_pattern = r'<span class="rc-prices-fullprice">(.*?)</span>'
    match = re.search(price_pattern, html)

    if match:
        print(f"El precio es: {match.group(1)}")

