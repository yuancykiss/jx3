import re

import pymysql as pymysql
import requests

from lxml import etree


def get_page(url):
    """
    获取html页面
    :param url:
    :return:
    """
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        return html
    return None


def get_img(img_url, id):
    content = requests.get(img_url).content
    with open('/home/yuancy/workspace/media/jx3petimg/'+str(id)+'.jpg', 'wb')as f:
        f.write(content)


def pares_html(content):
    etree_html = etree.HTML(content)

    # id
    id = etree_html.xpath('//ol/li/a/@href')
    ids = [re.findall(r'.*?(\d+)$', item)[0] for item in id]

    # 名称
    names = etree_html.xpath('//ol//div/h3/span/text()')

    # 分类
    category = etree_html.xpath('//ol//div/h3//b/text()')
    categorys = [re.findall(r'\s\|\s(\S+)', item)[0] for item in category]

    # 图片
    images = []
    details = []
    image = etree_html.xpath('//li//div/img/@src')
    for index in range(len(image)):
        print('正在下载第%d张图片' % index)
        get_img(image[index], ids[index])
        images.append(str(ids[index]) + '.jpg')
        details.append('http://jx3yymj.com/index.php?mid=cw&document_srl='+ids[index])

    # 获取途径
    methods = etree_html.xpath('//table/tbody/tr/td[1]/text()')

    # 星级
    stars = etree_html.xpath('//table/tbody/tr/td[2]/text()')

    # 分数
    scores = etree_html.xpath('//table/tbody/tr/td[3]/text()')

    # 分享者
    shares = etree_html.xpath('//li//div[@class="info"]/span/b/a/text()')

    # 点击数
    views = etree_html.xpath('//li//div[@class="info"]/span/b/text()')

    return {'ids': ids, 'names': names, 'categorys': categorys, 'images': images, 'methods': methods, 'stars': stars, 'scores': scores, 'shares': shares, 'views': views, 'details':details}


def db_conn():
    """
    取数据库连接, 游标
    :return: db, cur
    """
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', charset='utf8', database='jx3')
    cur = db.cursor()
    return (db, cur)


def insert_to_database(cur, result):
    """
    写入数据到数据库
    :param cur:
    :param result:
    :return:
    """
    for index in range(len(result['ids'])):
        sql = 'insert into pets (id, name, category, image, method, stars, score, share, views, detail) values ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")' % (result['ids'][index],
                                                                                                                         result['names'][index],
                                                                                                                         result['categorys'][index],
                                                                                                                         result['images'][index],
                                                                                                                         result['methods'][index],
                                                                                                                         result['stars'][index],
                                                                                                                         result['scores'][index],
                                                                                                                         result['shares'][index],
                                                                                                                         result['views'][index],
                                                                                                                         result['details'][index])



        cur.execute(sql)
    print('加入%s条数据' % index)


def init_db(db, cur):
    """
    初始化：在每次爬取前，先清空数据库中的资历表
    :param db:
    :param cur:
    :return:
    """
    sql = 'truncate table zili'
    cur.execute(sql)
    db.commit()


def main():
    db, cur = db_conn()
    for index in range(1, 19):
        print('正在爬取第%d页' % index)
        html = get_page('http://jx3yymj.com/index.php?mid=cw&page=%d' % index)
        result = pares_html(html)
        insert_to_database(cur, result)
        db.commit()
    db.close()


if __name__ == '__main__':
    # url = 'http://jx3yymj.com/index.php?mid=bd'
    # url = 'http://jx3yymj.com/index.php?document_srl=629980&mid=bd'
    # url = 'http://jx3yymj.com/index.php?mid=cw&page=4'
    main()