#!/usr/bin/python3
# (c) AlenPaulVarghese
import requests
import sys
import os

'''
--------------------------------------------------------------------------
Pipe Directly -->
cat example.txt | ./dogbin.py or cat example.txt | python3 dogbin.py
--------------------------------------------------------------------------
To get short links -->
python3 dogbin.py https://example.com or ./dogbin.py https://example.com
--------------------------------------------------------------------------
For Multiline -->
python3 dogbin.py and paste the content in nano editor
and save the file without renaming
--------------------------------------------------------------------------
'''


def deldog(message):
    url = "https://del.dog/documents"
    r = requests.post(url, data=message.encode("UTF-8")).json()
    print(f"Your Link --> https://del.dog/{r['key']}")


message = ''
if not sys.stdin.isatty():
    for lines in sys.stdin:
        message += lines
    deldog(message)
else:
    try:
        deldog(list(sys.argv)[1])
    except IndexError:
        os.system("nano PasteYouContentHere-Dont-Change-File-Name")
        with open("PasteYouContentHere-Dont-Change-File-Name", "rb") as nano:
            lines = nano.readlines()
            for texts in lines:
                message += texts.decode('UTF-8')
        os.remove("PasteYouContentHere-Dont-Change-File-Name")
        deldog(message)
