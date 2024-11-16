
from fastapi import FastAPI
from .database import engine, Base
from .routers import cats, missions  

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(cats.router, prefix="/cats", tags=["cats"])
app.include_router(missions.router, prefix="/missions", tags=["missions"])
