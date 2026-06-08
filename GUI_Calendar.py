from tkinter import *
from tkcalendar import *

root = Tk()
root.title("2026 Calendar")
root.geometry("600x400")

cal = Calendar(root, year=2026, month=6, day=4)
cal.pack(pady=60)

root.mainloop()