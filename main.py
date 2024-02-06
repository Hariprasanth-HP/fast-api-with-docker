from fastapi import FastAPI
from config import settings
from database import engine 
from model import Base
app = FastAPI()



# @app.get('/')
# async def getRoot():
#     return {'hello fastapi'}

# @app.get("/users")
# async def users():
#     users = [
#         {
#             "name": "Mars Kule",
#             "age": 25,
#             "city": "Lagos, Nigeria"
#         },

#         {
#             "name": "Mercury Lume",
#             "age": 23,
#             "city": "Abuja, Nigeria"
#         },

#          {
#             "name": "Jupiter Dume",
#             "age": 30,
#             "city": "Kaduna, Nigeria"
#         }
#     ]

#     return users



def create_tables():         
	Base.metadata.create_all(bind=engine)
        

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
    create_tables()
    return app


app = start_application()


@app.get("/")
def home():
    return {"msg":"Hello FastAPI🚀"}
