#!/usr/bin/env python
# -*- coding: utf-8 -*-

MAIN="BlackWidow"
AUTHOR="BeyazHacker.com"

import os

if (os.path.exists("/usr/share/set/modules/BlackWidow") == True):
	domain = raw_input ("Domain Girin(beyazhacker.com): ")
	os.system("cd /usr/share/set/modules/BlackWidow/ && python blackwidow -d " + domain)
	

elif (os.path.exists("/usr/share/set/modules/BlackWidow") == False):
	os.system("git clone https://github.com/1N3/BlackWidow.git")
	os.system("cp -r BlackWidow/ /usr/share/set/modules/")
	os.system("cd /usr/share/set/modules/BlackWidow/ && bash install.sh")
	os.system("clear")
	domain = raw_input ("Domain Girin(beyazhacker.com): ")
	os.system("cd /usr/share/set/modules/BlackWidow/ && python blackwidow -d " + domain)
