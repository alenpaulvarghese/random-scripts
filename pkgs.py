from bs4 import BeautifulSoup
import requests
import os
import lxml
import re
import time

def request(said_url):
    session = requests.Session()
    session.headers = {"User-Agent": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Mobile Safari/537.36"}
    url = said_url
    content = session.get(url).content
    soup = BeautifulSoup(content, "lxml")
    return soup


def random_function(said_url, dependecy_name_constant, n):
    soup = request(said_url)
    # https://stackoverflow.com/questions/5999747/beautifulsoup-nextsibling
    table= (soup.find(string="Requires").find_next('table'))
    dependecy_links = table.find_all('a', href=True)
    dependecy_name = [x.text for x in dependecy_links]
    for items in dependecy_name:
        print(n)
        if items not in dependecy_name_constant:
            dependecy_name_constant.append(items)
            #print(dependecy_name_constant)
            n-=1
        else:
            n+=1
            if n<=10:
                return Flase
    dependecy_links = [x['href'] for x in dependecy_links]
    very_new_links = []
    for items in dependecy_links:
        soup = request(items)
        new_link = soup.find(string="Ubuntu 20.04 LTS (Focal Fossa)").find_next("td", class_=["w-50", "pl-4"])
        #print(new_link.find("a"))
        very_new_links.append(new_link.find('a', href=True))
    very_new_links = [x['href'] for x in very_new_links]
    for very_new_link in very_new_links:
        random_function(very_new_link, dependecy_name_constant, n)

dependecy_name_constant = []
n=0
print("working")
random_function("https://ubuntu.pkgs.org/20.04/ubuntu-universe-amd64/qpdf_9.1.1-1build1_amd64.deb.html", dependecy_name_constant, n)