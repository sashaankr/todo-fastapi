from fastapi import FastAPI
import models
from database import engine
from routers import auth, todos

app = FastAPI()

# This creates a new database based on the info in database.py and models.py
models.Base.metadata.create_all(bind=engine)
app.include_router(auth.router)
app.include_router(todos.router)
