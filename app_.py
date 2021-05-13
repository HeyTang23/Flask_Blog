from flask import Flask, request, render_template
import sqlite3


app = Flask(__name__)

datas_dict = {}
datas = []
conn = sqlite3.connect('db.db')
cursor = conn.cursor()
sql = "select * from data"
data = cursor.execute(sql)


for i in data:
    datas.append(i)
    datas_dict[int(i[0])] = [i[1], i[2], i[3], i[4], i[5]]

divs = ['/', 'index.html', '/settings', "/post/<int:postid>"]


@app.route('/')
@app.route('/index.html')
def index():
    len_ = {}
    for i in range(len(datas)):
        len_[datas[i][2]] = len(datas[i][2]) // 3
        if len_[datas[i][2]] > 20:
            len_[datas[i][2]] = len(datas[i][2]) // 3
        else:
            len_[datas[i][2]] = -1
    return render_template("index.html", datas=datas, len_=len_)


@app.route('/settings')
def settings():
    return render_template("settings.html")


@app.route("/post/<int:postid>")
def post(postid):
    if postid in datas_dict.keys():
        datas = datas_dict[postid]
        content = [x.split('\n') for x in datas if x.strip() != '\n']
        print(datas[3])
        return render_template('page.html', datas=datas, content=content[1])
    else:
        return render_template('404.html')


@app.route("/<post>")
def post_(post):
    if post not in divs:
        return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True)
