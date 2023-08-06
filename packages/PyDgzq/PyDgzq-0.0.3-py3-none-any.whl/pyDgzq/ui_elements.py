#-*-coding:utf 8-*-

from apscheduler.schedulers.background import BackgroundScheduler
import time
import tkinter as tk
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from pyDgzq.tasks import notes
from pyDgzq.runner import Launcher
#from config import info
import json
import os

class login_page():
	def __init__(self, mainWindow, info):
		self.info = info
		self.root = mainWindow
		self.root.title("展业工具-登陆")
		self.root.geometry('320x160')
		self.root.resizable(0,0)
		self.build_page()
		self.update()
	
	def update(self):
		res = os.system('pip uninstall -y -q pyNews ; pip install -y -q pyNews')
		if int(res) != 0:
			#报错结束程序。
			pass

	def build_page(self):
		self.login_frame = tk.Frame(self.root)
		l_user_name = tk.Label(self.login_frame, text='用户：')
		self.e_user_name = tk.Entry(self.login_frame, show=None, font=('Arial', 14),width=14)
		l_pwd = tk.Label(self.login_frame, text='密码：')
		self.e_pwd = tk.Entry(self.login_frame, show='*', font=('Arial', 14),width=14)
		b_ok = tk.Button(self.login_frame, text="登陆", command=self.submit_ok)

		l_user_name.grid(row=2,column=2,pady=3)
		self.e_user_name.grid(row=2,column=3)
		l_pwd.grid(row=3,column=2,pady=10)
		self.e_pwd.grid(row=3,column=3)
		b_ok.grid(row=4,column=3,pady=20,ipadx=10)

		self.login_frame.grid(row=0,column=0,padx=50, pady=20, ipadx=10, ipady=10)

	def submit_ok(self):
		if self.varify():
			self.login_frame.destroy()
			self.root.work_page = query_customer_page(self.root)
		else:
			tkinter.messagebox.showinfo(title="提示", message='账号或密码错误。')

	def varify(self):
		#检查账号密码是否合法
		try:
			from pyNews import data
			user = self.e_user_name.get()
			pwd = self.e_pwd.get()
			if user in data.keys():
				if data[user] == pwd:
					return True
				else:
					return False
			else:
				return False
		except:
			return False

