import subprocess

file_name = 'links.txt'
order = 'youtube-dl --write-description --write-info-json --write-annotations --write-sub --write-thumbnail '
source = open(file_name, 'r')
for line in source:
	subprocess.call([order + line.strap()], shell=True)
source.close()
