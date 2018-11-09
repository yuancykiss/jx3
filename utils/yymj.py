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
        result = etree_html.xpath('//table//tr[' + str(i) + ']/td[2]/text()')
        if not result:
            result = etree_html.xpath('//table//tr[' + str(i) + ']/td[2]//span/text()')
            if not result:
                result = etree_html.xpath('//table//tr[' + str(i) + ']/td[2]/font/strong/text()')
        names.append(result)

        # 阵营
        result_war = etree_html.xpath('//table//tr[' + str(i) + ']/td[3]/img/@src')
        if not result_war:
            result_war = etree_html.xpath('//table//tr[' + str(i) + ']/td[3]/text()')
        for item in result_war:
            result_wars = re.findall(r'.*?(\w{2}).gif', item)
            if not result_wars:
                result_wars = ['中立']
            elif result_wars[0] == 'er':
                result_wars = ['恶人']
            else:
                result_wars = ['浩气']
            war.append(result_wars)

        # 门派
        result_menpai = etree_html.xpath('//table//tr[' + str(i) + ']/td[4]/img/@src')
        for item in result_menpai:
            result_menpais = re.findall(r'(\w{2}).gif', item)
            menpai.append(result_menpais)

        # 大区
        result_daqu = etree_html.xpath('//table//tr[' + str(i) + ']/td[5]/text()')
        if not result_daqu:
            result_daqu = etree_html.xpath('//table//tr[' + str(i) + ']/td[5]/strong/span/text()')
            if not result_daqu:
                result_daqu = etree_html.xpath('//table//tr[' + str(i) + ']/td[5]/font/strong/text()')
        daqu.append(result_daqu)

        # 服务器
        result_server = etree_html.xpath('//table//tr[' + str(i) + ']/td[6]/text()')
        if not result_server:
            result_server = etree_html.xpath('//table//tr[' + str(i) + ']/td[6]//span/text()')
            if not result_server:
                result_server = etree_html.xpath('//table//tr[' + str(i) + ']/td[6]//strong/text()')
        server.append(result_server)

        # 资历
        result_score = etree_html.xpath('//table//tr[' + str(i) + ']/td[7]/text()')
        if not result_score:
            result_score = etree_html.xpath('//table//tr[' + str(i) + ']/td[7]//span/text()')
        #     if not result_score:
        #         result_score = etree_html.xpath('//table//tr[' + str(i) + ']/td[6]//strong/text()')
        score.append(result_score)

    return menpai
    # return {'name': names, 'war': war, 'menpai': menpai, 'daqu': daqu, 'server': server, 'score': score}


def db_conn():
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', charset='utf8', database='jx3')

    return db


def insert_to_database(cur, result):

    for index in range(len(result['name'])):
        print(result['score'][index][0])
        sql = 'insert into zili (name, war, menpai, daqu, server, score) values ("%s", "%s", "%s", "%s", "%s", "%s")' % (result['name'][index][0],
                                                                                                                         result['war'][index][0],
                                                                                                                         result['menpai'][index][0],
                                                                                                                         result['daqu'][index][0],
                                                                                                                         result['server'][index][0],
                                                                                                                         result['score'][index][0])


        cur.execute(sql)
    print('加入%s条数据' % index)


def main():
    html = get_page(url)
    result = pares_html(html)
    print(result)
    # db = db_conn()
    # cur = db.cursor()
    # insert_to_database(cur, result)
    # db.commit()
    # db.close()


if __name__ == '__main__':
    url = 'http://jx3yymj.com/index.php?mid=bd'
    main()