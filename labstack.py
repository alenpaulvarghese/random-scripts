from datetime import datetime
import os
import requests
import subprocess
import time
import json
import sys

filebase = input('Enter the file path > ')
if os.path.isfile(filebase):
    filesize = os.path.getsize(filebase)
    filename = os.path.basename(filebase)
    headers2 = {'Up-User-ID': 'IZfFbjUcgoo3Ao3m'}
    files2 = {"ttl":604800,"files":[{"name": filename, "type": "", "size": filesize}]}
    r2 = requests.post("https://up.labstack.com/api/v1/links", json=files2, headers=headers2)
    r2json = json.loads(r2.text)
    url = "https://up.labstack.com/api/v1/links/{}/send".format(r2json['code'])
    max_days = 7
    command_to_exec = [
        "curl",
        "-F", "files=@" + filebase,
        "-H","Transfer-Encoding: chunked",
        "-H","Up-User-ID: IZfFbjUcFoo3Ao3m",
        url
    ]
    try:
        t_response = subprocess.check_output(command_to_exec, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as exc:
        print(exc.output.decode("UTF-8"))
    else:
        t_response_arry = "https://up.labstack.com/api/v1/links/{}/receive".format(r2json['code'])
    print(t_response_arry + "\nMax Days:" + str(max_days))
else:
    print('Soory the file not found')
