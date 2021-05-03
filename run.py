import os, sys, subprocess

file_name = 'links.txt'
order = 'youtube-dl --write-description --write-info-json --write-annotations --write-sub --write-thumbnail '
with open(file_name) as fp:
	line = fp.readline()
	cnt = 1
	while line:
		turl = line.strip()
		##proc = subprocess.Popen('cmd.exe', stdin=subprocess.PIPE, stdout = subprocess.PIPE)
		##stdout, stderr = proc.communicate(order + turl)
		subprocess.call([order + turl], shell=True)
