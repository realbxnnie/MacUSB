"""         CreateInstallMedia 
      The install media creation page.
"""

import sys
from threading import Thread
from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk

from Utils.Resource import Resource
from Mods.MarqueeBar import MarqueeBar

from Mods.TriggerButton import TriggerButton

from tkmacosx import Button

from os import listdir
from Utils.InstallationMedia import InstallationMedia


class CreateInstallMedia(Tk):
    def __init__(self):
        super().__init__()
        self.title("Create Installation Media")

        self.geometry("520x320")
        self.resizable(0, 0)

        #. Installers .#

        self.installers_container = Frame(self)
        self.installers_container.place(relx=0.5, rely=0.5, anchor="c", relwidth=0.9, relheight=0.9)

        self.installers_scrollbar = Scrollbar(self.installers_container, orient=VERTICAL)
        self.installers_scrollbar.pack(side=RIGHT, fill=Y)

        self.installers = Canvas(self.installers_container, yscrollcommand=self.installers_scrollbar.set)
        self.installers.pack(side=LEFT, fill=BOTH, expand=True)

        self.installers_scrollbar.config(command=self.installers.yview)

        self.installer_frame = Frame(self.installers)
        self.installer_window = self.installers.create_window((0, 0), window=self.installer_frame, anchor="n")

        self.installer_frame.bind(
            "<Configure>",
            lambda e: self.installers.configure(scrollregion=self.installers.bbox("all"))
        )
        self.installers.bind("<Configure>", lambda e: self.installers.coords(self.installer_window, (self.installers.winfo_width() // 2, 0)))

        #. Volumes .#

        self.volumes_container = Frame(self)
        self.volumes_scrollbar = Scrollbar(self.volumes_container, orient=VERTICAL)
        self.volumes_scrollbar.pack(side=RIGHT, fill=Y)

        self.volumes = Canvas(self.volumes_container, yscrollcommand=self.volumes_scrollbar.set)
        self.volumes.pack(side=LEFT, fill=BOTH, expand=True)

        self.volumes_scrollbar.config(command=self.volumes.yview)

        self.volume_frame = Frame(self.volumes)
        self.volume_window = self.volumes.create_window((0, 0), window=self.volume_frame, anchor="n")

        self.volume_frame.bind(
            "<Configure>",
            lambda e: self.volumes.configure(scrollregion=self.volumes.bbox("all"))
        )
        self.volumes.bind("<Configure>", lambda e: self.volumes.coords(self.volume_window, (self.volumes.winfo_width() // 2, 0)))

        self.installer_select()
        self.mainloop()

    def installer_select(self):
        self.title("Select a macOS Installer")

        found = False 

        for widget in self.installer_frame.winfo_children():
            widget.destroy()

        for app in listdir("/Applications"):
            app_name = app.lower()
            if app_name.startswith("install mac") or app_name.startswith("install os x"):
                found = True 

                self.installers_container.place(relx=.5, rely=.5, anchor="c", relwidth=0.9, relheight=0.9)

                self.installer = Frame(self.installer_frame)
                self.installer.pack(pady=15)

                self.installer.title = Label(self.installer, text=app.replace(".app", ""), font=("SF Pro Display", 18, "bold"))
                self.installer.title.pack()

                self.installer.description = Label(self.installer, text="macOS Install Application", font=("SF Pro Display", 15))
                self.installer.description.pack()

                self.installer.trigger = TriggerButton(self.installer, command=lambda app=app: self.disk_select(app))
                self.installer.trigger.pack()
            
        if not found:
            self.error = Frame(self)
            self.error.place(relx=.5, rely=.5, anchor="c")

            self.error.title = Label(self.error, text="No macOS Installers found.", font=("SF Pro Display", 25, "bold"))
            self.error.title.pack()

            self.error.back = Button(self.error, text="Return", bg="gray17", fg="white", command=lambda x=self.error: x.destroy())
            self.error.back.pack() # lol

    def disk_select(self, installer):
        self.title("Select a Disk Volume")

        self.installers_container.place_forget()

        found = False

        for widget in self.volume_frame.winfo_children():
            widget.destroy()

        for vol in listdir("/Volumes"):
            self.volumes_container.place(relx=.5, rely=.5, anchor="c", relwidth=0.9, relheight=0.9)

            self.volume = Frame(self.volume_frame)
            self.volume.pack(pady=15)

            self.volume.title = Label(self.volume, text=vol, font=("SF Pro Display", 18, "bold"))
            self.volume.title.pack()

            self.volume.description = Label(self.volume, text="Volume", font=("SF Pro Display", 15))
            self.volume.description.pack()

            self.volume.trigger = TriggerButton(self.volume, command=lambda vol=vol: self.create(installer, vol))
            self.volume.trigger.pack()

            found = True 

        if not found:
            self.error = Frame(self)
            self.error.place(relx=.5, rely=.5, anchor="c")

            self.error.title = Label(self.error, text="No Disk Volumes found.", font=("SF Pro Display", 25, "bold"))
            self.error.title.pack()

            self.error.back = Button(self.error, text="Return", bg="gray17", fg="white", command=lambda x=self.error: x.destroy())
            self.error.back.pack() # lol

    def create(self, installer, volume):
        if messagebox.askyesno("Are you sure?", "Creating an installation media will overwrite the volume. Please confirm the action.") == True:
            self.volumes_container.destroy()
            Thread(target=self.start_installation_thread, args=(installer, volume), daemon=True).start()
        else:
            self.destroy()

    def start_installation_thread(self, installer, volume):
        def setup_progress():
            self.progress = Frame(self)
            self.progress.place(relx=.5, rely=.5, anchor='c')

            self.title("Create installation media")

            self.progress.title = Label(self.progress, text="Creating installation media...", font=("SF Pro Display", 25, "bold"))
            self.progress.title.pack()

            self.progress.bar = MarqueeBar(self.progress, bg_color="gray25", height=10)
            self.progress.bar.pack()


        self.after(0, setup_progress)

        self.installationMedia = InstallationMedia(installer, volume)
        result = self.installationMedia.start()

        def finish():
            if type(result) == int:
                messagebox.showinfo("Success", "Installation media created successfully!")
            else:
                messagebox.showerror("Error", f"Installation failed (code {result})")
            self.destroy()

        self.after(0, finish)