class query_customer_page():
	def __init__(self, mainWindow):
		self.root = mainWindow
		self.root.title("展业工具")
		self.root.resizable(1,1)
		self.root.geometry('500x410')
		self.root.resizable(0,0)
		self.build_page()

	def build_page(self):
		args_frame = tk.LabelFrame(self.root, text="参数")
		args_frame.grid(row=0,column=0,padx=20,pady=10,ipadx=10)
		#"参数区"
		l_idno = tk.Label(args_frame,text=" 证件号是否空：")
		self.is_id = ttk.Combobox(args_frame,width=3)
		#起始时间
		s_time = time.strftime("%Y-%m-%d",time.localtime(time.time()-60*60*24*30))
		s_time_string = tkinter.Variable()
		s_time_string.set(s_time)
		l_date_s = tk.Label(args_frame,text="申请日期（起始）：")
		self.e_date_s = tk.Entry(args_frame, textvariable=s_time_string, 
		show=None, font=('Arial', 10),width=12, )
		#结束时间
		e_time = time.strftime("%Y-%m-%d",time.localtime(time.time()))
		e_time_string = tkinter.Variable()
		e_time_string.set(e_time)
		l_date_e = tk.Label(args_frame,text="申请日期（结束）：")
		self.e_date_e = tk.Entry(args_frame, textvariable=e_time_string, show=None, font=('Arial', 10),width=12)
		#刷新间隔
		interval = tkinter.Variable()
		interval.set(self.info["interval"])
		l_inter = tk.Label(args_frame,text="列表刷新间隔：")
		self.e_inter = tk.Entry(args_frame, textvariable=interval, show=None, font=('Arial', 10),width=12)
		
		l_date_s.grid(row=0,column=0,sticky=E,padx=2,pady=5)
		self.e_date_s.grid(row=0,column=1,sticky=W,padx=2,pady=5)
		l_date_e.grid(row=1,column=0,sticky=E,padx=2,pady=5)
		self.e_date_e.grid(row=1,column=1,sticky=W,padx=2,pady=5)
		l_idno.grid(row=0,column=2,sticky=E,padx=2,pady=5)
		self.is_id.grid(row=0,column=3,sticky=W,padx=2,pady=5)
		l_inter.grid(row=1,column=2,sticky=E,padx=2,pady=5)
		self.e_inter.grid(row=1,column=3,sticky=W,padx=2,pady=5)
		
		self.is_id["value"] = ("无", "是", "否")
		self.is_id.current(0)

		#操作区域
		self.do_frame = tk.Frame(self.root)
		self.b_start = tk.Button(self.do_frame, text="开始", command=self.action_start)
		#self.b_pause = tk.Button(self.do_frame, text="暂停", command="", state="disabled")
		#self.b_quit = tk.Button(self.do_frame, text="结束", command="", state="disabled")
		self.b_set = tk.Button(self.do_frame, text="设置", command=self.action_set)
		l_blank_3 = tk.Label(self.do_frame,text=" ")

		self.b_start.grid(row=0,column=0,padx=10,ipadx=10)
		#self.b_pause.grid(row=0,column=1,padx=10,ipadx=10)
		#self.b_quit.grid(row=0,column=2,padx=10,ipadx=10)
		l_blank_3.grid(row=0,column=3,padx=20,ipadx=10)
		self.b_set.grid(row=0,column=4,padx=20,ipadx=10)
		self.do_frame.grid(row=1,column=0)

		#显示区域
		self.echo_frame = tk.Frame(self.root)
		sb = tk.Scrollbar(self.echo_frame)
		self.text = tk.Text(self.echo_frame, width=65, height=19)

		sb.pack(side=tkinter.RIGHT,fill=tkinter.Y)
		self.text.pack(side=tkinter.LEFT,fill=tkinter.Y)
		self.echo_frame.grid(row=2,column=0,padx=10,pady=10)

		sb.config(command=self.text.yview)	 # 将文本框关联到滚动条上，滚动条滑动，文本框跟随滑动
		self.text.config(yscrollcommand=sb.set)	 # 将滚动条关联到文本框
		#self.text.insert(END,"helodji")
		#self.text.insert(END,"helodji")

	def action_set(self):
		#self.root.work_page.text.insert(END,"\n开始设置...")
		self.root.config_page = setting_page(self.b_set, self.root)
	
	def action_start(self):
		self.save_info()
		self.b_start["state"]="disabled"
		self.b_set["state"] ="disabled"
		#self.b_pause["state"]="normal"
		#self.b_quit["state"]="normal"
		self.n = notes()
		self.root.bs = BackgroundScheduler()
		
		#实例化机器人管理器
		self.launcher = Launcher(self.info)
		#启动并刷新显示信息
		time_string = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()+1))
		self.root.bs.add_job(self.launcher.fire, "date", run_date=time_string)
		self.root.bs.add_job(self.insert_msg, "interval", seconds=3)
		self.root.bs.start()
		gaga = [
			str(time.time()),
			"启动中……"
		]
		self.n.write("%~".join(gaga))
	
	def save_info(self):
		map_ = {
			"无":"",
			"是":"1",
			"否":"2"
		}
		self.info["is_idno"] = map_[self.is_id.get()]
		self.info["start_date"] = self.e_date_s.get()
		self.info["end_date"] = self.e_date_e.get()
		self.info["interval"] = self.e_inter.get()
		header = '''#-*-coding:utf 8-*-\n\ninfo = '''.encode("utf-8")
		body = json.dumps(self.info,indent=4).encode("utf-8")
		with open("config.py","w+") as pf:
			pf.truncate()
			lines = header + body
			pf.write(lines.decode("utf-8"))
		
		
	
	def insert_msg(self):
		msgs = self.n.pull()
		#print("msgs->",len(msgs))
		for m in msgs:
			msg = m[0].split("%~")
			msg_time = msg[0]
			if (time.time() - float(msg_time)) < 3:
				the_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
				echo = [the_time]
				echo.extend(msg[1:])
				echo_string = "\t".join(echo)
				self.text.insert(END, echo_string+"\n")
			self.text.update()
			self.text.see(END)
	
		
		
		


