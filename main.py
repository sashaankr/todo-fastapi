import uvicorn
from fastapi import FastAPI
import models
from database import engine
from routers import auth, todos

app = FastAPI()

# This creates a new database based on the info in database.py and models.py
models.Base.metadata.create_all(bind=engine)
app.include_router(auth.router)
app.include_router(todos.router)

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
