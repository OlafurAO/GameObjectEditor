import tkinter
import customtkinter

from game_object_screen import GameObjectScreen


class App:
	def __init__(self) -> None:
		customtkinter.set_appearance_mode('Dark')
		customtkinter.set_default_color_theme('blue')

		self.app = customtkinter.CTk()
		self.app.geometry('720x480')
		self.app.title('Bullet Hell Editor')

		self.game_screen = GameObjectScreen(self.app)
		self.current_frame = self.game_screen.get_frame()

		self.app.mainloop()

	def render_game_object_screen(self):
		self.current_frame.pack_forget()
		self.current_frame = self.game_screen.get_frame()
		self.current_frame.pack()
