import sqlite3
from time import *

def init_db():
    conn = sqlite3.connect("db.db")
    cursor = conn.cursor()

    sql = '''
        create table data(
        id integer primary key autoincrement, 
        title varchar,
        content text,
        date text,
        top text,
        link text
        )
    '''
    cursor.execute(sql)
    conn.commit()

    cursor.close()
    conn.close()

def insert_data(title,content,date,top,link):
    conn = sqlite3.connect("db.db")
    cursor = conn.cursor()
    sql = f'''
        insert into data (
            title,content,date,top,link
        )
        values (
            '{title}','{content}','{date}','{top}','{link}'
        )
    '''
    cursor.execute(sql)
    conn.commit()

    cursor.close()
    conn.close()

# init_db()

title = "测试页面"
content = '''
这是一个测试页面
很高兴你可以来这个页面逛逛
一个刚刚起步的Flask博客
再次感谢
'''
date = strftime("%m-%d %H:%M:%S")
top = "Top"
link = strftime("/%m/%d/")+f"{title}.html"

insert_data(title,content,date,top,link)