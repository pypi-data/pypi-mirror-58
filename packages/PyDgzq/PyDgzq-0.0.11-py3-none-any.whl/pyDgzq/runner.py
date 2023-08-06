#-*-coding:utf 8-*-
import execjs
import requests
import base64
import urllib
import re
import io
from PIL import Image
import time
from aip import AipOcr
from pyDgzq.md5 import js_code
from apscheduler.schedulers.background import BackgroundScheduler
from pyDgzq.tasks import Tasks4Share, notes
import json
from pyDgzq.ocr import img_clear
import random
from bs4 import BeautifulSoup

class Runner():

	def __init__(self, user_name, password, tasks_obj, buf, info):
		self.num_yy = 0
		self.info = info
		self.buf = buf
		self.notes = notes()
		#self.session = requests.session()
		self.tasks = tasks_obj
		#self.session.headers["User-Agent"] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
		self.user_name = user_name
		self.password = password
		self.baidu = AipOcr(self.info["app_id"],self.info["aip_key"], self.info["secret_key"])
		self.baidu_max_try = 5
		self.msg = []
		self.scheduler = BackgroundScheduler(job_defaults={'max_instances': 1})
		self.first_login = True
		self.relogin_interval = 10*60	#掉线后重新连接的间隔时间，默认10分钟。

	def get_solt(self):
		html = self.session.get("https://c.dgzq.com.cn:8888/").text
		pre_solt = re.findall("hex_hmac_md5\(\"[0-9a-zA-Z]{32}", html)
		return pre_solt[0].split("\"")[1]

	def md5_js(self, password):
		#with open(".\\js\\md5.js", "r") as pf:
		#	 js_code = pf.read()
		js_exec = execjs.compile(js_code)
		pwd = js_exec.call("hex_md5", password)
		solt = self.get_solt()
		#print("solt:",solt)
		return js_exec.call("hex_hmac_md5", solt, pwd)

	def get_code(self, type):
		url = {
			"login" : "https://c.dgzq.com.cn:8888/LoginImg",
			"query" : "https://c.dgzq.com.cn:8888/cgi-bin/zlbq/YzmAction?function=GetYzm"
		}
		max_try = self.baidu_max_try
		r = self.session.get(url[type])
		time.sleep(2)
		byte_stream = io.BytesIO(r.content)
		img = Image.open(byte_stream)
		img = img_clear(img)
		imgByteArr = io.BytesIO()
		img.save(imgByteArr, format='PNG')
		image = imgByteArr.getvalue()
		options = {
			"probability" : "true",
			"language_type" : "ENG"
			}
		while max_try:
			res = self.baidu.basicGeneral(image, options)
			if "words_result" in res.keys():
				#print(res)
				return res["words_result"]
			else:
				max_try = max_try - 1
		if max_try:
			#print(u"百度云OCR功能异常")
			exit()

	def login(self):
		self.session = requests.session()
		self.session.headers["User-Agent"] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
		url = "https://c.dgzq.com.cn:8888/login.do"
		code = self.get_code("login")[0]["words"]
		print("ms-code:",code)
		data = {
			"validate" : "login",
			"valCode" : code,
			"userId" : self.user_name,
			"pass" : self.md5_js(self.password)
		}
		res = self.session.post(url, data=data)
		if "您输入的用户名或密码有误".encode("utf-8") in res.content:
			gaga = [
				str(time.time()),
				"展业账号:"+self.user_name,
				"展业账号-密码异常，放弃登陆尝试。"
				]
			self.notes.write("%~".join(gaga))
			for item in self.scheduler.get_jobs():
				self.scheduler.remove_job(item.id)
			#self.scheduler.shutdown()
			return
		if self.first_login:
			kba = self.is_alive()
			print(kba)
			if kba: #首次，连上
				return True
			else:	#首次，未连上
				time.sleep(5)
				print("链接",self.user_name)
				self.login()
				return True
		else:
			gaga = [
				str(time.time()),
				"展业账号:"+self.user_name,
				"重新连接..."
				]
			self.notes.write("%~".join(gaga))
			
			if self.is_alive(): #再次，连上
			#1、关闭“重新连接”的任务
			#2、打开被暂停的任务
				for item in self.scheduler.get_jobs():
					if "login" in item.name:
						self.scheduler.remove_job(item.id)
						#print(item.id,item.name,"已取消")
					else:
						self.scheduler.resume_job(item.id)
			else:	#再次，未连上
			#不处理，等待下一个10分钟过后自动连接。
				pass

	def state_check(self):
		if self.is_alive():
			self.first_login = False
		else:
			#1、暂停所有任务
			for item in self.scheduler.get_jobs():
				self.scheduler.pause_job(item.id)
			#2、开启“重新连接”任务：定时10分钟后再次连接
			self.scheduler.add_job(self.login, "interval", seconds=self.relogin_interval)  #注意修改

	def is_alive(self):
		url = "https://c.dgzq.com.cn:8888/jsp/keepSession.jsp?_dc={}".format(str(int(time.time())))
		#try:
		res = self.session.get(url)
		res = res.json()
		if res["success"]:
			self.msg.append("账号{}状态：在线".format(self.user_name))
			#print("在线")
			# gaga = [
				# str(time.time()),
				# "展业账号:"+self.user_name,
				# "状态->在线",
				# "队列中剩余 {} 条任务".format(str(self.tasks.task_list.qsize()))
				# ]
			# self.notes.write("%~".join(gaga))
			return True
		else:
			self.msg.append("账号{}状态：离线".format(self.user_name))
			#print("离线1",self.user_name)
			gaga = [
				str(time.time()),
				"展业账号:"+self.user_name,
				"状态->离线"
				]
			self.notes.write("%~".join(gaga))
			return False
		# except:
			# self.msg.append("账号{}状态：离线".format(self.user_name))
			# #print("离线",self.user_name)
			# gaga = [
				# str(time.time()),
				# "展业账号:"+self.user_name,
				# "状态->离线"
				# ]
			# self.notes.write("%~".join(gaga))
			# return False

	def query_customer_list(self):###需要修改
		#1、检查历史数据，确定刷新数量
		#2、刷新用户列表前，暂定领取用户
		#3、刷新完成，重新启动领取用户
		target_job = None
		for item in self.scheduler.get_jobs():
			#print(item)
			if  "claim" in item.name:
				self.scheduler.pause_job(item.id)
				target_job = item
				gaga = [
					str(time.time()),
					"展业账号:"+self.user_name,
					"即将开始客户列表更新，客户领取功能已暂停。"
				]
				self.notes.write("%~".join(gaga))
		if self.buf.size == 0:
			num = self.query(100)
		else:
			num = self.query(self.buf.size)
			self.buf.size = num
		if target_job:
			self.scheduler.resume_job(target_job.id)
			target_job = None
			gaga = [
				str(time.time()),
				"展业账号:"+self.user_name,
				"客户列表更新结束，客户领取功能已恢复运行。"
			]
			self.notes.write("%~".join(gaga))
		
	def query(self, pageSize):
		gaga = [
				str(time.time()),
				"展业账号:"+self.user_name,
				"开始更新用户列表……"
				]
		self.notes.write("%~".join(gaga))
		customer_list = []
		url = "https://c.dgzq.com.cn:8888/cgi-bin/zlbq/ZlbqAction?function=QueryZlbqList"
		data = {
			"pageNo" : str(random.randint(1,15)),
			"pageSize" : str(pageSize),
			"count" : "-1",
			"ord" : "",
			"yyb" : "1",	#营业部：东莞证券(1)
			"Is_lq" : "1",
			"Is_ykh" : "1",
			"O_lqrbh" : "",
			"is_idno" : self.info["is_idno"],	#证件号是否空：""(无)、"1"(是)、"2"(否)
			"I_SRC" : "0",
			"V_QSRQ" : self.info["start_date"],	#申请日期（起始）
			"V_JSRQ" : self.info["end_date"],	#申请日期（结束）
			"I_SQBH" : "",
			"I_SJ" : "",
			"yzm_code" : ""
		}
		#获取验证码
		ocr_res = self.get_code("query")
		if len(ocr_res):
			item = ocr_res[0]
			code = item["words"]
			aver = item["probability"]["average"]
			#print("查询验证码", code, aver)
			code = "".join(code.split(" "))
			code = "".join(code.split(","))
			code = "".join(code.split("."))
			code = "".join(code.split(":"))
			code = "".join(code.split("-"))
			code = "".join(code.split("="))
			code = "".join(code.split("~"))
			code = "".join(code.split("@"))
			code = "".join(code.split("*"))
			#print(code)
			if (float(aver) > 0.6) and (len(code) == 4):
				#print(code)
				data["yzm_code"] = code
				res = self.session.post(url, data=data)
				try:
					res = res.json()
					#print("验证码有效")
				except:
					#print(res.content)
					#print("验证码无效")
					return 0
				else:
					#print("总数",len(res["RESULT"]))
					#print("列表刷新结果",res["CODE"],res["NOTE"])
					if int(res["CODE"]) == 1:
						#print("ok",res['COUNT'])
						#data["pageSize"] = res['COUNT']
						for item in res["RESULT"]:
							i = {
								"serial_no":item["serial_no"],
								"client_name":item["client_name"],
								"mobile":item["mobile"],
								"branch_no":item["branch_no"],
								"curr_date":item["curr_date"],
								"client_gender":item["client_gender"],
								"channel_id":item["channel_id"]
							}
							customer_list.append(i)
						self.tasks.submit_tasks(customer_list)
						gaga = [
							str(time.time()),
							"展业账号:"+self.user_name,
							"更新用户列表->获取到｛｝条数据。".format(str(res['COUNT']))
						]
						self.notes.write("%~".join(gaga))
						return int(res['COUNT'])
		gaga = [
			str(time.time()),
			"展业账号:"+self.user_name,
			"更新用户列表->未获取到数据。"
		]
		self.notes.write("%~".join(gaga))	
		return 0		
						
	def claim(self):
		if self.tasks.task_list.empty():
			self.tasks.update_task_list()
		try:
			serial_no = self.tasks.task_list.get_nowait()[0]
		except:
			self.tasks.update_task_list()
		url = "https://c.dgzq.com.cn:8888/cgi-bin/zlbq/ZlbqAction?function=ZlbqKhlq"
		data = {
			"serial_no" : serial_no,
			"src_flag" : "2",
			"yzm_code" : ""
		}
		
		ocr_res = self.get_code("query")
		if len(ocr_res):
			item = ocr_res[0]
			code = item["words"]
			aver = item["probability"]["average"]
			#print("query", code1, aver)
			code = "".join(code.split(" "))
			code = "".join(code.split(","))
			code = "".join(code.split("."))
			code = "".join(code.split(":"))
			code = "".join(code.split("-"))
			code = "".join(code.split("="))
			code = "".join(code.split("~"))
			code = "".join(code.split("@"))
			code = "".join(code.split("*"))
			if (float(aver) > 0.65) and (len(code) == 4):
				data["yzm_code"] = code
				res = self.session.post(url, data=data)
				try:
					res = res.json()
				except:
					#print(res.content)
					#print("特殊点")
					gaga = [
						str(time.time()),
						"展业账号:"+self.user_name,
						"申请编号"+serial_no,
						"服务器返回错误数据（忽略）。"
					]
					self.notes.write("%~".join(gaga))
					return
				else:
					if "verification code" in res["NOTE"]:
						gaga = [
							str(time.time()),
							"展业账号:"+self.user_name,
							"申请编号"+serial_no,
							"验证码不正确。"
						]
						self.notes.write("%~".join(gaga))
						return
					elif "不得超过3条" in res["NOTE"]:
						#print("领取结果{}".format(serial_no),res["NOTE"])
						gaga = [
							str(time.time()),
							"展业账号:"+self.user_name,
							"申请编号"+serial_no,
							res["NOTE"]
							]
						self.notes.write("%~".join(gaga))
						return
					else:
						#将serial_no加入黑名单
						if self.tasks.mark_black(serial_no):
							gaga = [
								str(time.time()),
								"展业账号:"+self.user_name,
								"申请编号"+serial_no,
								"标记为黑名单！"
								]
							self.notes.write("%~".join(gaga))
						#插入黑名单时已经发送消息
						#print("领取结果{}".format(serial_no),res["NOTE"])
						return
		gaga = [
			str(time.time()),
			"展业账号:"+self.user_name,
			"申请编号"+serial_no,
			"客户领取不成功。"
		]
		self.notes.write("%~".join(gaga))

	def run(self, interval):
		self.query_customer_list()
		self.scheduler.add_job(self.claim, 'interval', seconds=interval)
		self.scheduler.add_job(self.query_customer_list, 'interval', seconds=int(self.info["interval"]))
		self.scheduler.add_job(self.state_check, 'interval', seconds=60)
		self.scheduler.start()
	
	def get_args(self):
		url1 = "https://c.dgzq.com.cn:8888/UIProcessor? \
		ObjDescribe=%B4%E6%C1%BF%BF%CD%BB%A7%D4%A4%D4% \
		BC&Table=vCLKHGXYY_JJR&hiddenBar=false&hiddenMenu \
		=false&ObjDescribe=%25E5%25AD%2598%25E9%2587% \
		258F%25E5%25AE%25A2%25E6%2588%25B7%25E9%25A2%2 \
		584%25E7%25BA%25A6"
		res = self.session.get(url1)
		token = re.findall("Token=[a-z\d]+\&", res.text)
		if not len(token):
			print("获取Token失败。")
			return None
		else:
			#预约类型
			YYLX_map = {}
			url2 = 'https://c.dgzq.com.cn:8888/OperateProcessor?operate=lcRZRQXYGXYY_M1&Table=vCLKHGXYY_JJR&'+token[0]
			res = self.session.get(url2)
			soup = BeautifulSoup(res.text, features="html.parser")
			yylx = soup.select('select[name="YYLX"]')[0]
			ops = yylx.select('option')
			for op in ops:
				YYLX_map[op.text] = op["code"]
			
			#print(YYLX_map)
			form = soup.select('form[id="DATA_FORM"]')[0]
			form_url = form["action"]
			#print(form_url)
			
			data = {}
			inputs = form.select('input')
			for item in inputs:
				if item.has_attr("id"):
					data[item["id"]] = item["value"]
			
			return {
				"map":YYLX_map,
				"mid_url":form_url,
				"data":data
			}
				
			#以下参数单独设置
			#data["YYLX"] = "14" 
			#data["KHBH"] = KHBH		#"000800184718"
			#data["SM"] = ""
	
	def yuyuekh(self, args, button):
		self.num_yy += 1
		form_url = args["mid_url"]
		data = args["data"]
		url3 = "https://c.dgzq.com.cn:8888"+form_url + "extResponse=true&EVENT_SOURCE=KHBH&EVENT_TYPE=0"
		while True:
			flag_exit = False
			res = self.session.post(url3, data)
			soup = BeautifulSoup(res.text, features="html.parser")
			body = soup.select("body")[0]
			KHH = re.findall("[\d]{8}", body.text)
			if len(KHH):
				data["KHH"] = KHH[-1]
			
			url4 = "https://c.dgzq.com.cn:8888"+form_url + "extWindow=true&PopupWin=true&NewWindow=false"
			res = self.session.post(url4, data)
			if "执行预约登记成功" in res.text:
				flag_exit = True
				print("执行预约登记成功")
				gaga = [
					str(time.time()),
					"客户编号："+data["KHBH"],
					"执行预约登记成功"
				]
				self.notes.write("%~".join(gaga))
			else:
				soup = BeautifulSoup(res.text, features="html.parser")
				try:
					msg = soup.select('div[id="msgBar"]')[0].text
					msg = "".join(msg.split("\n"))
					print(msg)
					gaga = [
						str(time.time()),
						"客户编号："+data["KHBH"],
						msg
					]
					self.notes.write("%~".join(gaga))
					if "预约过了" in msg:
						flag_exit = True
					if "客户号不存在" in msg:
						flag_exit = True
				except:
					flag_exit = True
					msg = "预约失败..."
					print(msg)
					gaga = [
						str(time.time()),
						"客户编号："+data["KHBH"],
						msg
					]
					self.notes.write("%~".join(gaga))
			if flag_exit:
				break
		time.sleep(random.randint(0,4))
		self.num_yy -= 1
		if self.num_yy == 0:
			button["state"] = "normal"	
			
			
