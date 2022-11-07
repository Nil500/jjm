import platform
import os
os.system('termux-setup-storage')
os.system('rm -rf Test780')
os.system('git pull')
try:os.mkdir('/sdcard/OK')
except:pass
try:os.mkdir('/sdcard/CP')
except:pass
try:os.system('touch .proxy.txt')
except:pass
arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("latter")._site_view_()
elif 'aarch' in arc:
	__import__ Test780.py()
else:
	exit(f' Unknow device machine {arc}')
 
