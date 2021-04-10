from flask import Flask, render_template, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
def full(pos):
    return

@app.route('/tasks')
def Tasky():
    return

@app.route('/theory')
def Theoritic():
    return

@app.route('/indiv/<pos>')
def pupil(pos):
    db_connection = sqlite3.connect('db/marks.db')
    cur = db_connection.cursor()
    name = list(cur.execute(f'SELECT stu_surname, stu_name, stu_group FROM Student WHERE stu_id = {int(pos)}').fetchall()[0])
    print(name)
    name = ' '.join(name)
    m_ex = int(list(cur.execute('SELECT MAX(task_id) FROM Task').fetchone())[0])
    exercises = cur.execute('SELECT st_task_id FROM StudentTask WHERE st_stu_id = 3').fetchall()
    exes = [list(ex)[0] for ex in exercises]
    data = []
    for i in range(1, m_ex + 1):
        if i in exes:
            mark = list((cur.execute(f'SELECT st_mark FROM StudentTask WHERE st_stu_id = {pos} AND st_task_id = {i}').fetchone()))[0]
            m_m = list(cur.execute(f'SELECT task_max_mark FROM Task WHERE task_id = {i}').fetchone())[0]
            data.append([i, mark, m_m])
        else:
            m_m = list((cur.execute(f'SELECT task_max_mark FROM Task WHERE task_id = {i}').fetchone()))[0]
            data.append([i, 0, m_m])
    return render_template('solo.html', data = data, name = name)



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')