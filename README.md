# ss-subscribe
Python3编写的ss订阅脚本

## 截图

![](https://github.com/Fndroid/ss-subscribe/blob/master/imgs/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20180304114651.png?raw=true)

## 项目组成
- ss-subscribe.py (脚本主文件)
- ss-subscribe.json (脚本配置文件)

## 依赖
- Python3
- base64
- json
- re
- requests
- urllib

## 如何使用

### 1. 将ss-subscrib.py和ss-subscrib.json拷贝至shadowsocks文件夹下
### 2. 在ss-subscribe.json文件中加入要订阅服务器的URL
```json
{
 "servers": [{
   "url": "https://raw.githubusercontent.com/Fndroid/ss-subscribe/master/test/subscrib-data"
  },{
   "url": "你的订阅地址"
  }]
}
```
### 3. 在shadowsocks目录下,打开cmd,执行以下命令
```bash
python3 ss-subscribe.py
```
### 4. 重启shadowsocks
