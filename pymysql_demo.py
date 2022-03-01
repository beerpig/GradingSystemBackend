import hashlib

from DB_utils import POOL
import pymysql


def create_conn():
    conn = POOL.connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    return conn, cursor


def close_conn(conn, cursor):
    conn.close()
    cursor.close()


def select_all(sql, args):
    conn, cur = create_conn()
    cur.execute(sql, args)
    result = cur.fetchall()
    print(result)
    close_conn(conn, cur)
    return result


def select_token(sql, args):
    conn, cur = create_conn()
    cur.execute(sql, args)
    result = cur.fetchall()
    print('{} token: {}'.format(args, result))
    close_conn(conn, cur)
    return result


def token_insert(sql, args):
    conn, cur = create_conn()
    try:
        cur.execute(sql, args)
        conn.commit()
        close_conn(conn, cur)
        return True
    except Exception as e:
        print("token insert except", args)
        conn.rollback()
        close_conn(conn, cur)
        return False


def user_insert(sql, args):
    conn, cur = create_conn()
    try:
        result = cur.execute(sql, args)
        conn.commit()
        close_conn(conn, cur)
        return True
    except Exception as e:
        print("user insert except", args)
        conn.rollback()
        close_conn(conn, cur)
        return False


def select_user_login(sql, args):
    conn, cur = create_conn()
    try:
        result = cur.execute(sql, args)
        conn.commit()
        close_conn(conn, cur)
        return True if result != 0 else False
    except Exception as e:
        print("user select except", args)
        conn.rollback()
        close_conn(conn, cur)
        return False


def select_get_user(sql, args):
    conn, cur = create_conn()
    try:
        result = cur.execute(sql, args)
        conn.commit()
        close_conn(conn, cur)
        return True if result == 0 else False
    except Exception as e:
        print("user select except", args)
        conn.rollback()
        close_conn(conn, cur)
        return False


def encode_(str):
    MD5 = hashlib.md5()
    MD5.update(str.encode(encoding='utf-8'))
    print("加密后：", MD5.hexdigest())
    return MD5.hexdigest()


# sql = "select * from user where userName=%s "
# q = "🍺🐷"
# res = select_all(sql, q)
# print(res)
def update_token(sql, args):
    conn, cur = create_conn()
    try:
        cur.execute(sql, args)
        conn.commit()
        close_conn(conn, cur)
        return True
    except Exception as e:
        print("user_token update except", args)
        conn.rollback()
        close_conn(conn, cur)
        return False
