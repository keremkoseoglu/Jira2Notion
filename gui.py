""" GUI module """
import tkinter as tk
from tkinter import DISABLED
import sys

class _Popup(tk.Tk):
    """ Popup """
    def __init__(self, callback):
        tk.Tk.__init__(self)
        self.popup = tk.Toplevel(self)
        self.popup.wm_title("Issue")
        self.popup.protocol("WM_DELETE_WINDOW", _Popup.on_close)
        self.popup.tkraise(self)
        tk.Label(self.popup, text="Issue number").pack(side="left", fill="x", pady=10, padx=10)
        self.issue_code = tk.StringVar(self.popup)
        tk.Entry(self.popup, textvariable=self.issue_code).pack(side="left", fill="x")
        self.button = tk.Button(self.popup, text="Transfer", command=self.on_button)
        self.button.pack(fill="x")
        self.callback = callback
        self.withdraw()

    def on_button(self):
        """ Called when OK is clicked """
        self.button["state"] = DISABLED
        self.popup.update()
        self.callback(self.issue_code.get())

    @staticmethod
    def on_close():
        """ Called when window is closed """
        sys.exit(0)


def get_value_by_popup(callback):
    """ Main Popup function """
    app = _Popup(callback)
    app.mainloop()
