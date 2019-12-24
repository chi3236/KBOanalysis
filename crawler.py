from bs4 import BeautifulSoup
import requests

req = requests.get('http://old.statiz.co.kr/player.php?opt=1')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
data = soup.find('div', {'class': 'contents_main_full'})
data = data.findAll('div', {'style': 'position:relative; width:93px; margin:0px 0px 5px 1px; float:left;'})