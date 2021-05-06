import subprocess
import threading

file_name = 'links1.txt'
order = 'youtube-dl --write-description --write-info-json --write-annotations --write-sub --write-thumbnail '
source = open(file_name, 'r')
outputdir = '' #<--Input Download location here
output = ' -o ' + outputdir
lastIndex = 0
lines = source.readlines()
lineCount = len(lines)
def worker():
	global lastIndex
	global lines
	global lineCount
	while lastIndex < lineCount:
		lastIndex +=1
		line = lines[lastIndex-1]
		subprocess.call([order + line.strip() + output], shell=True)

threads = [threading.Thread(target=worker) for _i in range(300)]
for thread in threads:
	thread.start()
source.close()
