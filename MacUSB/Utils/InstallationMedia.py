"""        InstallationMedia
      Creates a bootable USB drive.
"""

import subprocess
import threading

class InstallationMedia:
    def __init__(self, installer, volume):
        self.installer = installer
        self.volume = volume


    def start(self):
        base_path = f'/Applications/{self.installer}/Contents/Resources/createinstallmedia'
        args = [base_path, "--volume", f"/Volumes/{self.volume}"]

        app_path_required = {
            "Install OS X Mavericks.app",
            "Install OS X Yosemite.app",
            "Install OS X El Capitan.app",
            "Install macOS Sierra.app",
        }

        if self.installer in app_path_required:
            args += ["--applicationpath", f"/Applications/{self.installer}"]
        args.append("--nointeraction")

        def run_process():
            process = subprocess.run(args)

            try:
                return process.returncode
            except subprocess.CalledProcessError as e:
                return e
