from pprint import pprint
import json


def main():

    with open("todos.json") as f:
        todo_list = json.load(f)
        print(todo_list[0]['title'])

def main_write_json():
    todo_list = [
        {
            "userId": 1,
            "id": 1,
            "title": "delectus aut autem",
            "completed": False
        },
        {
            "userId": 1,
            "id": 2,
            "title": "quis ut nam facilis et officia qui",
            "completed": True
        },
        {
            "userId": 1,
            "id": 3,
            "title": "fugiat veniam minus",
            "completed": False
        }]

    with open("todos.json", "w") as f:
        json.dump(todo_list,f)


def main_read():
    todos = []
    with open('todos.csv', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        header = lines[0].split(";")
        data = lines[1:]

        for d in data:
            line = d.split(';')
            todo = dict(zip(header, line))
            todos.append(todo)

    pprint(todos)


def main_write():
    todo_list = [
        {
            "userId": 1,
            "id": 1,
            "title": "delectus aut autem",
            "completed": False
        },
        {
            "userId": 1,
            "id": 2,
            "title": "quis ut nam facilis et officia qui",
            "completed": True
        },
        {
            "userId": 1,
            "id": 3,
            "title": "fugiat veniam minus",
            "completed": False
        }]

    with open('todos.csv', 'w') as f:
        k = todo_list[0].keys()
        header = ";".join(k)
        print(header, file=f)
        for todo in todo_list:
            # values = [str(v) for v in todo.values()]
            # # join
            # line = ";".join(values)
            # print(line,file=f)
            # values = todo.values()
            # format String
            # line = "{};{};{};{}".format(*values)
            # print(line,file=f)

            values = list(todo.values())
            # # fstring
            line = f"{values[0]};{values[1]};{values[2]};{values[3]}"
            print(line, file=f)

            # print
            # print(*todo.values(),file=f,sep=";")


if __name__ == "__main__":
    main()
