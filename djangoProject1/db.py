from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql://root:1502@localhost:8888/database_name")

Base = declarative_base()

class User(Base):
    __tablename__ = "gamers"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(100))

def addNewUser(user,email):
    user = User(user,email)
    engine.execute(user.insert())
    print("New user:" + user)

def runQuery(query):
    users = engine.execute(query)
    print(users)



