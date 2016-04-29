#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import json
from websocket import create_connection

class Notify:
    def __init__(self, token='', channel=''):
        self.token = token
        self.channel = channel
        self.id=1
        self.layout = lambda _t: json.dumps({"id": self.id, "type": "message", "channel": self.channel, "text": _t})
        self.ws = None
        self.connect()

    def connect(self):
        if self.token=='' or self.channel =='':
            raise ValueError('Both token and channel should be specified!')
        else:
            _url = json.loads(urllib2.build_opener().open(urllib2.Request('https://slack.com/api/rtm.start?token=%s' % self.token)).read())['url']
            self.ws = create_connection(_url)

    def write(self, text):
        try:
            return self.ws.send(self.layout(text))
        except Exception as e:
            self.connect()
            return self.ws.send(self.layout(text))
        finally:
            self.id += 1

    def read(self):
        return self.ws.recv()

    def close(self):
        self.ws.close()

