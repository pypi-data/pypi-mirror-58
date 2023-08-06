from datetime import datetime
from yfile.db.sqlalchemy.session import get_session
from yfile.db.sqlalchemy.models import IFile
from yfile.exception import FileAlreadyExist, NotFound


def add_picture(name, session=None):
    if session is None:
        session = get_session()

    with session.begin():
        ifile = IFile(name=name)
        ifile.save(session=session)

        return ifile


def update_picture(id, values, session=None):
    if session is None:
        session = get_session()

    with session.begin():
        ifile = session.query(IFile).filter(IFile.id == id).first()
        ifile.update(**values)
        ifile.save(session=session)

        return ifile


def get_pictures(session=None):
    if session is None:
        session = get_session()

    pictures = []

    with session.begin():
        pictures_db = session.query(IFile).all()

        for picture_db in pictures_db:

            picture = {
                "id": picture_db.id,
                "uuid": picture_db.uuid,
                "name": picture_db.name,
                "md5": picture_db.md5,
                "size": picture_db.size,
                "path": picture_db.path
            }
            pictures.append(picture)

        return pictures


def get_picture(id, session=None):
    if session is None:
        session = get_session()

    with session.begin():
        picture_db = session.query(IFile).filter(IFile.id == id).first()

        if not picture_db:
            raise NotFound("picture not found, id: %s" % id)

        picture = {
            "id": picture_db.id,
            "uuid": picture_db.uuid,
            "name": picture_db.name,
            "md5": picture_db.md5,
            "size": picture_db.size,
            "path": picture_db.path
        }

        return picture


def destory_picture(id, session=None):
    if session is None:
        session = get_session()

    with session.begin():
        picture = session.query(IFile).filter(IFile.id == id).first()

        if picture:
            session.query(IFile).filter(IFile.id == id).delete()
