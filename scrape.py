from bs4 import BeautifulSoup

import requests

url = raw_input("ENETR A WEBSITE TO EXTRACT THE URL'S FROM: ")

r = requests.get("http://" +url)

data = r.text

soup = BeautifulSoup(data)

for link in soup.find_all('a')
    print(link.get('href'))
    
