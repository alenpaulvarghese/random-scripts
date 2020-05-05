#(c) AlenPaulVarghese
dummy = 'https://psarips.xyz'
inital_tv = 'https://psarips.xyz/category/tv-show/'
inital_movie = 'https://psarips.xyz/category/movie/'

#https://stackoverflow.com/a/16079581/13033981
class Finished(Exception): pass

try: 
	from bs4 import BeautifulSoup
	from simple_colors import *
	import requests
	import lxml
	import textwrap
	import time

	def content_graber(inital_link):
		response = requests.get(inital_link)
		html = response.text
		soup = BeautifulSoup(html,"lxml")
		footer = soup.head.title.getText()
		if 'Page not found' not in str(footer):
			body = soup.find('div',class_='hu-pad group')
			hello = body.find_all('div',class_=['post-inner','post-hover'])

			for items in hello:
				title = items.find('a').get('title')
				link_to_item = dummy + str(items.find('a').get('href'))
				try:
					content = items.find_all('p')[:]
					content = [item.get_text() for item in content]
					update = content[0]
					category = content[1]
					author_date = content[2][2:]
					description = content[3]
					description =  textwrap.fill(description,width=80)

					print(f'\t\t\t\t {green(title,"bold")}   ->  {magenta(author_date,"bright")}') 
					if 'update' in  update:
						print(f'{red("Update:","bold")}\n\t{update[10:]}')
					else:
						print(f'{red("Update:","bold")}\n\t{update}')
					print(f'{red("category:","bold")}\n\t{category}')
					print(f'{red("Link:","bold")}\n\t{link_to_item}')
					print(f"{red('Description:','bold')}\n{description}\n\n")
					

				except IndexError as err:
					pass
			print(blue(footer,'bold'))
		else:
			raise Finished
	
	def tv_series_grabber(inital_tv):
		n=0
		try:
			while True:
				content_graber(inital_tv)
				inital_tv=f'https://psarips.xyz/category/tv-show/page/{n}/'
				n+=1
				time.sleep(0.3)
		except Finished:
			pass
            

	def movie_grabber(inital_movie):
		n=0
		try:
			while True:
				content_graber(inital_movie)
				inital_movie=f'https://psarips.xyz/category/movie/page/{n}/'
				n+=1
				time.sleep(0.2)
		except Finished:
			pass


	tv_series_grabber(inital_tv)
	print(yellow('\nTv Series Page Finished Scraping Continuing to Scrap Movies Page',['bold','underlined']))
	time.sleep(3)
	movie_grabber(inital_movie)
	print(yellow('\nEverything Scrapped',['bold','underlined']))
	print(red('\nMade By AlenPaulVarghese',['bold','italic']))

except ImportError as err:
	import os 
	os.system('pip3 install bs4 simple-colors lxml requests')
	print('\n Please Re-Run the script')
	

