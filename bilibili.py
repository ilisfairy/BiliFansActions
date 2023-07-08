#!/usr/bin/env python
# coding=utf-8
import datetime
import requests
import sys

uid = sys.argv[1]

header = {
        'Host': ' api.bilibili.com ',
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A037U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
}
url = f' https://api.bilibili.com/x/relation/stat?vmid={uid} '
resp = requests.get(url, headers=header)
json_data = resp.json()
data = json_data['data']
follower_cnt = data['follower']

date =  datetime.datetime.now ().strftime('%Y-%m-%d')
line = f'{date},{follower_cnt}'
print(line)