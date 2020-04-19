#Made by AlenPaulVarghes
from tools import *

#NAME-GRABER --> PRETTY USELESS
name = os.getcwd().split("/")[2]
print(f'Welcome to WIKI {name}! sir')
bye_message=f'Thanks For Using me , {name}'

# _MAIN_FUNCTION
try:
    while True:
        search_parameter = str(input('wiki> '))

        if search_parameter == 'quit' or search_parameter == 'exit':
            print(bye_message)
            break
        elif search_parameter=='upgrade' or search_parameter == 'update':
            stark_updater()
            pass
        elif search_parameter=='reboot' or search_parameter == 'restart':
            restarter()
            break
        elif search_parameter=='help':
            print(stark_help)
        elif search_parameter=='about':
            print(stark_about)
        else:
            search_query = f'https://en.wikipedia.org/wiki/{search_parameter}'
            stark_text_grabber(search_query,search_parameter)

# FOR NERDS WHO PRESS CTRL-C EVERYTIME
except KeyboardInterrupt:
    print()
    print(bye_message) 
# FOR NERDS WHO TURN OF NETWORK TO FOOL THE MODULE
except requests.exceptions.ConnectionError:
    error('No Internet')          


