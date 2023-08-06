from datetime import datetime

from sqlalchemy import (
    Column, Integer, String,
    DateTime, Text, ForeignKey,
    Boolean)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

from yfile.db.sqlalchemy.session import get_session

Base = declarative_base()
metadata = Base.metadata


class MetaBase(object):
    create_at = Column(DateTime(timezone=True), server_default=func.now())
    update_at = Column(DateTime(timezone=True), server_default=func.now())

    def save(self, session=None):
        if session is None:
            session = get_session()
            with session.begin():
                session.add(self)
        else:
            session.add(self)
            session.flush()

    def update(self, **kwargs):
        self.update_at = func.now()

        for k, v in kwargs.items():
            setattr(self, k, v)


class IFile(Base, MetaBase):
    __tablename__ = "ifile"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    uuid = Column(String(100))
    md5 = Column(String(100))
    size = Column(Integer)
    path = Column(String(500))
