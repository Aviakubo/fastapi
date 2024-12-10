from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from datetime import date
import uuid

app = FastAPI()

tasks = {}

class Task(BaseModel):
    id: Optional[str] = None
    title: str
    description: Optional[str] = None
    due_date: Optional[date] = None
    status: str = "pending"

@app.get("/")
def read_root():
    return{"message": "Welcome to the Task Manager API"}

@app.post("/createtasks/")
def create_task(task: Task):
    task.id = str(uuid.uuid4())
    tasks[task.id] = task
    return task

@app.get("/tasks/")
def get_tasks():
    return list(tasks.values())

@app.get("/tasks/{task_id}")
def get_task(task_id: str):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]

@app.put("/tasks/{task_id}")
def update_task(task_id: str, updated_task: Task):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks[task_id].title = updated_task.title
    tasks[task_id].description = updated_task.description
    tasks[task_id].due_date = updated_task.due_date
    tasks[task_id].status = updated_task.status
    return tasks[task_id]

@app.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks[task_id]
    return {"message": "Task deleted successfuklly"}