from tkinter import Canvas 

def round_rectangle(canvas, x1, y1, x2, y2, radius=10, **kwargs):
    points = [
        x1+radius, y1,
        x2-radius, y1,
        x2-radius, y1,
        x2, y1,
        x2, y1+radius,
        x2, y2-radius,
        x2, y2-radius,
        x2, y2,
        x2-radius, y2,
        x1+radius, y2,
        x1+radius, y2,
        x1, y2,
        x1, y2-radius,
        x1, y1+radius,
        x1, y1+radius,
        x1, y1,
    ]
    return canvas.create_polygon(points, smooth=True, splinesteps=36, **kwargs)


class MarqueeBar(Canvas):
    def __init__(self, master=None, width=300, height=24, bar_length=80,
                 bar_color="#007aff", bg_color="#e1e1e1", radius=12, **kwargs):
        super().__init__(master, width=width, height=height, highlightthickness=0, **kwargs)
        
        self.width = width
        self.height = height
        self.bar_length = bar_length
        self.bar_color = bar_color
        self.bg_color = bg_color
        self.radius = radius

        self.pos = 0
        self.direction = 1
        self.speed = 5

        self.background_items = []
        self.bar_items = []
        self.draw_background()
        self.draw_bar()
        self.animate()

    def draw_background(self):
        for item in self.background_items:
            self.delete(item)

        self.background_items = [round_rectangle(self, 0, 0, self.width, self.height,
                                                 self.radius, fill=self.bg_color, outline=self.bg_color)]

    def draw_bar(self):
        for item in self.bar_items:
            self.delete(item)
        
        vertical_margin = 2
        self.bar_items = [round_rectangle(self, self.pos, vertical_margin,
                                          self.pos + self.bar_length, self.height - vertical_margin,
                                          self.radius, fill=self.bar_color, outline=self.bg_color)]

    def animate(self):
        max_pos = self.width - self.bar_length
        if self.pos >= max_pos:
            self.direction = -1
        elif self.pos <= 0:
            self.direction = 1

        self.pos += self.speed * self.direction
        self.draw_bar()
        self.after(20, self.animate)