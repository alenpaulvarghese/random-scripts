import os  
import json
import textwrap
import time

#default config value
config = {
    "subtitle":{
        "language":"en",
        "format":"srt"
    }
}

try: 
    config = open('config.json','r')
except FileNotFoundError:
    with open("config.json","w") as write_file:
        json.dump(config,write_file)


while True:
    input_link = input('link > ')
    playlist_search = input_link.split('/')[3]
    playlist_search = str(playlist_search.split('?')[0])
    if playlist_search == 'playlist':
        print('[?] Playlist found ')
        while True:
            print('')
            playlist_enable = str(input('[?] Download As Playlist [y/n] > ').lower())
            if playlist_enable == 'y' or playlist_enable == 'n':
                if playlist_enable == 'y':
                    is_playlist = '--yes-playlist '
                    playlist_query = 'downloading as playlist '
                    break
                else:
                    is_playlist = '--no-playlist --playlist-start 1 --playlist-end 1 '
                    playlist_query = ''
                    break
            else:
                print('Try Again')
                pass   
    # input_id = str(input('[?] Additional Options [Y/N] > ').lower())
    # if input_id == 'y':
    while True:
        include_subtitle = str(input('[?] Include Subtitle [y/n] > ').lower())
        if include_subtitle == 'y' or include_subtitle == 'n':   
            if include_subtitle == "y":
                subtitle_include = 'yes'
                include_subtitle = '--write-sub --write-auto-sub'
                break
            else:
                subtitle_include = 'no'
                include_subtitle = ''
                break
        else:
            print('Try Again !')
            pass

    print('Please Choose the Format !')
    print('')
    os.system(f"youtube-dl -F --no-playlist --playlist-start 1 --playlist-end 1 {input_link}")
    downloading_resoulution = input('format_id > ')
    print(f'''
    Please Confirm !
    link = {input_link}
    include subtitle = {subtitle_include}
    format = {downloading_resoulution}
    {playlist_query}''')
    while True:
        confirmed = str(input('[y/n] > ').lower())
        if confirmed == 'y' or confirmed == 'n':
            if confirmed == 'y':
                timer = 1
                while timer<=3:
                    print(f'[!] Ok Starting Download ... {timer}')
                    timer+=1     
                    time.sleep(1)
                os.system('echo ')
                os.system(f"youtube-dl -f {downloading_resoulution} {is_playlist}{include_subtitle} --convert-subs srt '{input_link}'")
                break
            else:
                print('Ok resetting everything .')
                break
        else:
            print('Try again !')
            pass

            
