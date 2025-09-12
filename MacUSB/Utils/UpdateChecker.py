"""   UpdateChecker 
 Checks for MacUSB updates.
"""

import requests
import sys 
 
from json import loads

sys.path.append("..")
from __init__ import Program

class UpdateChecker:
    def __init__(self):
        self.ReceivedData = {}
        self.ShouldUpdate = False

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def Check(self):
        with requests.get(Program.VERSION_TRACKER_URL) as req:
            self.ReceivedData = loads(req.content.decode('utf-8').strip())

        if self.ReceivedData["Version_ID"] > Program.VERSION_ID:
            self.ShouldUpdate = True
        else:
            self.ShouldUpdate = False
    
        return self.ShouldUpdate