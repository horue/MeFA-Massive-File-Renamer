import os
import easygui
import random   
import shutil
import sys
from renamer import run





def auto_rename():
    os.system('cls')
    print("#"*len('# MeFA - Massive File Renamer #'))
    print('# MeFA - Massive File Renamer #')
    print("#"*len('# MeFA - Massive File Renamer #'))
    run()

def manual_rename():
    print(1)

def help():
    print(1)

def principal_menu():
    option=input("> ")
    if option.lower() == ("1"):
        auto_rename()
    elif option.lower() == ('2'):
        manual_rename()
    elif option.lower() ==  ('3'):
        help()
    elif option.lower() == ("4"):
        sys.exit
    while option.lower() not in ['1', '2', '3', '4']:
        print("Please enter a valid command.")
        option=input("> ")





def principal():
    os.system('cls')
    print("#"*len('# MeFA - Massive File Renamer #'))
    print('# MeFA - Massive File Renamer #')
    print("#"*len('# MeFA - Massive File Renamer #'))
    print('1 — Auto Rename')
    print('2 — Manual Rename')
    print('3 — Help')
    print('4 — Exit')
    print('By horue.')
    principal_menu()


while True:
    principal()