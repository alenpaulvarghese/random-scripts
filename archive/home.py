import os 

home = os.getcwd().split('/')[:3]
HOME = (f'/{home[1]}/{home[2]}')
