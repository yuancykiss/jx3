import http.client
import json
import logging
import random
from urllib.error import URLError
from urllib.parse import urlencode

SMS_ACCOUNT = 'C27997383'
SMS_PASSWORD = '36f65296d7bd78e1b59afcea033bd33e'
MSG_TEMPLATE = '您的验证码是：%s。请不要把验证码泄露给其他人。'
SMS_SERVER = '106.ihuyi.com'
SMS_URL = '/webservice/sms.php?method=Submit'
def send_short_message(tel, code):
    """发送短信"""
    params = urlencode({
        'account': SMS_ACCOUNT,
        'password': SMS_PASSWORD,
        'content': MSG_TEMPLATE % code,
        'mobile': tel,
        'format': 'json'
    })
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/plain'
    }
    conn = http.client.HTTPConnection(SMS_SERVER, port=80, timeout=10)
    try:
        conn.request('POST', SMS_URL, params, headers)
        json_str = conn.getresponse().read().decode('utf-8')
        return json.loads(json_str)
    except URLError or KeyError as e:
        logging.error(e)
        return json.dumps({
            'code': 500,
            'msg': '短信服务暂时无法使用'
        })
    finally:
        conn.close()


def get_code(lenth=6):
    return random.randint(lenth*lenth**10, lenth*lenth**11-1)


if __name__ == '__main__':
    code = str(get_code(5))
    tel = 13219031865
    send_short_message(tel, code)
