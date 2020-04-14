#Made by AlenPaulVarghese
import os
import time

def what_if_someone_execute_this_file():
    while True:
        os.system('clear')
        time.sleep(1.0)
        print('\t\tActually this is not the file to be executed.')
        time.sleep(1.0)
        print('')
        print("\t\tType 'python3 wiki.py' and press ENTER.")
        time.sleep(1.0)
        print('')
        print('\t\tThanks for checking , by AlenPaulVarghese')
        time.sleep(1.0)
        print('')
        input_value = str(input('Do you like to parse the code here[y/n] : ').lower())
        print(input_value)
        os.system('clear')
        time.sleep(1)
        if (input_value == 'y'):
            print('select the file you want to parse : ')
            print('[1] wiki.py')
            print('[2] tools.py')
            input_value_second=int(input('Enter the number : '))
            if (input_value_second==1):
                os.system('less wiki.py')
                print('')
                print('Enjoy Reading ..............................................!')
                break
            elif(input_value_second==2):
                os.system('less tools.py')
                print('')
                print('Enjoy Reading ..............................................!')
                break
            else:
                pass
        else:
            os.system('clear')
            break
what_if_someone_execute_this_file()
try:
    from bs4 import BeautifulSoup
    import requests
    import os
    import lxml
    import time
    import textwrap


    #MAIN_FUCTIONS
    def stark_text_grabber(import_module,search_parameter):
        main_url = import_module
        response = requests.get(main_url)
        html = response.text
        soup = BeautifulSoup(html,"lxml")
        stark = soup.find('body')
        try:
            heading = stark.h1.text
            paragraph = stark.find('div',class_='mw-parser-output')
            paragraph_main = paragraph.find_all('p')[2].text
    #WRITER
            paragraph = textwrap.dedent(paragraph_main).strip()
            paragraph = textwrap.fill(paragraph,width=80)
            print(f'\t\t\t\t{heading}\n')
            print(f'{paragraph}\n')
    #ERROR_HANDLING     
        except IndexError:
            error('Not A Valid Search')
        except AttributeError:
            error('Not A Valid Search')

    def error(error_log):
            error_message=f'wiki> Soory Request Cannot Proceed Caused By "{error_log}", Try Again.'
            print(error_message)

    def stark_updater():
            os.system('echo ')
            os.system('pip3 install bs4 requests lxml')
            os.system('echo ')
            os.system('echo "[!] UPGRADE FINISHED"')
            os.system('echo ')
            os.system('echo "[?] Try restarting by tryping restart and press ENTER"')


    def restarter():
        print('[*] Rebooted Succefully')
        os.system('python3 wiki.py')

    #MESSAGES_STORED_IN_VARIABLE

    stark_help = '''
    what is this: 
        This is a simple module to fetch few informations from wikipedia 
        just type your search query and press ENTER.

    command usage:
        help : For retrieving help menu !
        about : For retrieving module description !
        quit or exit : For quiting the module !
        update or upgrade : for installing dependencies 
        reboot or restart : For restarting the module

    '''
    stark_about='''
    This is a simple module to grab some minor informations from wikipedia.org made by
    STARKTM1 aka AlenPaulVarghese as part of studying python web scraping and requests.'''


    def stark_parser():
        os.system('cat tools.py')
except ModuleNotFoundError:
    print('Seems like your running this module for the first time')
    print('Running updater script.....')
    import os 
    def stark_updater():
        os.system('echo ')
        os.system('pip3 install bs4 requests lxml')
        os.system('echo ')
        os.system('echo "[!] UPGRADE FINISHED"')
        os.system('echo ')
        os.system('echo "[?] Try restarting by tryping restart and press ENTER"')
    stark_updater()


    def restarter():
        print('[*] Rebooted Succefully')
        os.system('python3 wiki.py')
