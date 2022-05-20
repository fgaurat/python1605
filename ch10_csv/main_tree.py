from tkinter import *
from tkinter import ttk

from Todo import Todo
from TodoDAO import TodoDAO

def main():
    root = Tk()
    tree = ttk.Treeview(root,columns=('id','userId','title','completed'),show="headings")
    tree.heading("id",text="#")
    tree.heading("userId",text="User ID")
    tree.heading("title",text="Title")
    tree.heading("completed",text="done ?")
    
    dao = TodoDAO(r'todos.sqlite')

    for todo in dao.findAll():
        tree.insert("",index=todo.id,values=[todo.id,todo.userId,todo.title,todo.completed])

    tree.pack(fill=BOTH,expand=True)

    root.mainloop()

if __name__ == '__main__':
    main()