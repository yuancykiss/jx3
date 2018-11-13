import json
import os
from urllib.parse import quote

import requests

daqu = '电信一区'
server = '长安城'
qiyu_category = '绝世奇遇'
qiyu_name = '阴阳两界'

url = 'https://jx3.derzh.com/serendipity/?m=1&test=1&R='+daqu+'&S='+server+'&t='+qiyu_category+'&s='+qiyu_name+'&n=&csrf='
response = requests.get(url, verify=False)
content = json.loads(response.text)
print(content['result'])

