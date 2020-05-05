import requests
from bs4 import BeautifulSoup
import time
import lxml
import time

inital_link = 'https://psarips.xyz/category/tv-show/'
response = requests.get(inital_link)
html = response.text
soup = BeautifulSoup(html,"lxml")
body = soup.find('div',class_='hu-pad group')
hello = body.find_all('div',class_=['post-inner','post-hover'])
for items in hello:
	print(items.prettify())
	time.sleep(5)
# n=1
# for x in range(78):
# 	print(inital_link)
# 	inital_link=f'https://psarips.xyz/category/tv-show/page/{n}/'
# 	n+=1
# 	time.sleep(0.2)

# inital_link = 'https://psarips.xyz/category/movie/'
# n=1
# for x in range(171):
# 	print(inital_link)
# 	inital_link=f'https://psarips.xyz/category/movie/page/{n}/'
# 	n+=1
# 	time.sleep(0.3)
