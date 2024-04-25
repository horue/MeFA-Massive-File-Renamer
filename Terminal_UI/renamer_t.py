import os
import easygui
import random   
import shutil

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q','r','s','t','u','v','w','x','y','z']
names = ['ba', 'xe', 'za', 'ux', 'pd', 'le', 'rx']


def manual():
    number_n = 1
    source_path = easygui.diropenbox()
    output_path = os.path.join(os.path.expanduser("~"), f"Documents\\MeFA\\Renamed Files\\Manual Renamed")
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for files in source_path:
       print(f'Enter new name for {files}.')
       name=input(f'> ')
       extension = os.path.splitext(files)[1]
       shutil.move(os.path.join(source_path, files), os.path.join(output_path, name + '_' + str(number_n) + extension))
       number_n += 1




def rename_c(source_path, name):
    output_path = os.path.join(os.path.expanduser("~"), f"Documents\\MeFA\\Renamed Files\\{name}")
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    number_n = 1
    for files in os.listdir(source_path):
        extension = os.path.splitext(files)[1]
        shutil.move(os.path.join(source_path, files), os.path.join(output_path, name + '_' + str(number_n) + extension))
        number_n += 1


def rename(source_path, name):
    n1 = str(random.randint(0,9))

    output_path = os.path.join(os.path.expanduser("~"), f"Documents\\MeFA\\Renamed Files")
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for files in os.listdir(source_path):
        extension = os.path.splitext(files)[1]
        n2=str(random.randint(1000, 9999))
        n3=random.choice(alphabet)
        n4=random.choice(names)
        shutil.move(os.path.join(source_path, files), os.path.join(output_path, n3 + n1 + '_' + n2 + '_' + name + '_' + n3 + extension))


def run():
    print('How do you want to rename the files? ')
    print('If you press enter the program will generate a random name with a code.')
    name=input('> ')
    if name == '':
        name = 'h_MeFA_renamed_image'
        source_path = easygui.diropenbox()
        rename(source_path, name)
    else:
        source_path = easygui.diropenbox()
        rename_c(source_path, name)