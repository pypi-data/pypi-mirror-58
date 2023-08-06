#-*-coding:utf 8-*-

import tkinter as tk
from pyDgzq.ui_elements import login_page

class page():
	
	def __init__(self, info):
		self.new_requests()
		self.info = info
		self.root = tk.Tk()
		l = login_page(self.root, self.info)
		self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
		self.root.mainloop()
	
	def new_requests(self):
		apps = [
			"APScheduler==3.6.3",
			"baidu-aip==2.2.18.0",
			"certifi==2019.11.28",
			"chardet==3.0.4",
			"idna==2.8",
			"Pillow==6.2.1",
			"PyExecJS==1.5.1",
			"pytz==2019.3",
			"requests==2.22.0",
			"six==1.13.0",
			"tzlocal==2.0.0",
			"urllib3==1.25.7"
		]
		with open("requests.txt","w+") as pf:
			pf.truncate()
			pf.write("\n".join(apps))
	
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
