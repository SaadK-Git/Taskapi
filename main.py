from fastapi import FastAPI;
from endpoints import router
from database import Base, engine
app = FastAPI()
app.include_router(router,prefix="/api")
@app.on_event("startup")
def create_tables():  
    # Base.metadata.drop_all(bind=engine) #Use this line to drop preexisting tables.
    Base.metadata.create_all(bind=engine) 
    print("Tables created successfully!")