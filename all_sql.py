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
        page_class text
        )
    '''
    cursor.execute(sql)
    conn.commit()

    cursor.close()
    conn.close()

def insert_data(title,content,date,top,page_class):
    conn = sqlite3.connect("db.db")
    cursor = conn.cursor()
    sql = f'''
        insert into data (
            title,content,date,top,page_class
        )
        values (
            '{title}','{content}','{date}','{top}','{page_class}'
        )
    '''
    cursor.execute(sql)
    conn.commit()

    cursor.close()
    conn.close()

# init_db()

title = "xxxxx"
content = '''
xxxxx
xxxxxxx
xxxxxxxx
'''
date = strftime("%m-%d %H:%M:%S")
page_class = "随笔与个人文集"
top = "xxxxx"


insert_data(title,content,date,top,page_class)