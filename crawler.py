from bs4 import BeautifulSoup
import requests

req = requests.get('http://www.statiz.co.kr/player.php')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
data = soup.find('div', {'class': 'wrapper'})
data = data.find('div', {'class': 'content-wrapper'})
data = data.find('div', {'class': 'container'})
data = data.find('section', {'class': 'content'})
data = data.find('div', {'class': 'row'})
data = data.findAll('div', {'class': 'col-md-12 col-xs-12 col-sm-12 col-lg-12'})[1]
data = data.find('div', {'class': 'row'})
