from model import *


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_win(name, score,time):
	 
		win_object = Win(
		name= name,
		score=score,
		time= time)
		session.add(win_object)
		session.commit()



def query_all():
	 
	 users = session.query(
			User).all()
	 return users


def query_by_name(their_name):

	 user= session.query(
			 User).filter_by(
			 name=name).first()
	 return user

















