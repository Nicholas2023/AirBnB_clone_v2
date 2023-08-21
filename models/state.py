from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Class for State"""
    __tablename__ = 'states'  # Table name

    name = Column(String(128), nullable=False)

    # Add a relationship to City class (for DBStorage)
    cities = relationship("City", back_populates="state",
                          cascade="all, delete-orphan")

    def __init__(self, *args, **kwargs):
        """Initializes State"""
        super().__init__(*args, **kwargs)
