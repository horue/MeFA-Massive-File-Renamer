import os
import easygui
import random
import shutil
import tkinter


def rename(source_path, name):
    n1 = str(random.randint(0,9))

    output_path = os.path.join(os.path.expanduser("~"), f"Documents\\MeFA\\Renamed Files")
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for files in os.listdir(source_path):
        extension = os.path.splitext(files)[1]
        n2=str(random.randint(1000, 9999))
        shutil.move(os.path.join(source_path, files), os.path.join(output_path, 'h' + n1 + '_' + n2 + '_' + name + extension))


def run():
    name=input('Como os arquivos serão renomeados? ')
    if name == '':
        name = 'h_MeFA_reanmed_image'
    source_path = easygui.diropenbox()
    rename(source_path, name)

run()