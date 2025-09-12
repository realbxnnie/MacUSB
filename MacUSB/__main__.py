"""   __main__.py 
      Program runner.
"""

from tkinter import messagebox

from GUI.Home import Home
from Utils.UpdateChecker import UpdateChecker

from webbrowser import open_new_tab

if __name__ == "__main__":
    with UpdateChecker() as UC:
        if UC.Check() is True:
            answer = messagebox.askyesno(
                "A new version available",
                f"A new version {UC.ReceivedData["Version"]} is available. Would you like to update?"
                )
            if answer == True:
                    open_new_tab("https://github.com/realbxnnie/MacUSB/releases/latest")
            
    root = Home()