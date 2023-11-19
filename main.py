'''
import tkinter
import customtkinter

# System Settings
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Bullet Hell Editor")

# UI elements
title = customtkinter.CTkLabel(app, text="Welcome!")
title.pack(padx=10, pady=10)

# Input
string = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=string)
link.pack()

# Download button
button = customtkinter.CTkButton(app, text="AAAAAAAA", command=None)

app.mainloop()
'''
from app import App

if __name__ == '__main__':
  app = App()
  app.render_game_object_screen()