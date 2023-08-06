# -*- coding: UTF-8 -*-
import os
import sys
import json
from androidautotest.tool import *

# logger class
class Logger:
	log_dir = ''
	case_name = ''
	log_file_path = ''
	html_file_path = ''
	serial_file_path = ''
	
	log_list = []
	def __init__(self, case_name):
		self.case_name = case_name 
		# generate log file name
		time_log, time_str, random_str = random_id()
		# create log dir
		log_dir = r'%s%s%s.log.%s_%s' % (MODULE_PATH, PATHSEP, case_name, time_str, random_str)
		if not os.path.exists(log_dir):
			os.makedirs(log_dir)
		self.log_dir = log_dir
		self.log_file_path = r'%s%slog_%s_%s_%s.txt' % (log_dir, PATHSEP, case_name, time_str, random_str)
		self.html_file_path = r'%s%sreport_%s_%s_%s.html' % (log_dir, PATHSEP, case_name, time_str, random_str)
		self.serial_file_path = r'%s%sserial_log_%s_%s_%s.txt' % (log_dir, PATHSEP, case_name, time_str, random_str)
		print(r'------------------------------------------------------------')
		print(r'case %s start...' % self.case_name)

	def info(self, msg):
		log_file = open(self.log_file_path, mode='a+')
		print(msg)
		time_log, time_str, random_str = random_id()
		log_file.write(line_join(time_log, msg))
		log_file.close()
		if msg.startswith('[androidtest]') or msg.startswith('[matching]'):
			self.log_list.append(line_join(time_log, msg))
		elif msg.startswith('[adb]'):
			serial_file = open(self.serial_file_path, mode='a+')
			serial_file.write(line_join(time_log, msg))
			serial_file.close()

	def error(self, msg):
		log_file = open(self.log_file_path, mode='a+')
		print(msg)
		time_log, time_str, random_str = random_id()
		log_file.write(line_join(time_log, msg))
		log_file.close()
		self.log_list.append(line_join(time_log, msg))
		self.end(status='error')
	
	def end(self, status='normal'):
		log_list = self.log_list
		html_file = open(self.html_file_path, mode='a+')
		html_file.write('<meta http-equiv="Content-Type" content="text/html;charset=utf-8">')
		html_file.write('<body style="width:80%;margin-left:10%;">')
		if status == 'normal':
			html_file.write('<h2 style="background: green;color:#ffffff;padding-left:20px;">Case Result: Pass</h2>')
		else:
			html_file.write('<h2 style="background: red;color:#ffffff;padding-left:20px;">Case Result: Fail</h2>')
		steps = 0
		for i, log in enumerate(log_list):
			html_file.write('<div>')
			if log.find(r'[androidtest]') != -1:
				html_file.write('<div id="step%d" style="background: #6ab0de; margin-top:20px;color:#ffffff;height:40px;line-height:40px;border-radius:10px;padding-left:10px;">[Step%d] %s</div>' % (steps+1, steps+1, log.replace(r'[androidtest]', '')))
				steps = steps + 1
			elif log.find(r'[matching]') != -1:
				if (i < len(log_list)-1 and log_list[i+1].find(r'[androidtest]') != -1) or i == len(log_list)-1:
					matchObj = {}
					# window
					if PATHSEP == '\\':
						matchObj = json.loads(log[33:].replace('\\', r'\\'))
					else:# linux
						matchObj = json.loads(log[33:])
					html_file.write('<div style="margin-top:10px;">target:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="%s"></img></div>' % matchObj['template'])
					html_file.write('<div style="margin-top:10px;">screencap: <img src="%s"></img></div>' % matchObj['screencap'])
					if matchObj['exists'] == 'True':
						html_file.write('<div style="margin-top:10px;">confidence: %s</div>' % matchObj['confidence'])
						html_file.write('<div style="background: #e7f2fa;height:40px;line-height:40px;padding-left:10px;margin-top:10px;">Target picture is in screen</div>')
					else:
						html_file.write('<div  style="background: #e7f2fa;height:40px;line-height:40px;padding-left:10px;margin-top:10px;">Target picture is not in screen</div>')
			elif log.find(r'[error]') != -1:
				html_file.write('<div style="background: #eeffcc;height:200px;padding-left:10px;">%s</div>' % log[30:])
			html_file.write('</div>')
		
		html_file.write('<div style="position:fixed;display: flex;flex-direction: row;bottom:20px;z-index:10000;right:0;">')
		for i in range(steps):
			html_file.write('<a href="#step%d" style="background: #6ab0de;color:#ffffff;margin-right:10px;border-radius:20px;height:40px;width:40px;line-height:40px;text-align:center;text-decoration:none;color:#ffffff;">%d</a>' % (i+1,i+1))
		html_file.write('</div>')
		html_file.write('</body>')
		html_file.write('</html>')
		html_file.close()
		print(r'case %s end...' % self.case_name)
		print(r'------------------------------------------------------------')
		sys.exit(0)