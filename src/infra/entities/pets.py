import enum
from sqlalchemy import Column, String, Integer, ForeignKey
from src.infra.config import Base


class Animals(enum.Enum):
    """Defining animals Types to use in column specie"""

    DOG = "dog"
    CAT = "cat"
    FISH = "fish"
    TURTLE = "turtle"
    SNAKE = "snake"


class Pets(Base):
    """Pets Entity"""

    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)
    specie = Column(Integer)
    age = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))

    def __rep__(self):
        return f"Pet: [Name:{self.name}, Specie={self.specie} User_id={self.user_id}]"
