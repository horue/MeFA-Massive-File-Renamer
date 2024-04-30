import customtkinter as ct


def main(root):
    b1=ct.CTkButton(root, text='Select folder')
    b1.pack(pady=20)
    print('')

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