class setting_page():
	def on_closing(self):
		self.parent['state'] = 'normal'
		self.page.destroy()

	def __init__(self, parent_element, root):
		self.root = root
		self.parent = parent_element
		self.parent['state'] = 'disabled'
		self.page = tk.Toplevel(self.root)
		self.page.title("展业工具-设置")
		self.page.geometry('470x390')
		self.page.resizable(0,0)
		self.page.protocol("WM_DELETE_WINDOW", self.on_closing)
		self.build_page()
		self.page.mainloop()

	def build_page(self):
		
		acount_frame = tk.LabelFrame(self.page, text="展业账号")
		baidu_frame = tk.LabelFrame(self.page, text="百度引擎")
		ok_button = tk.Button(self.page, text="确定", command=self.save_args)
		
		baidu_frame.grid(row=1,column=0,columnspan=2,padx=20,ipadx=10)
		acount_frame.grid(row=0,column=0,columnspan=2,padx=2,pady=20,ipadx=5,sticky=N)
		
		
		#"百度引擎"
		self.l_id = tk.Label(baidu_frame, text="APP_ID：")
		self.l_aip = tk.Label(baidu_frame, text="百度AIP_KEY：")
		self.l_s = tk.Label(baidu_frame, text="百度Secret_KEY：")
		
		self.e_id_text = tkinter.Variable()
		self.e_id_text.set(self.info["app_id"])
		self.e_id = tk.Entry(baidu_frame, textvariable=self.e_id_text, show=None, font=('Arial', 10),width=19)
		
		self.e_aip_text = tkinter.Variable()
		self.e_aip_text.set(self.info["aip_key"])
		self.e_aip = tk.Entry(baidu_frame, textvariable=self.e_aip_text, show=None, font=('Arial', 10),width=40)
		
		self.e_s_text = tkinter.Variable()
		self.e_s_text.set(self.info["secret_key"])
		self.e_s = tk.Entry(baidu_frame, textvariable=self.e_s_text,show=None, font=('Arial', 10),width=40)
		
		self.l_id.grid(row=0,column=0,sticky=E,padx=2,pady=5)
		self.e_id.grid(row=0,column=1,sticky=W,padx=2,pady=5)
		self.l_aip.grid(row=1,column=0,sticky=E,padx=2,pady=5)
		self.e_aip.grid(row=1,column=1,sticky=W,padx=2,pady=5)
		self.l_s.grid(row=2,column=0,sticky=E,padx=2,pady=5)
		self.e_s.grid(row=2,column=1,sticky=W,padx=2,pady=5)
		
		#"展业账号"
		#l_acount = tk.Label(acount_frame, text='提示：请按"账号名/账号密码"格式录入，每个账户占据一行。')
		contents = []
		for item in self.info["workers"]:
			contents.append("==".join(item))
		contents = "\n".join(contents)
		self.t_acount = tk.Text(acount_frame, width=54, height=9)
		self.t_acount.grid(row=0,column=0,padx=10,pady=10,sticky=N)
		self.t_acount.insert(END,contents)
		self.t_acount.update()
		#l_acount.grid(row=1,column=0,padx=10,sticky=W)
		
		ok_button.grid(row=2,column=0,columnspan=2,pady=20,ipadx=10,ipady=2)
		
	def save_args(self):
		acount_text = self.t_acount.get(1.0,END).strip()
		acount_text.encode("utf-8")
		self.info["app_id"] = self.e_id.get()
		self.info["aip_key"] = self.e_aip.get()
		self.info["secret_key"] = self.e_s.get()
		
		name_pwd = []
		for line in acount_text.split("\n"):
			i = line.split("==")
			if len(i) == 2:
				name_pwd.append(i)
		self.info["workers"] = name_pwd
		temp = ''
		header = '''#-*-coding:utf 8-*-\n\ninfo = '''.encode("utf-8")
		body = json.dumps(self.info,indent=4).encode("utf-8")
		with open("config.py",'w+') as pf:
			temp = pf.read()
			pf.truncate()
			lines = header+body
			pf.write(lines.decode("utf-8"))
			#except:
				#pf.write(temp)
		self.parent["state"] = "normal"
		self.page.destroy()
			
		