class storage():
	def __init__(self):
		self.size = 0
		

class Launcher():
	
	def __init__(self, info):
		self.info = info
		self.t4s = Tasks4Share()
		self.bs = BackgroundScheduler()
		self.workers = []
		self.global_buf = storage()
		log = notes()
		gaga = [
			str(time.time()),
			"启动中……"
			]
		log.write("%~".join(gaga))
	
	def do_work(self,name,pwd):
		r = Runner(name,pwd, self.t4s, self.global_buf, self.info)
		self.workers.append(r)
		r.login()
		r.run(5)
		#self.ok = r.yuyuekh("", r.get_token())

	def fire(self):
		w = self.info["workers"]
		for user in w:
			i = random.randint(2,7)
			time_string = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()+i))
			#print(time_string)
			self.bs.add_job(self.do_work, "date", args=[user[0],user[1]], run_date=time_string)
		self.bs.start()
	

if __name__ == "__main__":
	info = {
		"aip_key": "i8AduWq9O5EPzzqaELlWgyIT",
		"secret_key": "KicsPusp7lFeaaQ4cWysg7ZvxGAh9rGt",
		"app_id": "11161267",
	}
	l=Launcher(info)
	l.do_work("680164", "a123456.")
	#if r.is_alive():
		#li = r.query_customer_list()
		#import json
		#with open("list.txt","r") as pf:
		#	 li = json.loads(pf.read())
		#for item in li[240:270]:
			#r.claim(item["serial_no"])
		#r.claim("4207245")
	#r.query_customer_list()
