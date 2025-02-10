from sqlalchemy import Column, String, Integer, Float
from settings import Base

class PlaceModel(Base):
    __tablename__ = 'place'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    place_id = Column(String)
    formatted_address = Column(String, nullable=True)
    formatted_phone_number = Column(String, nullable=True)
    # opening_hours
    rating = Column(Float, nullable=True)
    user_rating_total = Column(Integer, nullable=True)
    # reviews
    url = Column(String, nullable=True)