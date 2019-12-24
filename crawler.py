from bs4 import BeautifulSoup
from selenium import webdriver
import time
driver = webdriver.Chrome('/Users/scw/Downloads/chromedriver')
driver.get('http://old.statiz.co.kr/player.php?opt=1')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
data = soup.find('div', {'class': 'contents_main_full'})
data = data.findAll('div', {'style': 'position:relative; width:93px; margin:0px 0px 5px 1px; float:left;'})
all_records = {}
for d in data[0:5]:
    players = d.findAll('tr')
    for p in players[3:]:
        time.sleep(3)
        p_stat = p.find('a').attrs['href']
        p_stat_ = p_stat.split('?')[0] + '?opt=1&' + p_stat.split('?')[1]
        url = 'http://old.statiz.co.kr/' + p_stat_
        driver.get(url)
        html_ = driver.page_source
        p_soup = BeautifulSoup(html_, 'html.parser')
        p_data = p_soup.find('div', {'class': 'contents_main_full'})
        p_name = p_data.find('div', {'class': 'menu_title_left'}).contents[0]
        p_position = p_data.findAll('div', {'id': 'minimenu_list'})[7].contents[0]
        p_record = p_data.find('div', {'style': 'position:relative; width:940px; margin:0px 0px 5px 0px; clear:both;'})
        p_record = p_record.findAll('tr')
        all_records[p_name] = []
        all_records[p_name].append(p_position)
        if p_position == u'\ud22c\uc218':
            for r in p_record[3:-3]:
                year = []
                for r_content in r.contents[3:31]:
                    try:
                        year.append(r_content.contents[0].contents[0])
                    except:
                        if(isinstance(r_content.contents[0], basestring)):
                            year.append(r_content.contents[0])
                        else:
                            year.append('-1')
                all_records[p_name].append(year)
        else:
            for r in p_record[3:-3]:
                year = []
                for r_content in r.contents[3:30]:
                    try:
                        year.append(r_content.contents[0].contents[0])
                    except:
                        if(isinstance(r_content.contents[0], basestring)):
                            year.append(r_content.contents[0])
                        else:
                            year.append('-1')
                all_records[p_name].append(year)