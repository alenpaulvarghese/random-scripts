#!/usr/bin/python3
# -*- coding: utf-8 -*-
# currently supports maple index only
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import argparse
import time, os


class Crawler(object):
    start = time.time()
    def __init__(self, timeout, head, writer):
        options = webdriver.ChromeOptions()
        if not head:
            options.add_argument('headless')
        options.add_argument("--log-level=3")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.t = timeout
        self.browser =  webdriver.Chrome(options=options)
        self.indent, self.retry = 0,0
        self.filename = writer


    def get(self, url):
        self.browser.get(url)
        try:WebDriverWait(self.browser, self.t).until(EC.invisibility_of_element((By.CLASS_NAME, "v-progress-linear__buffer")))
        except TimeoutException:
            if self.retry == 0:self.retry += 1;self.get(url);self.retry -= 1;return
            else:pass
        structure = list()
        all_items = [x for x in self.browser.find_elements_by_class_name("v-list-item--link")]
        for items in all_items:
            if items.find_elements_by_class_name("mdi-folder"):
                link = items.get_attribute("href")
                name = items.text
                structure.append((1,link, name))
            else:
                link = items.get_attribute("href")
                name = items.text
                structure.append((0, link, name))
        self.create(structure)


    def create(self, structure):
        for is_folder, link, name in structure:
            if (is_folder):
                self.indent += 1
                self.write_head(name)
                self.get(link)
                self.indent -= 1
            else:
                self.writer(link)


    def writer(self, text):
        indent = '\t'*self.indent
        with open(self.filename, "a") as writer:
            writer.writelines(indent + text)
            writer.writelines("\n")


    def write_head(self, text):
        indent = '\t'*(self.indent-1)
        with open(self.filename, "a") as writer:
            writer.writelines("\n" + indent + '['+text+']' + "\n")


def main():
    parser = argparse.ArgumentParser(description='Generate links from gdrive-index', epilog='By AlenPaulVarghese', prog="Gdirve Index Crawler")
    parser.add_argument('-v','--version', action='version', version='%(prog)s 1.0')
    parser.add_argument('link', help="Gdrive Index Link", type=str)
    parser.add_argument('-t', '--time', help="Time to wait for some particular page to load", type=int, default=30, metavar="", choices=range(20, 60))
    parser.add_argument('-w', '--write', help="Filename to write into", default="links.txt", type=str, metavar="")
    parser.add_argument('-H', '--head', action="store_true", help="pass to open chrome without headess mode")
    op = parser.parse_args()
    c = Crawler(op.time, op.head, op.write)
    c.get(op.link)


if __name__ == "__main__":
    try:main()
    except KeyboardInterrupt:
        pass