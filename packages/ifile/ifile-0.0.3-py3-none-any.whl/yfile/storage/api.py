from flask import current_app

from yfile.storage.mongo import GridFsApi
from yfile.storage.disk import DiskApi
from yfile.db.sqlalchemy import api as db_api
from yfile.common.constant import StorageType
from yfile.exception import NotFound


class Picture(object):
    def __init__(self, id):
        self._id = id
        picture = self._get()

        self.uuid = picture["uuid"]
        self.name = picture["name"]
        self.md5 = picture["md5"]
        self.size = picture["size"]

        storage_type = current_app.config["STORAGE_TYPE"]

        if storage_type == "mongodb":
            mongo_uri = current_app.config["MONGO_URI"]
            self.storage = GridFsApi(mongo_uri, "tb_picture")

        if storage_type == "disk":
            self.storage = DiskApi()

    def _get(self):
        picture = db_api.get_picture(self._id)
        return picture

    @property
    def id(self):
        return self._id

    @property
    def stream(self):
        # TODO 优化异常捕获
        try:
            picture = db_api.get_picture(self._id)
            metadata = self.storage.get(picture["uuid"])
            stream = metadata.read()
        except NotFound as e:
            raise NotFound(str(e))

        return stream

    def destroy(self):
        self.storage.destroy(self.uuid)
        db_api.destory_picture(self._id)

    def add_stream(self, stream):
        ifile = self.storage.add(stream)
        values = {
            "uuid": ifile.uuid,
            "md5": ifile.md5
        }
        picture = db_api.update_picture(self._id, values)
        return picture

    def to_json(self):
        picture = {
            "id": self._id,
            "uuid": self.uuid,
            "name": self.name,
            "md5": self.md5,
            "size": self.size
        }
        return picture


class Pictures(object):
    def __init__(self):
        self._pictures = None
        self._refresh()

    def _get_all_from_db(self):
        pictures = db_api.get_pictures()
        return pictures

    def _refresh(self):
        pictures_db = self._get_all_from_db()
        self._pictures = {picture_db["id"]: Picture(picture_db["id"])
            for picture_db in pictures_db}

    def add(self, name, stream):
        picture_db = db_api.add_picture(name)
        picture = Picture(picture_db.id)
        picture.add_stream(stream)

        self._refresh()
        return picture

    def _destroy(self, id):
        try:
            picture = self._pictures[id]
            picture.destroy()
        except NotFound as e:
            raise NotFound(str(e))

        self._refresh()

    def to_json(self):
        pictures = []
        for _, picture in self._pictures.items():
            pictures.append(picture.to_json())
        return pictures

    def __len__(self):
        return len(self._pictures)

    def __getitem__(self, id):
        return self._pictures[id]

    def __delitem__(self, id):
        self._destroy(id)

    def __iter__(self):
        return iter(self._pictures)
