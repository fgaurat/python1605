import requests
import csv
import sqlite3

from Todo import Todo
from TodoDAO import TodoDAO


def main():

    # t = Todo(1,"le titre",False)    
    # print(t)

    dao = TodoDAO("todos.sqlite")

    todos = dao.findAll()
    for todo in todos:
        print(todo)



def main_insert():
    with sqlite3.connect('todos.sqlite') as con:
        cur = con.cursor()

        with open('todos.csv', newline='') as csvfile:
            todos = csv.DictReader(csvfile,delimiter=";")
            for todo in todos:
                sql = f"""INSERT INTO todos_tbl(user_id,title,completed)
                VALUES ({todo['userId']},'{todo['title']}',{todo['completed']})
                """
                cur.execute(sql)
            
            con.commit()


def main_read_csv():
    with open('todos.csv', newline='') as csvfile:
        todos = csv.DictReader(csvfile,delimiter=";")
        for todo in todos:
            print(todo)

def main_write_csv():   
    url_todos = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url_todos)
    todos = response.json()

    with open('todos.csv', 'w', newline='') as f:
        keys = todos[0].keys()
        writer = csv.DictWriter(f, fieldnames=keys,delimiter=";")
        writer.writeheader()
        writer.writerows(todos)

    

if __name__ == "__main__":
    main()