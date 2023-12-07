from fastapi import APIRouter, status, Depends, Request
from todo.todo_model import TodoModel
from core.database import DB
from todo.todo_schemas import Todo
from core.security import oauth2_scheme


router = APIRouter(
    prefix="/todo",
    tags=["Todo"],
    dependencies=[Depends(oauth2_scheme)],
)


@router.post("/create-todo", status_code=status.HTTP_201_CREATED)
async def create_todo(request: Request, todo: Todo, db: DB):
    add_todo = TodoModel(**todo.model_dump(), owner_id=request.user.id)
    db.add(add_todo)
    db.commit()


@router.get("", status_code=status.HTTP_200_OK)
async def get_totos(request: Request, db: DB):
    return db.query(TodoModel).filter(TodoModel.owner_id == request.user.id).all()


@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_totos(request: Request, db: DB, id: int):
    return (
        db.query(TodoModel)
        .filter(TodoModel.owner_id == request.user.id)
        .filter(TodoModel.id == id)
        .first()
    )
