import tkinter as tk
import login_gui


if __name__ == '__main__':

    t = tk.Tk()
    login_gui = login_gui.LoginGui(t)
    t.mainloop()

