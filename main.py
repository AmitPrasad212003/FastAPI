from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ToDo(BaseModel) :
    id : int
    name : str
    descripton : str

todos = []

@app.get("/")
def show_Todos():
    return todos

@app.post('/')
def create_todo(todo : ToDo):
    todos.append(todo)
    return {"message" : "Todo Created Succesfully"}

@app.put('/{todo_id}')
def update_todo(todo_id : int, updated_todo : ToDo):
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[i] = updated_todo
            return { "message" : "Your Todo Has Been Updated"}
    return {"message" : "Failed to Updated todo"}

@app.delete('/{todo_id}')
def delete_todo(todo_id : int):
    global todos
    todos = [todo for todo in todos if todo.id != todo_id]
    return {"message" : "Todo Deleted Successfully"}