#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


# User-Agant代理池
class MyUserAgentMiddleware(object):
    def __init__(self, user_agent_list):
        self.user_agent_list = user_agent_list

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.get('USER_AGENT_LIST'))

    def process_request(self, request, spider):
        request.headers['User-Agent'] = random.choice(self.user_agent_list)


# ip代理池
class MyIPProxyMiddleware(object):
    def __init__(self, ip_proxy_list):
        self.ip_proxy_list = ip_proxy_list

    @classmethod
    def from_crawler(cls, crawler):
        with open('conf/ip_proxy.list', 'r', buffering=1024, encoding='utf-8') as f:
            ip_proxy_list = f.readlines()
            return cls(ip_proxy_list)

    def process_request(self, request, spider):
        request.meta['proxy'] = 'http://' + random.choice(self.ip_proxy_list)

