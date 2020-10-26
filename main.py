import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

cpu_url = 'https://www.newegg.com/p/pl?d=cpu'

# opening up, connecting to, and grabbing the page
uClient = uReq(cpu_url)

# html parsing
page_soup = soup(uClient.read(), "html.parser")
uClient.close()

# Grabs each product
containers = page_soup.findAll('div', {"class": "item-container"})

for container in containers:
    brand = container.div.div.a.img['title']

    title_container = container.findAll('a', {'class': 'item-title'})
    product_name = title_container[0].text

    shipping_container = container.findAll('li', {'class': 'price-ship'})
    shipping = shipping_container[0].text.strip()

    print('Brand: ',brand)
    print('Product Name: ',product_name)
    print('Shipping: ', shipping)