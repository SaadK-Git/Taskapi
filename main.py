from fastapi import FastAPI;
from endpoints import router
from database import Base, engine
from contextlib import asynccontextmanager
@asynccontextmanager
async def lifespan(app: FastAPI):
    # This is startup code that helps to create tables in the database when the application starts. It ensures that the necessary tables are set up before handling any requests.
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")

    yield

app = FastAPI(lifespan=lifespan)

app.include_router(router, prefix="/api")