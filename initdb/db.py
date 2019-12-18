from time import sleep
import os

from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import Session

from models import Base
from utils import eprint


URL_TEMPLATE = 'postgresql://{user}:{password}@{host}:{port}/{database_name}'
_engine = None


def _get_engine():
    """
    Lazily instantiates an sqlalchemy.Engine.
    """
    global _engine

    if _engine is None:
        connection_params = {
            'user': os.getenv('DBUSER'),
            'password': os.getenv('DBPASSWORD'),
            'host': os.getenv('DBHOST'),
            'port': os.getenv('DBPORT'),
            'database_name': os.getenv('DBNAME'),
        }
        db_url = URL_TEMPLATE.format(**connection_params)
        _engine = create_engine(db_url)
    return _engine


def make_session():
    return Session(bind=_get_engine())


def create_all(retries=10, retry_period=2.0):
    engine = _get_engine()

    while retries > 0:
        try:
            Base.metadata.create_all(engine)
            break
        except OperationalError:
            eprint(f'database still unavailable... retrying in {retry_period} seconds.')
            sleep(retry_period)
            retries -= 1
