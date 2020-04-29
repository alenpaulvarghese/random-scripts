#!/usr/bin/python3
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
command = ['youtube-dl']
query = []

#Starting Of Main Loop
while True:
    input_link = input('link > ')
    query.append(f'Link --> {input_link}')
    #If Playlist Found
    if 'playlist' in input_link:
        print('[?] Playlist found ')
        while True:
            print('')
            #Confirming To Download As Playlist
            playlist_enable = str(input('[?] Download As Playlist [y/n] > ').lower())
            if playlist_enable == 'y' or playlist_enable == 'n':
                if playlist_enable == 'y':
                    command.append('--yes-playlist')
                    query.append('Downloading as playlist')
                    break
                else:
                    command.append('--no-playlist --playlist-start 1 --playlist-end 1')
                    break
            #In Case Of Invalid Input
            else:
                print('Try Again')
                pass

#Starting Of Additional  Options Loop
    while True:
        #Confirming To Goto Additional Options
        advanced_option = str(input('[?] Additional Options [Y/N] > ').lower())
        if advanced_option == 'y' or advanced_option == 'n':
            if advanced_option == 'y':
                #Options Available 
                print('''
Please Choose Options:
1.Downloading Path
2.Playlist Start
3.Playlist Stop
4.Subtitle Format
5.Exit Advanced Option''')
                #Starting of Secondary Additional Options Loop
                while True:
                    advanced = int(input('> '))
                    if advanced == 1 or advanced == 2 or advanced == 3 or advanced == 4 or advanced == 5:
                        #Playlist Start
                        if advanced == 2:
                            number = int(input('Enter The Playlist Start Number > '))
                            command.append(f'--playlist-start {number}')
                            #For Query Section
                            query.append(f'Playlist Start = {number}')

                        #Playlist Stop
                        if advanced == 3:
                            number = int(input('Enter The Playlist Stop Number > '))
                            command.append(f'--playlist-end {number}')
                            #For Query Section
                            query.append(f'Playlist Stop = {number}')

                        
                        if advanced == 1:
                            while True:
                                input_path = str(input('path>'))
                                home_path = ''
                                if 'home' in input_path:
                                    actual_path = input_path
                                else:
                                    home_path = os.getcwd().split('/')
                                    home_path = f'/{home_path[1]}/{home_path[2]}'
                                    actual_path = os.path.join(home_path,input_path)

                                if os.path.isdir(actual_path):
                                    downloading_path = actual_path
                                    os.chdir(actual_path)
                                    print('Options Saved')
                                    break
                                else:
                                    print('Not A Valid Path or Directory')
                                    pass
                        #Not Adding Now
                        if advanced == 4:
                            pass

                        #Exiting 
                        if advanced == 5:
                            print('Options Saved')
                            break
                    #In Case Of Invalid Input
                    else:
                        print('Try Again1')
                        pass

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
    query.append(f'Download Path --> {os.getcwd()}')
    #Subtitle Selection
    while True:
        include_subtitle = str(input('[?] Include Subtitle [y/n] > ').lower())
        if include_subtitle == 'y' or include_subtitle == 'n':   
            if include_subtitle == "y":
                #For Query Section
                query.append('Downloading with subtitles')
                #For Downloading Section
                command.append('--write-sub --write-auto-sub --convert-subs srt')
                break
            else:
                #For Query Section
                query.append('Downloading without subtitles')
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
    command.insert(1,f'-f {downloading_resoulution}')

    querys = ''
    #Confirming Everthing
    print('\t\t'+'Please Confirm !')
    for helpers in query:
        querys+= '\t' + helpers + '\n'
    print(querys)
    
    command.append(input_link)
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
                execute = ''
                for helpers in command:
                    execute += helpers + ' '
                os.system(execute)
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
