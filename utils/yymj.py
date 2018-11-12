import re

import pymysql as pymysql
import requests

from lxml import etree


def get_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        return html
    return None


def to_menpai(menpai):
    if menpai == 'qx':
        return '七秀'
    elif menpai == 'wh':
        return '万花'
    elif menpai == 'cy':
        return '纯阳'
    elif menpai == 'tc':
        return '天策'
    elif menpai == 'sl':
        return '少林'
    elif menpai == 'wd':
        return '五毒'
    elif menpai == 'cj':
        return '藏剑'
    elif menpai == 'tm':
        return '唐门'
    elif menpai == 'mj':
        return '明教'
    elif menpai == 'gb':
        return '丐帮'
    elif menpai == 'cy2':
        return '苍云'
    elif menpai == 'cg':
        return '长歌'
    elif menpai == 'bd':
        return '霸刀'
    elif menpai == 'bl':
        return '蓬莱'


def pares_html(content):
    etree_html = etree.HTML(content)
    names = []
    war = []
    menpai = []
    daqu = []
    server = []
    score = []
    for i in range(2, 202):
        # id
        result_name = etree_html.xpath('//table//tr[' + str(i) + ']/td[2]//text()')[0].strip()
        names.append(result_name)

        # 阵营
        try:
            result_war = etree_html.xpath('//table//tr[' + str(i) + ']/td[3]/img/@src')[0][-6:-4]
            if result_war == 'er':
                result_war = '恶人谷'
            else:
                result_war = '浩气盟'
        except IndexError:
            result_war = '中立'
        war.append(result_war)

        # 门派
        result_menpai = re.findall(r'm_(\w+)\.gif', etree_html.xpath('//table//tr[' + str(i) + ']/td[4]/img/@src')[0])[0]
        menpai.append(to_menpai(result_menpai))

        # 大区
        result_daqu = etree_html.xpath('//table//tr[' + str(i) + ']/td[5]//text()')[0].strip()
        daqu.append(result_daqu)

        # 服务器
        result_server = etree_html.xpath('//table//tr[' + str(i) + ']/td[6]//text()')[0].strip()
        server.append(result_server)

        # 资历
        result_score = etree_html.xpath('//table//tr[' + str(i) + ']/td[7]//text()')[0].strip()
        score.append(result_score)

    # print(menpai)
    return {'name': names, 'war': war, 'menpai': menpai, 'daqu': daqu, 'server': server, 'score': score}


def db_conn():
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', charset='utf8', database='jx3')

    return db


def insert_to_database(cur, result):

    for index in range(len(result['name'])):
        sql = 'insert into zili (name, war, menpai, daqu, server, score) values ("%s", "%s", "%s", "%s", "%s", "%s")' % (result['name'][index],
                                                                                                                         result['war'][index],
                                                                                                                         result['menpai'][index],
                                                                                                                         result['daqu'][index],
                                                                                                                         result['server'][index],
                                                                                                                         result['score'][index])


        cur.execute(sql)
    print('加入%s条数据' % index)


def init_db(db, cur):
    sql = 'truncate table zili'
    cur.execute(sql)
    db.commit()


def main():
    html = get_page(url)
    result = pares_html(html)
    db = db_conn()
    cur = db.cursor()

    init_db(db, cur)

    insert_to_database(cur, result)
    db.commit()
    db.close()


if __name__ == '__main__':
    # url = 'http://jx3yymj.com/index.php?mid=bd'
    url = 'http://jx3yymj.com/index.php?document_srl=629980&mid=bd'
    main()