# -*- coding: utf-8 -*-
# @FileName    : main.py.py
# @Author  : LQYHYQ
# @Time    : 2023/9/8 11:37

import random
import requests
import json
import configparser
import os


config = configparser.ConfigParser()
config.read(os.path.join(os.getcwd(), "config.ini"))


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
        "template": "json"
    }
    body = json.dumps(data).encode(encoding='utf-8')
    requests.post(api_url, headers=headers, data=body)


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
    step = random.randint(int(min_step), int(max_step))

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
        if response.text == "数据库连接失败：SQLSTATE[HY000] [1040] Too many connections":
            response2 = requests.post(base_url, headers=headers, data=data)
            pushplus("第二次请求：{}".format(response2.text))
    else:
        pushplus(response)
        response = requests.post(base_url, data=data)
        pushplus(response.text)
    response.close()


if __name__ == '__main__':
    main()
