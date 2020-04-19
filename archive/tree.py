import os
path = os.getcwd() 
#change this to your likings 
folder_name = 'Videos'
file = os.path.join(path,folder_name)



with open("lister.txt","w") as file_name:
    for directory,name,file_names in os.walk(file):
        file_name.write(f'{directory}\n')
        file_name.write('\n')
        for video_name in file_names:
            file_name.write(f'\t\t{video_name}\n')
            file_name.write('\n')