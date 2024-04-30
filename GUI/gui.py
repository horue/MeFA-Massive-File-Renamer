import customtkinter as ct


def main(root):
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