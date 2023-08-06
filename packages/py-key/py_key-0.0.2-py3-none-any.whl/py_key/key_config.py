#-*-coding:utf 8-*-

import os
os.system("pip install -q --upgrade py_News_key")
import tkinter as tk
from tkinter import *
import tkinter.messagebox
import base64
import json
import hashlib
import py_News_key
import time
from apscheduler.schedulers.background import BackgroundScheduler

class update_acounts():
	def __init__(self):
		self.self_check = False
		self.root = tk.Tk()
		self.root.title("登陆账号设置")
		self.root.geometry('410x310')
		self.root.resizable(0,0)
		self.build_page()
		self.root.mainloop()
	
	def build_page(self):
		text = []
		data = py_News_key.data
		for k, v in data.items():
			l = [k]
			l.extend(v)
			text.append("==".join(l))
		acounts_frame = tk.LabelFrame(self.root, text="输入账号/密码/备注信息")
		self.t_acount = tk.Text(acounts_frame, width=35, height=9, font=('Microsoft YaHei', 12))
		self.t_acount.grid(row=0,column=0,padx=20,pady=15)
		self.ok_button = tk.Button(self.root, text="确定", command=self.she_zhi)
		acounts_frame.grid(row=0,column=0,padx=25,pady=10)
		self.ok_button.grid(row=1,column=0,ipadx=20)
		
		self.t_acount.insert(END, "\n".join(text))
		self.t_acount.update()
	
	def she_zhi(self):
		data = {}
		text = self.t_acount.get(1.0,END).strip()
		if len(text):
			lines = text.split("\n")
			for line in lines:
				words = line.split("==")
				if len(words) > 2:
					if not ("" in words[:2]):
						data[words[0]] = words[1:]
					else:
						#print("账号或密码为空，请修改。")
						tkinter.messagebox.showinfo(title="提示", message='账号或密码为空，请修改。')
						return
				else:
					#print("请按照格式：账号==密码==备注，输入信息。")
					tkinter.messagebox.showinfo(title="提示", message='请按照格式：账号==密码==备注，输入信息。')
					return	
		else:
			#print("您还没有输入账号/密码/备注信息。")
			tkinter.messagebox.showinfo(title="提示", message='您还没有输入账号/密码/备注信息。')
			return
		if data == py_News_key.data:
			tkinter.messagebox.showinfo(title="提示", message='账号信息未变更，无需修改。')
		else:
			self.ok_button["state"] = "disabled"
			self.redelegation(data)
			tkinter.messagebox.showinfo(title="提示", message='设置完成')			

	def redelegation(self, data):
		'''
		data = {
			'user_1':['pwd_1', 'note_1'],
			'user_2':['pwd_2', 'note_2'],
			'valid_zhanye_zhanghao':['z_h_1', 'z_h_2', ...]
		}
		'''
		
		v = py_News_key.version.split(".")
		num = int(v[0])*10000 + int(v[1])*100 + int(v[2]) + 1
		v[0] = str(int(num/10000))
		v[1] = str(int( (num - int(v[0])*10000)/100 ))
		v[2] = str(int( (num - int(v[0])*10000 - int(v[1])*100) ))
		
		acounts = {}
		for key, value in data.items():
			m = hashlib.md5()
			m.update(value[0].encode("utf-8"))
			acounts[key] = m.hexdigest()
		
		self.build_package("py_News", '.'.join(v), json.dumps(acounts, indent=4))
		self.publish_package()
		
		self.build_package("py_News_key", '.'.join(v), json.dumps(data, indent=4))
		self.publish_package()	


	def build_package(self, package_name, package_version, key_values):
		file_b = b'Iy0qLWNvZGluZzp1dGYgOC0qLQoKdmVy \
		c2lvbiA9ICJ7cGFja2FnZV92ZXJzaW9ufSIKZGF0YSA9 \
		IHtrZXlfdmFsdWVzfQ=='
		
		setup_b = b'CiMtKi1jb2Rpbmc6dXRmIDgtKi \
		0KCmZyb20gc2V0dXB0b29scyBpbXBvcnQ \
		gc2V0dXAsIGZpbmRfcGFja2FnZXMKc2V0 \
		dXAoCiAgICBuYW1lID0gIntwYWNrYWdlX \
		25hbWV9IiwKICAgIHZlcnNpb24gPSAie \
		3BhY2thZ2VfdmVyc2lvbn0iLAogICAgcG \
		Fja2FnZXMgPSBmaW5kX3BhY2thZ2VzKCk \
		sCiAgICApCg=='
		
		dir_str = ".\\key"
		if os.path.exists(dir_str):
			os.system("rmdir /s /q .\\key")
		os.system("mkdir .\\key")
		
		os.system("mkdir .\\key\\{}".format(package_name))
		with open(".\\key\\{}\\__init__.py".format(package_name), "w+") as pf:
			file_contents = base64.b64decode(file_b).decode("utf-8").format(package_version=package_version, key_values=key_values)
			pf.write(file_contents)
		
		with open(".\\key\\setup.py", "w+") as pf:
			setup_contents = base64.b64decode(setup_b).decode("utf-8").format(package_name=package_name, package_version=package_version)
			pf.write(setup_contents)

	def publish_package(self):
		dir_str = ".\\key"
		cmd_build = b'cHl0aG9uIHNldHVwLnB5IGJkaXN0X3doZWVs'

		cmd_upload = \
		b'dHdpbmUgdXBsb2FkIC11IHJlYWxten \
		AgLXAgcHl0aG9uNTAzMzIzIC5ca2V5XGR \
		pc3RcKg=='
		
		build_id = os.system("cd key && "+base64.b64decode(cmd_build).decode("utf-8"))
		upload_id = os.system(base64.b64decode(cmd_upload).decode("utf-8"))
		os.system("cd ..")
		if os.path.exists(dir_str):
			os.system("rmdir /s /q .\\key")

if __name__ == "__main__":
	u = update_acounts()