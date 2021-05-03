Make suer you are install python3

usage:
WINDOWS:

INSTALL:

git clone <br>
chmod +x run.py<br>
python3 -m pip install -U pip<br>
python3 -m pip install youtube-dl<br>

USAGE:

check the [links.txt] file as the youtube url are your order<br>
and start the following command in Terminal<br>

python3 run.py

原生run.py為Linux及Mac OSX而設<br>
如果想係Windwos執行當中第10及11行可以剛除##號即何<br>
並在subprocess.call前加入回##號<br>

如果需要播夜清單下載請自行於第4行改為<br>
order = 'youtube-dl -F '<br>
並於links.txt確認URL
