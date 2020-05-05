try:
	from bs4 import BeautifulSoup
	from simple_colors import *
	import requests
	import time
	import lxml
	import textwrap

except ImportError as err:
	import os 
	os.system('pip3 install bs4 simple-colors lxml requests')

inital_link = 'https://psarips.xyz/category/tv-show/'
dummy = 'https://psarips.xyz'

response = requests.get(inital_link)
html = response.text
soup = BeautifulSoup(html,"lxml")
body = soup.find('div',class_='hu-pad group')
hello = body.find_all('div',class_=['post-inner','post-hover'])

for items in hello:
	title = items.find('a').get('title')
	link_to_item = dummy + str(items.find('a').get('href'))
	content = items.find_all('p')[:]
	content = [item.get_text() for item in content]
	update = content[0][10:]
	category = content[1]
	author_date = content[2][2:]
	description = content[3]
	description =  textwrap.fill(description,width=80)


	print(f'\t\t\t\t {green(title,"bold")}   ->  {magenta(author_date,"bright")}') 
	print(f'{red("Update:","bold")}\n\t{update}')
	print(f'{red("category:","bold")}\n\t{category}')
	print(f'{red("Link:","bold")}\n\t{link_to_item}\n')
	print(f"{red('Description:','bold')}\n{description}\n\n")
	time.sleep(0.5)
	


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
