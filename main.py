import time
from datetime import datetime as dt

hostPath = "/etc/hosts"
redirect = "127.0.0.1"
websiteList = ["https://vk.com/"]

while True:
    ymd = (dt.now().year, dt.now().month, dt.now().day)
    if dt(*ymd, 8) < dt.now() < dt(*ymd, 16):
        print("Rihanna")
        file = open(hostPath, "r+")
        content = file.read()
        for website in websiteList:
            if website in content:
                pass
            else:
                file.write(redirect + " " + website + "\n")
    else:
        file = open(hostPath, "r+")
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in websiteList):
                file.write(line)
            file.truncate()
        print("Drake")
    time.sleep(5)




