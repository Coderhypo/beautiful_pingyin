#!/usr/bin/env python
# coding=utf-8

from flask import request, abort
import xml.etree.ElementTree as ET
import hashlib

from app import app, TOKEN

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        if request.args.get('timestamp') == None:
            return abort(403)
        timestamp = request.args.get('timestamp')
        nonce = request.args.get('nonce')
        echostr = request.args.get('echostr')
        token = TOKEN
        li = [token, timestamp, nonce]
        li.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, li)
        hashcode = sha1.hexdigest()
        if hashcode == request.args.get('signature'):
            return echostr
        else:
            return abort(403)
    elif request.method == 'POST':
        message = request.data  # 接收用户消息
        root = ET.fromstring(message)  # 解析xml
        to_user_name = root.findall('ToUserName')[0].text  # 开发者账号
        from_user_name = root.findall('FromUserName')[0].text  # 用户微信id
        create_time = root.findall('CreateTime')[0].text  # 消息创建时间 （整型）
        message_type = root.findall('MsgType')[0].text # 消息类型text
        try:
            content = root.findall('Content')[0].text # 消息内容
        except:
            content = ''
        try:
            message_id = root.findall('MsgId')[0].text # 消息的ID
        except:
            message_id = ''
        try:
            event  = root.findall('Event')[0].text # 事件类型
        except:
            event = ''
        try:
            event_key = root.findall('EventKey')[0].text or ''  # 事件Key值
        except:
            event_key = ''

        if event == 'CLICK':
            if event_key == 'HISTORY': # 历史传说
                return text % (from_user_name, to_user_name, create_time, u"历史传说模块正在开发中……")
            elif event_key == 'CULTURAL': # 文物古迹
                return text % (from_user_name, to_user_name, create_time,  u"文物古迹模块正在开发中……")
            elif event_key == 'FOOD': # 饮食小吃
                return text % (from_user_name, to_user_name, create_time,  u"饮食小吃模块正在开发中……")
            elif event_key == 'NEWS': # 时事新闻
                return text % (from_user_name, to_user_name, create_time,  u"时事新闻模块正在开发中……")
            elif event_key == 'HEALTHY': # 健康养生
                return text % (from_user_name, to_user_name, create_time,  u"健康养生模块正在开发中……")

        return info % (from_user_name, to_user_name, create_time, u"梦续代码",content , "http://www.ihypo.net")


info = """
<xml>
<ToUserName><![CDATA[%s]]></ToUserName>
<FromUserName><![CDATA[%s]]></FromUserName>
<CreateTime>%s</CreateTime>
<MsgType><![CDATA[news]]></MsgType>
<ArticleCount>1</ArticleCount>
<Articles>
<item>
<Title><![CDATA[%s]]></Title>
<Description><![CDATA[%s]]></Description>
<Url><![CDATA[%s]]></Url>
</item>
</xml>
"""

text="""
<xml>
<ToUserName><![CDATA[%s]]></ToUserName>
<FromUserName><![CDATA[%s]]></FromUserName>
<CreateTime>%s</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[%s]]></Content>
</xml>
"""
