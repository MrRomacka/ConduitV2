from flask import Flask, render_template, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
def full():
    db_connection = sqlite3.connect('db/marks.db')
    cur = db_connection.cursor()
    exercises = cur.execute('SELECT task_id FROM Task').fetchall()
    numerous = [list(ex)[0] for ex in exercises]
    max_st = int(list(cur.execute('SELECT MAX(stu_id) FROM Student').fetchone())[0])
    data = []
    for j in range(1, max_st + 1):
        name = list(cur.execute(f'SELECT stu_surname, stu_name, stu_group FROM Student WHERE stu_id = {int(j)}').fetchall()[0])
        name = ' '.join(name)
        data.append([])
        data[j-1].append([name, j, 1])
        for i in range(1, max(numerous) + 1):
            exercises = cur.execute(f'SELECT st_task_id FROM StudentTask WHERE st_stu_id = {j}').fetchall()
            exes = [list(ex)[0] for ex in exercises]
            if i in exes:
                mark = list((cur.execute(f'SELECT st_mark FROM StudentTask WHERE st_stu_id = {j} AND st_task_id = {i}').fetchone()))[0]
                m_m = list(cur.execute(f'SELECT task_max_mark FROM Task WHERE task_id = {i}').fetchone())[0]
                data[j-1].append([mark, m_m, 0])
            else:
                m_m = list((cur.execute(f'SELECT task_max_mark FROM Task WHERE task_id = {i}').fetchone()))[0]
                data[j-1].append([0, m_m, 0])
    return render_template('tb_2.html', data = data, numerous = numerous)

@app.route('/task/<num>')
def Tasky(num):
    db_connection = sqlite3.connect('db/marks.db')
    cur = db_connection.cursor()
    inf = list(cur.execute(f'SELECT task_number, task_theme, task_equation, task_max_mark, task_date FROM Task WHERE task_id = {int(num)}').fetchone())
    print(inf)
    cur.close()
    db_connection.close()
    return render_template('task.html', number = inf[0], theme = inf[1], eq = inf[2], maxi = inf[3], date = inf[4])

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
    exercises = cur.execute(f'SELECT st_task_id FROM StudentTask WHERE st_stu_id = {pos}').fetchall()
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
    cur.close()
    db_connection.close()
    return render_template('solo.html', data = data, name = name)



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')