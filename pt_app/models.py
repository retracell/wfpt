from pt_app import db
from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey

class Price(db.Model):
    __tablename__ = 'prices'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    location_name = Column(String)
    good_name = Column(String)
    high = Column(Integer)
    low = Column(Integer)
    mean = Column(Float)

