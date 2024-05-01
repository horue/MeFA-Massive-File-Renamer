import customtkinter as ct
import easygui as eg


def select():
    global in_path
    in_path = eg.diropenbox()


def main(root):
    l1=ct.CTkLabel(root, text='MeFA - Massive File Renamer')
    l1.pack(pady=20)

    l2=ct.CTkLabel(root, text='Selected Folder: None')
    l2.pack()

    b1=ct.CTkButton(root, text='Select folder', command=lambda:select())
    b1.pack(pady=20)

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