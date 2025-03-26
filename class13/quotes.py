import requests
base_url='https://quotes.toscrape.com/'
repsonse=requests.get(url=base_url)
markup=repsonse.text
print(markup)