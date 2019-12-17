from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, BigInteger, String, Float, Boolean


Base = declarative_base()


class VehicleState(Base):
    """
    Represents the Vehicle state at a given point in time.
    """

    __tablename__ = 'vehicle_state'

    id = Column(BigInteger, primary_key=True)

    timestamp = Column(BigInteger, index=True)  # in microseconds, e.g. 1352160000000000.
    operator = Column(String, index=True)
    longitude = Column(Float)
    latitude = Column(Float)
    vehicle_id = Column(Integer, index=True)
    latitude = Column(Boolean, index=True)
