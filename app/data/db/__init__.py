import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker

from .db_config import *

engine = sqlalchemy.create_engine(
    f"mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
)

Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
