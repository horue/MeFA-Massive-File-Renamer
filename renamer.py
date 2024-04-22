import os
import easygui
import random
import shutil
import tkinter


def rename(folder_input):
    n=str(random.randint(1000, 9999))

    output_path = os.path.join(os.path.expanduser("~"), f"Documents\\MeFA\\Renamed Files\\{folder_input}")
    if not os.path.exists(output_path):
        os.makedirs(output_path)



    for files in folder_input:
        shutil.move(os.path.join(folder_input, files), os.path.join(output_path, n + '_' + files))








def run():
    input('Como os arquivos serão renomeados? ')
    folder_input = easygui.diropenbox()
    rename(folder_input)

run()