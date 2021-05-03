Make suer you are install python3

usage:
WINDOWS:

INSTALL:

WINDOWS:
下載ZIP https://github.com/constantinedev/youtube-dlownload-by-readline/archive/refs/heads/main.zip <br>
解壓<br>
開始>cmd.exe><br>
先輸入 cd[空格] > 再拉個File去CMD > [enter]<br>
輸入: python run.py<br>

LINUX:
git clone https://github.com/constantinedev/youtube-dlownload-by-readline.git<br>
cd youtube-dlownload-by-readline<br>
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
並於links.txt確認URL<br>

Pyhton3 Windows下載<br>
https://www.python.org/ftp/python/3.9.4/python-3.9.4-amd64.exe
