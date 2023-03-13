import requests
from bs4 import BeautifulSoup

url = 'https://www.udemy.com/topic/python/'

req = requests.get(url)

soup = BeautifulSoup(req.content, 'html.parser')

res = soup.title

print(res.get_text())
