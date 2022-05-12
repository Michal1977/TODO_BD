from forms import TodoForm
from models import Todos

#todos = Todos("_")

db = Todos("todos.db")
db.create_table(
    '''CREATE TABLE IF NOT EXISTS todos (
    id integer PRIMARY KEY,
    title text NOT NULL,
    description text,
    done BOOLEAN);
    ''')

try:
    db.add_to_table("todos", {'title':'szachy', 'description':'debiut obrona pirca', 'done':'False'})
except Exception as err:
    print(err)


try:
    result=db.get('todos', {'title':'szachy'}).fetchall()
    print(result)
except Exception as err:
    print(err)

db.update("todos", 1, title='szachy2')

try:
    result=db.get('todos', {'id':1}).fetchall()
    print(result)
except Exception as err:
    print(err)