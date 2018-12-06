import pymysql

data = [['长安城', '龙争虎斗', '白帝城', '蝶恋花', '红尘寻梦', '情深似海'],
        ['梦江南', '唯我独尊', '乾坤一掷', '斗转星移', '幽月轮', '剑胆琴心', '金榜题名', '平步青云'],
        ['亢龙有悔', '绝代天骄', '风骨霸刀', '战无不胜'],
        ['天鹅坪', '破阵子', '飞鸢泛月', '双剑合璧', '雪絮金屏', '鹏程万里', '长风破晓'],
        ['李忘生', '飞龙在天'],
        ['千古风流', '大美江湖', '碧海青天', '锦绣山河'],
        ['百无禁忌'],
        ['止戈为武']
        ]

daqus = ['电信一区', '电信五区', '电信八区', '双线一区', '双线二区', '双线三区', '电信PVP搞事区', '双线PVP搞事区']


def connect():
    """
    链接数据库
    :return:db, cursor
    """
    port = 3306,
    host = '127.0.0.1'
    password = '123456'
    database = 'jx3'
    user = 'root'
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', database='jx3')

    cur = db.cursor()
    return (db, cur)


def insert_daqu():
    i = 0
    for item in daqus:
        i += 1
        sql = 'insert into jx3_daqu values("%d", "%s")' % (i, item)
        cur.execute(sql)


def insert_server():
    daqu_id = 0
    server_id = 0
    for servers in data:
        daqu_id += 1
        for server in servers:
            server_id += 1
            sql = 'insert into jx3_server (id, name) values("%d", "%s")' % (server_id, server)
            cur.execute(sql)


if __name__ == '__main__':
    db, cur = connect()
    # insert_daqu()
    # insert_server()
    db.commit()
    db.close()
    print('success')

