import tkinter
import customtkinter

class GameObjectScreen:
  def __init__(self, app) -> None:
    self.frame = customtkinter.CTkFrame(app)

    title = customtkinter.CTkLabel(self.frame, text='New Game Object', bg_color='transparent')
    title.pack(padx=10, pady=10)

    self.frame.pack()

  def get_frame(self):
    return self.frame
