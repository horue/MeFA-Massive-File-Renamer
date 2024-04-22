import os
import easygui
import random
import shutil
import tkinter


def rename(folder_input):


    output_path = os.path.join(os.path.expanduser("~"), f"Documents\\MeFA\\Renamed Files\\{folder_input}")
    for files in folder_input:
        shutil.move(os.path.join(folder_input, files), os.path.join(output_path, {files+1} + files))








def run():
    input('Como os arquivos serão renomeados? ')
    folder_input = easygui.diropenbox()
    rename(folder_input)
