#-*-coding:utf 8-*-

import tkinter as tk
from pyDgzq.ui_elements import login_page

class page():
	
	def __init__(self):
		self.root = tk.Tk()
		l = login_page(self.root)
		self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
		self.root.mainloop()
	
	def on_closing(self):
		try:
			for item in self.root.bs.get_jobs():
				self.root.bs.pause_job(item.id)
				self.root.bs.remove_job(item.id)
			self.root.bs.shutdown()
		except:
			pass
		self.root.destroy()
	#	if self.root.config_page:
	#		self.root.config_page.page.destroy()


if __name__ == "__main__":
	page()
