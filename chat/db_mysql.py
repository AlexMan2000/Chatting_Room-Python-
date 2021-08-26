import pymysql

def db1():
    config = {
        "host": "182.92.205.131",
        "user": "root",  # 账号
        "password": "1122qq",  # 密码
        "database": "chat",
        "charset": "utf8"
    }
    return pymysql.connect(**config)



def stopdb(db):
    """
    :return: 关闭db
    """
    db.commit()
    db.close()


def runsql(db, sql):
    """
    :return: 运行完数据库
    """
    sql = sql.replace("\\", "\\\\")
    cursor = db.cursor()
    cursor.execute(sql)
    data1 = cursor.fetchall()
    cursor.close()
    return data1


def safe_runsql(db, sql, *safedata):
    """
    :return: 运行完数据库
    """
    sql = sql.replace("\\", "\\\\")
    cursor = db.cursor()
    cursor.execute(sql, safedata)
    data1 = cursor.fetchall()
    cursor.close()
    return data1


def safe_runsql_json(db, sql, *safedata):
    """
    :return: 运行完数据库
    """
    # sql = sql.replace("\\", "\\\\")
    # print(sql)
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, safedata)
    data1 = cursor.fetchall()
    cursor.close()
    return data1


def runsql_json(db, sql):
    """
    :return: 运行完数据库并返回json格式
    """
    sql = sql.replace("\\", "\\\\")
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql)
    data1 = cursor.fetchall()
    cursor.close()
    return data1


def wirtesql(db, sql, *wirte):
    """
    :return: 写入数据库
    """
    cursor = db.cursor()
    cursor.execute(sql, wirte)
    data1 = cursor.fetchall()
    cursor.close()
    return data1