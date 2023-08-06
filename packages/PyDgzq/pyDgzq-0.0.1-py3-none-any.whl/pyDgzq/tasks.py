#-*-coding:utf 8-*-
import sqlite3
import time
import queue

class Tasks4Share():

	def __init__(self):
		init_sql = '''
			create table IF NOT EXISTS tasks (
			ID TEXT NOT NULL UNIQUE,
			TIME TEXT NOT NULL,
			isBLACK INT NOT NULL
			);
		'''
		conn = sqlite3.connect("tasks.db")
		c = conn.cursor()
		c.execute(init_sql)
		conn.commit()
		conn.close()
		self.task_list = queue.Queue()

	def submit_tasks(self, tasks):
		conn = sqlite3.connect("tasks.db")
		c = conn.cursor()
		for t in tasks:
			id = t["serial_no"]
			my_time = str(int(time.time()/1000))
			is_black = '0'
			sql = '''
			INSERT INTO tasks (ID,TIME,isBLACK) VALUES (\"{}\",\"{}\",{});
			'''.format(id, my_time, is_black)
			try:
				c.execute(sql)
			except:
				#数据插入不成功，未做处理。违反UNIQUE原则时，自动忽略。
				pass
		conn.commit()
		conn.close()

	def mark_black(self, serial_no):
		conn = sqlite3.connect("tasks.db")
		c = conn.cursor()
		sql = '''
			UPDATE tasks set isBLACK=1 where ID=\"{}\";
		'''.format(serial_no)
		try:
			c.execute(sql)
			conn.commit()
			conn.close()
			#print(serial_no, "标记为黑名单成功！")
			gaga = [
				str(time.time()),
				"展业账号:"+self.user_name,
				"申请编号"+serial_no,
				"标记为黑名单！"
				]
			self.notes.write("%~".join(gaga))
		except:				
			conn.close()
		
		

	def update_task_list(self):
		conn = sqlite3.connect("tasks.db")
		c = conn.cursor()
		sql = '''
			SELECT ID FROM tasks WHERE tasks.isBLACK=0;
		'''
		if self.task_list.empty():
			try:
				c.execute(sql)
				for item in c.fetchmany(100):
					self.task_list.put_nowait(item)
			except:
				print("update_task_list更新失败")
			finally:
				conn.close()

class notes():
	def __init__(self):
		init_sql = '''
			create table IF NOT EXISTS notes (
			msg TEXT NOT NULL
			);
		'''
		conn = sqlite3.connect("tasks.db")
		c = conn.cursor()
		c.execute(init_sql)
		conn.commit()
		conn.close()
	
	def write(self, note):
		sql = '''
			INSERT INTO notes (msg) VALUES (\"{}\");
		'''.format(note)
		conn = sqlite3.connect("tasks.db")
		c = conn.cursor()
		c.execute(sql)
		conn.commit()
		conn.close()
	
	def pull(self):
		#[ASC | DESC] 升序/降序
		sql_1 = '''
			SELECT * FROM notes ORDER BY notes.msg ASC;
		'''		
		sql_2 = '''
			DROP TABLE notes;
		'''
		sql_3 = '''
			create table IF NOT EXISTS notes (
			msg TEXT NOT NULL
			);
		'''
		conn = sqlite3.connect("tasks.db")
		c = conn.cursor()
		c.execute(sql_1)
		rows = c.fetchall()
		c.execute(sql_2)
		conn.commit()
		c.execute(sql_3)
		conn.commit()
		conn.close()
		return rows
		
		

if __name__ == "__main__":
	t4s = Tasks4Share()
	b = [
		{"serial_no":"12345"},
		{"serial_no":"1234ew"},
		{"serial_no":"123rt"},
		{"serial_no":"12345"}
	]
	t4s.submit_tasks(b)
	t4s.mark_black("123rt")
