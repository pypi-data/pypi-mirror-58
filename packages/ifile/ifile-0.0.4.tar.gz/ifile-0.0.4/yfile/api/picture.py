import mimetypes

from flask import request, jsonify, make_response, send_file, url_for
from flask_restplus import Resource, fields
from werkzeug.datastructures import FileStorage

from yfile.api import pictures_api, downloader_api
from yfile.db.sqlalchemy import api as db_api
from yfile.exception import FileAlreadyExist
from yfile.exception import NotFound
from yfile.storage import api as storage_api


upload_parser = pictures_api.parser()
upload_parser.add_argument('file', location='files',
                           type=FileStorage, required=True)

picture_get_response_model = pictures_api.model(
    'PictureGetResponseModel',
    {
        'id': fields.Integer,
        'name': fields.String,
        'size': fields.Integer,
        'uuid': fields.String,
        'md5': fields.String,
        'url': fields.String,
        'downloader_url': fields.String
    }
)

picture_delete_response_model = pictures_api.model(
    'PictureDeleteResponseModel',
    {
        'id': fields.Integer,
    }
)

picture_add_response_model = pictures_api.model(
    'PictureAddResponseModel',
    {
        'id': fields.Integer,
        'url': fields.String,
        'downloader_url': fields.String
    }
)


@pictures_api.route('/<int:id>', endpoint='picture')
@pictures_api.response(404, "resource not found")
class Picture(Resource):
    @pictures_api.marshal_with(picture_get_response_model, code=200)
    @pictures_api.response(400, "params error.")
    def get(self, id):
        try:
            picture = storage_api.Picture(id)
        except NotFound as e:
            pictures_api.abort(404, message=str(e))

        item = picture.to_json()
        item.update({
            "url": url_for("api.picture", id=id, _external=True),
            "downloader_url": url_for("api.downloader", id=id, _external=True)
        })
        return item

    @pictures_api.marshal_with(picture_delete_response_model, code=200)
    def delete(self, id):
        try:
            picture = storage_api.Picture(id)
        except NotFound as e:
            pictures_api.abort(404, message=str(e))
        picture.destroy()
        return {"id": id}


@pictures_api.route('/')
class Pictures(Resource):
    @pictures_api.marshal_list_with(picture_get_response_model, code=200)
    def get(self):
        items = []
        pictures = storage_api.Pictures()
        for picture_id in pictures:
            picture = storage_api.Picture(picture_id)
            item = picture.to_json()
            item.update({
                "url": url_for("api.picture", id=picture_id, _external=True),
                "downloader_url": url_for("api.downloader", id=picture_id, _external=True)
            })
            items.append(item)

        return items

    @pictures_api.expect(upload_parser)
    @pictures_api.marshal_with(picture_add_response_model, code=201)
    def post(self):
        img = request.files.get('file')
        pictures = storage_api.Pictures()
        picture = pictures.add(img.filename, img.stream)

        item = {
            'id': picture.id,
            'url': url_for("api.picture", id=picture.id, _external=True),
            'downloader_url': url_for("api.downloader", id=picture.id, _external=True)
        }
        return item, 201


@downloader_api.route('/pictures/<int:id>', endpoint='downloader')
@downloader_api.response(404, "resource not found")
class PictureDownloader(Resource):
    def get(self, id):
        try:
            picture = storage_api.Picture(id)
            bdata = picture.stream
        except NotFound as e:
            pictures_api.abort(404, message=str(e))

        response = make_response(bdata)

        mime_type = mimetypes.guess_type(picture.name)
        response.headers['Content-Type'] = mime_type
        response.headers['Content-Disposition'] = \
            'attachment; filename={}'.format(
                picture.name.encode().decode('latin-1'))
        return response
