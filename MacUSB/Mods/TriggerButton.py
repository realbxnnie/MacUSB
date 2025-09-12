"""       TriggerButton 
    A tweak for tkmacosx button.
"""

from tkmacosx import CircleButton

class TriggerButton(CircleButton):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.configure(bg="gray25", fg="white", text="→", width=30, height=30, *args, **kwargs)