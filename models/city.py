from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """Class for City"""
    __tablename__ = 'cities'  # Table name

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    # Add a relationship to State class (for DBStorage)
    state = relationship("State", back_populates="cities")

    def __init__(self, *args, **kwargs):
        """Initializes City"""
        super().__init__(*args, **kwargs)
