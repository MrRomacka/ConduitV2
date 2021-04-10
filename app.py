from flask import Flask, render_template
import json
import sqlite3

app = Flask(__name__)

@app.route('/indiv/<pos>')
def pupil(pos):
    return


@app.route('/tasks')
def Tasky():
    return

@app.route('/theory')
def Theoritic():
    return

@app.route('/task/<number>')
def sp_task(number):
    name = cur.execute(f'SELECT stu_surname, stu_name, stu_group '
                       f'FROM Student WHERE stu_id = {int(number)}')
    m_ex = int(cur.execute('SELECT MAX(theory_id) FROM Theory'))
    data = []
    exercises = cur.execute('SELECT ')
    for i in range(1, m_ex + 1):
        if None:
            data.append(cur.execute('SELECT stu_'))
    return render_template('solo.html', data = data, name = name)



if __name__ == '__main__':
    db_connection = sqlite3.connect('db/marks.db')
    cur = db_connection.cursor()
    print(cur.execute('SELECT st_task_id FROM StudentTask WHERE st_stu_id = 3'), type(cur.execute('SELECT st_task_id FROM StudentTask WHERE st_stu_id = 3')))
    app.run(port=8080, host='127.0.0.1')