# (c) AlenPaulVarghese
import os  
import json
import textwrap
import time

#default config value - going to add later 
# config = {
#     "subtitle":{
#         "language":"en",
#         "format":"srt"
#     }
# }

# try: 
#     config = open('config.json','r')
# except FileNotFoundError:
#     with open("config.json","w") as write_file:
#         json.dump(config,write_file)


#Intialising some Variables
playlist_query = ''
is_playlist = ''
advanced_options_actual = ''
advanced_query = ''

#Starting Of Main Loop
while True:
    input_link = input('link > ')
    #Checking If The Given Link Is Playlist Or Not
    playlist_search = input_link.split('/')[3]
    playlist_search = str(playlist_search.split('?')[0])
    #If Playlist Found
    if playlist_search == 'playlist':
        print('[?] Playlist found ')
        while True:
            print('')
            #Confirming To Download As Playlist
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
            #In Case Of Invalid Input
            else:
                print('Try Again')
                pas
    #Starting Of Additional  Options Loop
    while True:
        #Confirming To Goto Additional Options
        advanced_option = str(input('[?] Additional Options [Y/N] > ').lower())
        if advanced_option == 'y' or advanced_option == 'n':
            if advanced_option == 'y':
                #Options Available 
                print('''
Please Choose Options:
1.Playlist Start
2.Playlist Stop
3.Subtitle Language
4.Subtitle Format
5.Exit Advanced Option''')
                #Starting of Secondary Additional Options Loop
                while True:
                    advanced = int(input('> '))
                    if advanced == 1 or advanced == 2 or advanced == 3 or advanced == 4 or advanced == 5:
                        #Playlist Start
                        if advanced == 1:
                            number = int(input('Enter The Playlist Start Number > '))
                            advanced_options_actual+=f'--playlist-start {number} '
                            #For Query Section
                            advanced_query+=f'Playlist Start = {number} '

                        #Playlist Stop
                        if advanced == 2:
                            number = int(input('Enter The Playlist Stop Number > '))
                            advanced_options_actual+=f'--playlist-stop {number} '
                            #For Query Section
                            advanced_query+=f'Playlist Stop = {number}'

                        #Not Adding Now
                        if advanced == 3:
                            pass
                        if advanced == 4:
                            pass

                        #Exiting 
                        if advanced == 5:
                            print('Options Saved')
                            break
                    #In Case Of Invalid Input
                    else:
                        print('Try Again1')

            #If Addvanced Options Confirmation Is False and 
            #Breaking Advanced Options Loop
            else:
                break
        #In Case Of Invalid Input
        else:
            print('Try Again')
            pass
        #Breaking Advanced Options Loop
        break

    #Subtitle Selection
    while True:
        include_subtitle = str(input('[?] Include Subtitle [y/n] > ').lower())
        if include_subtitle == 'y' or include_subtitle == 'n':   
            if include_subtitle == "y":
                #For Query Section
                subtitle_include = 'yes'
                #For Downloading Section
                include_subtitle = '--write-sub --write-auto-sub'
                break
            else:
                #For Query Section
                subtitle_include = 'no'
                #For Downloading Section
                include_subtitle = ''
                break
        #In Case Of Invalid Input
        else:
            print('Try Again !')
            pass
    
    #Format Selection
    print('Please Choose the Format !')
    print('')
    os.system(f"youtube-dl -F --no-playlist --playlist-start 1 --playlist-end 1 {input_link}")
    downloading_resoulution = input('format_id > ')

    #Confirming Everthing
    print(f'''
    Please Confirm !
    link = {input_link}
    include subtitle = {subtitle_include}
    format = {downloading_resoulution}
    {playlist_query}
    {advanced_query}''')

    #Confirmation and Actual Download
    while True:
        confirmed = str(input('[y/n] > ').lower())
        if confirmed == 'y' or confirmed == 'n':
            if confirmed == 'y':
                #Timer Just For Fun
                timer = 1
                while timer<=3:
                    print(f'[!] Ok Starting Download ... {timer}')
                    timer+=1     
                    time.sleep(1)
                #Actually This Is The Real Download
                os.system('echo ')
                os.system(f"youtube-dl -f {downloading_resoulution} {is_playlist}{advanced_options_actual}{include_subtitle} --convert-subs srt '{input_link}'")
                break
            #To Reset Everything If Confirmation IS False
            else:
                print('Ok resetting everything .')
                break
        #In Case Of Invalid Input
        else:
            print('Try again !')
            pass
    #Breaking Of The Main Loop
    break
