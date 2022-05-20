import sqlite3

from Todo import Todo


class TodoDAO:

    def __init__(self,db):
        self._con = sqlite3.connect(db)

    def findAll(self):
        # l = []
        cur = self._con.cursor()
        for id,userId,title,completed in cur.execute('SELECT * FROM todos_tbl'):
            todo = Todo(userId,title,completed,id)
            # l.append(todo)
            yield todo

        # return l

    def __del__(self):
        self._con.close()