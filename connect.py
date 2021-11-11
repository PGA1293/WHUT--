import requests
import base64


# 检查是否有网
def isNetConnected():
    response = requests.get(url='http://www.baidu.com')
    if 'STATUS OK' in response.text:
        return True
    else:
        return False


# 连接校园网
def Connect(username, password):
    b64password = base64.b64encode(password.encode()).decode('utf-8')
    url = 'http://172.30.16.34/srun_portal_pc.php'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
        'Host': '172.30.16.34'
    }
    data = {
        'action': 'login',
        'ac_id': 5,
        'ajax': 1,
        'username': username,
        'password': '{B}' + b64password
    }
    # requests.post(url=url, headers=headers, data=data)
    # 想静默联网就把上一行取消注释，下面5行和最后4行注释掉或者去掉
    response = requests.post(url=url, headers=headers, data=data)
    if 'login_ok' in response.text:
        print('连接成功')
    else:
        print('连接失败，请检查')


# 在username和password中分别填入校园卡号和密码
if __name__ == '__main__':
    username = ''
    password = ''
    if not isNetConnected():
        Connect(username, password)
    else:
        print('已联网，无需重复连接')
