# -*- coding: utf-8 -*-

import socket,struct
import ipaddress
import re
import configparser



class FilteringSubnets():
	''' Алгоритм и часть кода взята отсюда: http://qaru.site/questions/76775/how-can-i-check-if-an-ip-is-in-a-network-in-python'''

	def __init__(self, proxies):
		self.proxies = list(proxies)
		self.subnets = []
		
		# with configparser.ConfigParser() as config:
		# 	config.read("settings.ini")
		# 	self.NAME = config["main"]["NAME"]
		config = configparser.ConfigParser()
		config.read("settings.ini")
		self.NAME = "\x1b[32m" + config["main"]["NAME"] + "\x1b[0m"
		del config
		
		with open("texts/subnets.txt", mode="r") as file:
			self.subnets = file.read().split("\n")
			for i in self.subnets:
				if (i == "") or (i == " ") or ("#" in i):  # удаление комментариев и пустых строк
					self.subnets.remove(i)
		print(self.NAME + "Фильтрование подсетей...")

	def start(self):
		for i in range(0, len(self.proxies)):
			self.proxies[i] = self.proxies[i].split(":")  # разделение на айпи и порт

		
		self.proxies = FilteringSubnets.addressInNetwork(self, self.proxies)  # удаление айпи, входящих в запрещенные подсети
		
		for i in range(0, len(self.proxies)):
			self.proxies[i] = self.proxies[i][0] + ":" + self.proxies[i][1]  # воссоединение айпи
		
		return self.proxies


	def addressInNetwork(self, proxylist):
		output = []
		for i in range(0, len(proxylist)):
			ifinsubnet = False
			for subnet in self.subnets:
				try:
					if ipaddress.ip_address(proxylist[i][0]) in ipaddress.ip_network(subnet):  # входит ли айпи в запрещенную подсеть
						print(self.NAME + "Удален айпи ({0}), входящий в запрещенную подсеть.".format(str(proxylist[i][0])))
						ifinsubnet = True
						break
					else:
						pass
				except ValueError:
					print(self.NAME + "Удален невалидный айпи ({0})".format(i[0]))
				except Exception as e:
					print(self.NAME + "Необработанная ошибка!")
				else:
					pass
			if not ifinsubnet:
				output.append(proxylist[i])

		return output
			


if __name__ == '__main__':
	start = FilteringSubnets(['103.79.169.153:4145', '54.38.81.12:45907', '127.0.0.1:228'])
	print(start.start())