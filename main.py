from fastapi import FastAPI;
from endpoints import router
from database import Base, engine
from contextlib import asynccontextmanager
@asynccontextmanager
async def lifespan(app: FastAPI):
    #App starts..
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")

    yield
    
    #App ends..

app = FastAPI(lifespan=lifespan)

app.include_router(router, prefix="/api")