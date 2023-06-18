# 开发时间：2023/6/18  20:43
# @authored by Jam

import requests

url = "https://10.254.241.3/webauth.do?&wlanacname=SC-CD-XXGCDX-SR8810-X"

data = {
    "loginType":"",
    "auth_type":"0",
    "isBindMac1":"0",
    "pageid":"1",
    "templatetype":"1",
    "listbindmac":"0",
    "recordmac":"0",
    "isRemind":"1",
    "loginTimes":"",
    "groupId":"",
    "distoken":"",
    "echostr":"",
    "url":"",
    "isautoauth":"",
    "notice_pic_loop2":"/portal/uploads/pc/demo2/images/bj.png",
    "notice_pic_loop1":"/portal/uploads/pc/demo2/images/logo.png",
    "userId":"",    #add your studentID here
    "passwd":"",    #add your password here
    "remInfo":"on"
}

header = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control":"max-age=0",
    "Connection":"keep-alive",
    "Content-Length":"336",
    "Content-Type":"application/x-www-form-urlencoded",
    "Cookie":"softrand=2c311a061511d1834501f3ad293d02b41dd46309c2f028fa82e3e9514e198ba2; JSESSIONID=90C8C8F980F9BB2396B98199A2D3BA21; portalUserCookie=ac5a1d00b4785b690d29dd70b047c9cc72d68c66794641b073928d9804466344452ae09f419da88c5c046bee0f0f82cf; remeberMeCookie=ac5a1d00b4785b690d29dd70b047c9cc72d68c66794641b097f8d686bca12a7d152c1f59168064940a106551c147f51b",
    "Host":"10.254.241.3",
    "Origin":"https://10.254.241.3",
    "Referer":"https://10.254.241.3/webauth.do?&wlanacname=SC-CD-XXGCDX-SR8810-X",
    "Sec-Fetch-Dest":"document",
    "Sec-Fetch-Mode":"navigate",
    "Sec-Fetch-Site":"same-origin",
    "Sec-Fetch-User":"?1",
    "Upgrade-Insecure-Requests":"1",
    #注意你使用认证的浏览器
    #edge：
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edg/114.0.1823.51",
    #chrome：
    #"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 ",
    #Safari
    #"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36",
    "sec-ch-ua-mobile":"?0",
    "sec-ch-ua-platform":"Windows"
}

response = requests.post(url, data, headers=header, verify=False).status_code

print("回应代码{}".format(response))
