# ZeppLifeShuabu
## 项目弃用
2024年1月31日更新，API Store的API已停用，本项目弃用。

## 介绍
借助 [API Store](https://apis.jxcxin.cn/) 的 [微信运动刷步](https://apis.jxcxin.cn/doc/mi.html) API，通过ZeppLife(原小米运动)账号刷步，可同步至微信、支付宝。  
API返回结果通过 [pushplus](http://www.pushplus.plus/) 推送回微信。  

:moneybag: 如果你嫌麻烦或者看不懂以下的步骤，直接查看最后的 [最简易版本](#最简易版本) 手动操作。

## 使用
修改 `config.ini` 文件，填写好ZeppLife账号、密码，要刷的步数区间（程序将在区间中取随机值），以及pushplus的token。
+ `zepplife.user`：ZeppLife账号，最好用邮箱注册的，小米账号不行
+ `zepplife.password`：ZeppLife密码
+ `step.min_step`：步数区间最小值
+ `step.max_step`：步数区间最大值
+ `pushplus.token`：pushplus的token，前往 pushplus官网 微信登陆获取

执行 `main.py` 文件，等待微信通知。

## 效果
通过pushplus公众号查看通知

![image](https://github.com/LQYHYQ/ZeppLifeShuabu/assets/38932132/46d9f357-177e-4c4d-ae93-7327e9fa3bf2)

通知详情

![image](https://github.com/LQYHYQ/ZeppLifeShuabu/assets/38932132/108c573b-bd69-482a-840d-cac914468434)

## 最简易版本
浏览器打开 [API Store](https://apis.jxcxin.cn/) 的 [微信运动刷步](https://apis.jxcxin.cn/doc/mi.html) ，找到 `在线测试工具` ，在下面填写账号、密码、步数，然后点击上面发起请求，查看下方返回结果是否请求成功，完事！
![image](https://github.com/LQYHYQ/ZeppLifeShuabu/assets/38932132/90e3e4de-55f9-409f-a164-add355239b93)

