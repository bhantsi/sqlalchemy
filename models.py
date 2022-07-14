from sqlalchemy import (create_engine, Column , Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///pets.db', echo=False)
Sesssion = sessionmaker(bind=engine)
session = Sesssion()
Base = declarative_base()


class Pet(Base):
    __tablename__ = 'pets'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    species = Column(String)
    age = Column(Integer)
    owner = Column(String)

    def __repr__(self):
        return f'<Pet {self.id} {self.name} {self.species} {self.age} {self.owner}>'

if __name__ == '__main__':
    Base.metadata.create_all(engine)