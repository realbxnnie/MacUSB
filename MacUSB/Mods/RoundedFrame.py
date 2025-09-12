"""       RoundedFrame
        A tweak for Frame.
"""
from tkinter import Frame, Canvas, BOTH

class RoundedFrame(Frame):
    def __init__(self, master=None, corner_radius=25, **kwargs):
        super().__init__(master, **kwargs)
        self.corner_radius = corner_radius
        self.canvas = Canvas(self, bg=self['bg'], highlightthickness=0)
        self.canvas.pack(fill=BOTH, expand=True)
        self.bind("<Configure>", lambda e: self.draw_rounded_rectangle())

    def draw_rounded_rectangle(self):
        width = self.winfo_width()
        height = self.winfo_height()
        r = self.corner_radius
        self.canvas.delete("all") 
        self.canvas.create_arc((0, 0, 2*r, 2*r), start=90, extent=90, fill=self['bg'], outline=self['bg'])
        self.canvas.create_arc((width-2*r, 0, width, 2*r), start=0, extent=90, fill=self['bg'], outline=self['bg'])
        self.canvas.create_arc((0, height-2*r, 2*r, height), start=180, extent=90, fill=self['bg'], outline=self['bg'])
        self.canvas.create_arc((width-2*r, height-2*r, width, height), start=270, extent=90, fill=self['bg'], outline=self['bg'])

        self.canvas.create_rectangle((r, 0, width-r, height), fill=self['bg'], outline=self['bg'])
        self.canvas.create_rectangle((0, r, width, height-r), fill=self['bg'], outline=self['bg'])
