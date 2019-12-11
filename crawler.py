from bs4 import BeautifulSoup
import urllib

response = urllib.urlopen("http://www.statiz.co.kr/stat.php")
html = response.read()
print "asdf"
