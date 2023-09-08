# -*- coding: utf-8 -*-
# @FileName    : main.py.py
# @Author  : LQYHYQ
# @Time    : 2023/9/8 11:37

import random
import requests
import json
import configparser


config = configparser.ConfigParser()
config.read("config.ini")


# 使用pushplus服务推送
def pushplus(content):
    api_url = "http://www.pushplus.plus/send/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "Content-Type": "application/json",
    }
    token = config.get("pushplus", "token")
    data = {
        "token": token,
        "title": "ZeppLife刷步执行通知",
        "content": content,
        "channel": "wechat",
        "template": "html"
    }
    body = json.dumps(data).encode(encoding='utf-8')
    response = requests.post(api_url, headers=headers, data=body)
    print(response.text)
    response.close()


def main():
    # ZeppLife账号
    user = config.get("zepplife", "user")
    # ZeppLife密码
    password = config.get("zepplife", "password")
    # 最小步数
    min_step = config.get("step", "min_step")
    # 最大步数
    max_step = config.get("step", "max_step")

    # 步数取 min_step 至 max_step 随机数。
    step = random.randint(min_step, max_step)

    base_url = "https://apis.jxcxin.cn/api/mi?"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'host': 'apis.jxcxin.cn',
        'Accept': '*/*',
    }
    data = {
        "user": user,
        "password": password,
        'step': step,
    }
    response = requests.post(base_url, headers=headers, data=data)
    if response.status_code == 200:
        pushplus(response.text)
    else:
        pushplus(response.status_code)
        response = requests.post(base_url, data=data)
        pushplus(response.text)
    response.close()


if __name__ == '__main__':
    main()
