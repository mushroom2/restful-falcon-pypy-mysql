import mysql.connector
from mysql.connector import Error


def connect():
    """ Connect to MySQL database """
    conn = mysql.connector.connect(host='localhost', database='test', user='mushroom', password='123333')
    cur = conn.cursor()
    cur.execute('SET NAMES `utf8`')
    cur.execute('SELECT `name` FROM `city` ORDER BY `name` DESC')
    result = cur.fetchall()
    for row in result:
        print row[0]

if __name__ == '__main__':
    connect()
