import json
from urllib.parse import quote

import requests


def get_qiyu(daqu, server, qiyu_category, qiyu_name):
    # daqu = ''
    # server = ''
    # qiyu_category = ''
    # qiyu_name = ''

    url = 'https://jx3.derzh.com/serendipity/?m=1&test=1&R='+quote(daqu)+'&S='+server+'&t='+qiyu_category+'&s='+qiyu_name+'&n=&csrf='

    response = requests.get(url, verify=False)
    content = json.loads(response.text)
    return content['result']


if __name__ == '__main__':
    get_qiyu()
