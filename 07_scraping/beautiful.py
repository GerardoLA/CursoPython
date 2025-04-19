from bs4 import BeautifulSoup
import requests

url = 'https://www.apple.com/es/shop/buy-mac/macbook-air'
response = requests.get(url)
if response.status_code == 200:
    print('La petición fue exitosa')

    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup.prettify())

title_tag = soup.title
if title_tag:
    print(f"El título de la web es: {title_tag.text}")


# find price using bs
# price_span = soup.find('span',class_='rc-prices-fullprice')
# if price_span:
#     print(f"El precio del producto es: {price_span.text}")

# find all the prices 
# price_span = soup.find_all('span',class_='rc-prices-fullprice') # funcionaría igual sin especificarle que es span
# for price in price_span:
#     print(f"El precio del producto es: {price.text} ")

# for i, price in enumerate(price_span):
#     if i % 4  == 0:
#         print(f"El precio {i} es : {price.text}")


# find each product and get the name and the price 
products = soup.find_all(class_='rc-productbundle')
for product in products:
    name = product.find(class_='list-title').text
    price = product.find(class_="rc-prices-fullprice").text
    print(f"El producto con las características:\n {name} \nTiene un precio de {price}\n")
