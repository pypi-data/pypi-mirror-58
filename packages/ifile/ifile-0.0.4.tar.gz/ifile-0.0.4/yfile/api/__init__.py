from flask import Blueprint, jsonify
from flask_restplus import Api

from yfile.version import __version__

api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint, doc='/docs', version=__version__, title='YFile API')

downloader_api = api.namespace('Downloader', path='/downloader',
                               description='downloader api')
pictures_api = api.namespace('Pictures', path='/pictures',
                             description='pictures api')


@api_blueprint.route('/version/')
def get_version():
    return jsonify({'version': __version__}), 200


from yfile.api import picture
