from bs4 import BeautifulSoup
import requests
import textwrap
import lxml

main_url = ("https://en.wikipedia.org/wiki/AI")
response = requests.get(main_url)
html = response.text
soup = BeautifulSoup(html,"lxml")
wiki = soup.find("body")
heading = wiki.h1.text
paragraph = wiki.find('div',class_="mw-parser-output")
paragraph = paragraph.find_all("p")
paragraph = paragraph[2].text
paragraph = textwrap.dedent(paragraph).strip()
paragraph = textwrap.fill(paragraph,width=90)
print (heading)
print (paragraph)