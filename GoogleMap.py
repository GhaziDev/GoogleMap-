#! python
import sys,webbrowser,pyperclip
sys.argv
if((len(sys.argv))>1):
   adress=' '.join(sys.argv[1:])
else:
    adress=pyperclip.paste()
webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://www.google.com/maps/place/"+adress)
