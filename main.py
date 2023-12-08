from fastapi import FastAPI
from fastapi.responses import JSONResponse
from users.routes import router as guest_router, user_router
from auth.route import router as auth_router
from core.security import JWTAuth
from starlette.middleware.authentication import AuthenticationMiddleware
from core.database import Base, engine
from todo.todos_routes import router as todo_route


Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(guest_router)
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(todo_route)

# Add Middleware
app.add_middleware(AuthenticationMiddleware, backend=JWTAuth())


@app.get("/")
def health_check():
    return JSONResponse(content={"status": "is woking fine"})
