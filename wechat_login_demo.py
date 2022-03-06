import base64
import xml.etree.ElementTree as ET

import requests


def wechat_login():
    app_id = 'wx398a330716af094a'
    app_secret = 'ae170d1592c60dafd4160462ef24405f'
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={0}&secret={1}'.format(app_id,
                                                                                                             app_secret)
    print("url=>", url)
    resp = requests.get(url)
    access_token = resp.json()['access_token']
    print(access_token)
    # my_scene_str = 'xxxxx'  # 场景码可以做个key放到redis里并设置一个和二维码一样的过期时间
    url = 'https://api.weixin.qq.com/cgi-bin/qrcode/create?access_token={0}'.format(access_token)
    data = {
        "expire_seconds": 604800,
        "action_name": "QR_STR_SCENE",
    }
    resp = requests.post(url, json=data)
    print("resp=>", resp)
    ticket = resp.json()['ticket']
    print("ticket=>", ticket)
    url = 'https://mp.weixin.qq.com/cgi-bin/showqrcode?ticket=' + ticket
    resp = requests.get(url)
    img = base64.b64encode(resp.content).decode('ascii')
    print(img)


def get_public_wx_status(request):
    root = ET.fromstring(request.data.decode('utf-8'))
    dic = {}
    for x in root:
        dic[x.tag] = x.text

    if dic.get('MsgType') == 'event':
        print("----------------------")
        if dic.get('Event') == 'subscribe':
            # parse_subscribe(dic)  # 新关注用户扫码
            print("new account")
        # if dic.get('Event') == 'SCAN':
        #     parse_scan(dic)  # 已经关注用户扫码


# wechat_login()
# while (True):
#     get_public_wx_status()
# print("--------------")
