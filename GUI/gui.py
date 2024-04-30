import customtkinter as ct


def main():
    print('')

def root():
    root = ct.CTk()
    root.geometry("400x350")
    root.title("Seiri - Desktop Organizer")

    
    main(root)
    
    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()

root()