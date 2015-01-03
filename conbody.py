#!/usr/bin/python
#coding: utf8
import RPi.GPIO as GPIO #调入GPIO库
import time #调入时间库
import os
from weixin import WeiXinClient
from weixin import APIError
from weixin import AccessTokenError


BODYPORT=12
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(BODYPORT,GPIO.IN) 

my_appid = ''
my_secret = ''


if __name__ == '__main__':
    wc = WeiXinClient(my_appid, my_secret, fc=True, path='/tmp')
    
    wc.request_access_token()
    rjson = wc.user.get._get(next_openid=None)
    count = rjson.count
    id_list = rjson.data.openid
    while count < rjson.total:
        rjson = wc.user.get._get(next_openid=rjson.next_openid)
        count += rjson.count
        id_list.extend(rjson.openid)
    # 最后看看都有哪些用户
    print id_list

    while True:
        inputValue = GPIO.input(BODYPORT)
        if(inputValue!=0):
            #截图
            os.system('fswebcam -d /dev/video0 -r 640x480 /tmp/snapshot.png')
            #发送报警文字
            for uid in id_list:
                content = '{"touser":"%s", "msgtype":"text", "text":{ "content":"Warning!"}}' %uid
                #print 可以看有没有发送成功, 可以捕获api错误异常
                try:
                    print wc.message.custom.send.post(body=content)
                except APIError, e:
                    print e, uid

            #发送报警画面
            rjson = wc.media.upload.file(type='image', pic=open('/tmp/snapshot.png', 'rb'))
            print rjson
            # 把上传的图片发出去
            for uid in id_list:
                content = '{"touser":"%s", "msgtype":"image", ' \
                    '"image":{ "media_id":"%s"}}' % (uid, rjson.media_id)
                try:
                    print wc.message.custom.send.post(body=content)
                except APIError, e:
                    print e, uid


        time.sleep(5.0)
        
