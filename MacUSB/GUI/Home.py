"""         Home 
    The home page for MacUSB.
"""

import sys

from tkinter import *

from Mods.TriggerButton import TriggerButton
from Utils.Resource import Resource
from GUI.CreateInstallMedia import CreateInstallMedia

sys.path.append("..")
from MacUSB import Program

class Home(Tk):
    def __init__(self):
        super().__init__()
        self.title(Program.NAME)
        
        self.menubar = Menu(self)
        self.menu = Menu(self, tearoff=0)
        self.menu.delete(0)

        self.menu.add_command(label="dasasd", command=lambda:print("hi"))
        self.config(menu=self.menubar)

        self.geometry("520x320")
        self.resizable(0, 0)

        #.     Create installation media     .#

        self.createinstallmedia = Frame(self, width=370, height=60)
        self.createinstallmedia.place(relx=.5, rely=.3, anchor='c')

        self.createinstallmedia.grid_propagate(0)

        self.createinstallmedia.title = Label(self.createinstallmedia, background="gray20", foreground="white", font=("SF Pro Display", 20, "bold"), text="Create installation media")
        self.createinstallmedia.title.pack(pady=0)

        self.createinstallmedia.description = Label(self.createinstallmedia, background="gray20", foreground="white", font=("SF Pro Display", 15), text="Create a bootable USB installer using installer application.")
        self.createinstallmedia.description.pack(pady=0)

        self.createinstallmedia.trigger = TriggerButton(self.createinstallmedia, command=lambda self=self: self.trigger_cim())
        self.createinstallmedia.trigger.pack(pady=0)

        self.mainloop()

    def trigger_cim(self):
        CreateInstallMedia()