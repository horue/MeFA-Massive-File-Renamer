import customtkinter as ct
import easygui as eg
from renamer_ui import *

def select(l2):
    global in_path
    in_path = eg.diropenbox()
    l2.configure(text=in_path)

def main(root):
    l1=ct.CTkLabel(root, text='MeFA - Massive File Renamer')
    l1.pack(pady=20)

    e1=ct.CTkEntry(root, placeholder_text='New name')
    e1.pack(pady=10)

    l2=ct.CTkLabel(root, text='Selected Folder: None')
    l2.pack()

    b1=ct.CTkButton(root, text='Select folder', command=lambda:select(l2))
    b1.pack(pady=20)

    b2=ct.CTkButton(root, text='Rename Files', command=lambda:run(name=e1.get(), source_path=in_path))
    b2.pack()

def root():
    root = ct.CTk()
    root.geometry("500x350")
    root.title("MeFA - Massive File Renamer")

    
    main(root)
    
    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()

root()