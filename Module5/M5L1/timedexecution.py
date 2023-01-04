import schedule
import time
import webbrowser
import os

def exe():
    with open('motd.txt', 'r') as f:
        a = f.readline()
        print(a)

def open_browser():
    webbrowser.open('https://noroff.no', new=2)
    os.popen('start https://www.noroff.no')


schedule.every().day.at('08:00').do(exe)
schedule.every().hour.do(open_browser)


while True:
     schedule.run_pending()
     time.sleep(1)