from flask import Flask, request, render_template
import sqlite3
from time import *

app = Flask(__name__)

datas_dict = {}
datas = []
conn = sqlite3.connect('db.db')
cursor = conn.cursor()
sql = "select * from data"
data = cursor.execute(sql)

for i in data:
    datas.append(i)
    link = strftime("/%m/%d/")+f"{i[3]}.html"
    datas_dict[link] = [i[1], i[2], i[3], i[4]]
    # print(i)
print(datas_dict)


@app.route('/')
def index():
    datas = []
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    sql = "select * from data"
    data = cursor.execute(sql)
    for i in data:
        datas.append(i)
        print(i)
    cursor.close()
    conn.close()
    return render_template("index.html", datas=datas)


@app.route('/settings')
def settings():
    return render_template("settings.html")


@app.route('/index.html')
def index_():
    return render_template("index.html")

# links = request.path
# for i in datas_dict.keys():
@app.route(request.path)
def link():
    # print(request.path)
    # print(request.args.get('key', ''))
    # print(datas_dict['/05/12/测试页面.html'])
    return render_template("page.html")


if __name__ == '__main__':
    app.run(debug=True)
