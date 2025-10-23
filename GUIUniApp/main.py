import tkinter as tk
import frame_view as view

root = tk.Tk()
root.geometry("400x380")
root.title("Uni GUI Module")
root.resizable(False, False)

view.LoginFrame(root)

root.mainloop()