import os, sys, subprocess

file_name = 'links.txt'
order = 'youtube-dl --write-description --write-info-json --write-annotations --write-sub --write-thumbnail '
with open(file_name) as fp:
	line = fp.readline()
	cnt = 1
	while line:
		turl = line.strip()
		subprocess.call([order + turl], shell=True)
