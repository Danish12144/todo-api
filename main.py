from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, Todo, engine

app = FastAPI()

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/todos/", response_model=dict)
def create_todo(title: str, description: str = None, db: Session = Depends(get_db)):
    new_todo = Todo(title=title, description=description)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return {"id": new_todo.id, "title": new_todo.title, "description": new_todo.description}

@app.get("/todos/", response_model=list)
def read_todos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    todos = db.query(Todo).offset(skip).limit(limit).all()
    return todos

@app.get("/todos/{todo_id}", response_model=dict)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"id": todo.id, "title": todo.title, "description": todo.description}

@app.put("/todos/{todo_id}", response_model=dict)
def update_todo(todo_id: int, title: str, description: str = None, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo.title = title
    todo.description = description
    db.commit()
    db.refresh(todo)
    return {"id": todo.id, "title": todo.title, "description": todo.description}

@app.delete("/todos/{todo_id}", response_model=dict)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()
    return {"detail": "Todo deleted"}

