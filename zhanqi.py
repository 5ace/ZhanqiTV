#!/usr/bin/python3
#author = 'zeek'

import urllib.request
import urllib.parse
import mylog
import json
import time

ZHANQI_URL  = 'http://www.zhanqi.tv'
CAPTCHA_URL = '/api/auth/user.captcha'
LOGIN_URL   = '/api/auth/user.login'

opener = urllib.request.build_opener()
opener.addheaders = [('appVersion', '2.5.9'),
                     ('User-Agent', 'Zhanqi.tv Api Client'),
                     ('imei', '8pngm9/Rg6iTnGOrp6uqp2KqnZenoZpflvM'),
                     ('Content-Type', 'application/x-www-form-urlencoded'),
                     ('charset', 'utf-8')]

def getCaptcha():
    with urllib.request.urlopen(ZHANQI_URL + CAPTCHA_URL) as f:
        captchaJson = f.read().decode('utf-8')
        mylog.writeLog('get', captchaJson)
        captchaDict = json.loads(captchaJson)
        #mylog.writeLog('info', captchaDict)
        captchaImg = captchaDict['data']['img']
        captchaKey = captchaDict['data']['captchaKey']
        mylog.writeLog('img', captchaImg)
        print(captchaImg)
        return captchaKey

def login(captchaKey):
    captcha = input('captcha:')
    params = urllib.parse.urlencode({'captcha': captcha, 'password': 'fuckyou', 'account': 'zephyrzoom', 'captchaKey': captchaKey})
    mylog.writeLog('post', ZHANQI_URL + LOGIN_URL + '?' + params)
    urllib.request.install_opener(opener)
    with urllib.request.urlopen(ZHANQI_URL + LOGIN_URL + '?' + params) as f:
        loginInfo = f.read().decode('utf-8')
        mylog.writeLog('login', loginInfo)

def main():
    captchaKey = getCaptcha()
    login(captchaKey)

if __name__ == '__main__':
    main()
