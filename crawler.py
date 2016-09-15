# -*- coding:utf-8 -*-
import requests
import re
import json
from bs4 import BeautifulSoup
from prettytable import PrettyTable

r = requests.get("http://www.ishadowsocks.net/")
soup = BeautifulSoup(r.text, "html.parser")
pw = soup.find_all(text=re.compile('密码'))
server = soup.find_all(text=re.compile('服务器'))
port = soup.find_all(text=re.compile('端口'))
status = soup.find_all('font')
status = [status[0].text, status[2].text, status[4].text]
def f(s):
	return s.split(':')[1]
pw = list(map(f, [pw[0],pw[2],pw[4]]))
server = list(map(f, [server[0],server[1],server[2]]))
port = list(map(f, [port[0],port[1],port[2]]))
l = []
for i in range(3):
	if status[i] == "正常":
		d = {"method": "aes-256-cfb", "server": server[i], "password": pw[i], "remarks": "", "server_port": port[i]}
		l.append(d)
	else:
		continue

info = PrettyTable(["服务器", "端口", "密码", "状态"])
for i in range(3):
	info.add_row([server[i], port[i], pw[i], status[i]])
print(info)


def get_pw(j):
	for x in range(len(j)):
		yield j[x]["server"],j[x]["password"]
with open("config.json", "r") as c:
	p = json.load(c)
	p = p["gui-config-path"]
	with open(p, "r") as s:
		j = json.load(s)
		j["configs"] = l
		with open(p, "w") as n_c:
			try:
				json.dump(j, n_c)
				print("写入成功")
			except:
				print("写入失败")
			