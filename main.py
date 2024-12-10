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
    description: Optional[date] = None
    due_date: Optional[date] = None
    status: str = "pending"

@app.get("/")
def read_root():
    return{"message": "Welcome to the Task Manager API"}