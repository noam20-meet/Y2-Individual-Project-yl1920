from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
   __tablename__ = 'Users'
   id = Column(Integer, primary_key=True)
   name = Column(String)
   nummOfWin= Column(Integer)

  
   


class Win (Base):
   __tablename__ = 'Cart'
   id= Column(String, primary_key=True)
   score= Column(Integer)
   time= Column(Integer)
   



