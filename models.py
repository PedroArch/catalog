from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__="users"

    id = Column(Integer, primary_key=True)
    username = Column(String(250))
    email = Column(String(250))
    password = Column(String(250))

class Category(Base):
    __tablename__ ="categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(250))

class Item(Base):
    __tablename__="items"

    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    description = Column(String(2000))
    category_id = Column(Integer, ForeignKey('categories.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=func.now())
    category = relationship(Category)
    user = relationship(User)







## End of File ##
engine = create_engine('sqlite:///catalog.db')
Base.metadata.create_all(engine)
