from flask import Flask, request, render_template
import sqlite3
# from time import *

app = Flask(__name__)

datas_dict = {}
datas = []
conn = sqlite3.connect('db.db')
cursor = conn.cursor()
sql = "select * from data"
data = cursor.execute(sql)


for i in data:
    datas.append(i)
    datas_dict[int(i[0])] = [i[1], i[2], i[3], i[4]]
# print(datas_dict)
# print(datas[0][2])

@app.route('/')
@app.route('/index.html')
def index():
    # datas = []
    # conn = sqlite3.connect('db.db')
    # cursor = conn.cursor()
    # sql = "select * from data"
    # data = cursor.execute(sql)
    # for i in data:
    #     datas.append(i)
    #     print(i)
    # cursor.close()
    # conn.close()
    # print(datas[0])
    len_ = {}
    # print(datas)
    for i in range(len(datas)):
        # len_.append(i)
        # print(datas[0])
        # print(f"{}")
        # print(datas[0][i+1])
        # print(datas[i][2])
        len_[datas[i][2]] = len(datas[i][2]) // 3
    print(len_)    
    
    return render_template("index.html", datas=datas, len_ = len_)


@app.route('/settings')
def settings():
    return render_template("settings.html")


@app.route("/post/<int:postid>")
def post(postid):
    # print(datas_dict[postid][1])
    datas = datas_dict[postid]
    # datas = [x.replace('\n', '"<br>"') for x in datas if x.strip() != '\n']
    content = [x.split('\n') for x in datas if x.strip() != '\n']
    # print(content)
    return render_template('page.html', datas=datas, content=content[1])


if __name__ == '__main__':
    app.run(debug=True)
