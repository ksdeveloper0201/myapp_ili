from flask import Blueprint, jsonify
from flaskr.exceptions.custom_exception import IsNotFound
from flaskr.responses import api_response
from flaskr.providers.world_provider import WorldProvider

bp = Blueprint("world", __name__)


@bp.route("/", methods=["GET"])
def hello_world():
    return "hello world!"


@bp.route("/city", methods=["GET"])
def get_city():
    """世界の都市情報を取得

    Returns:
        _type_: _description_
    """
    try:
        city_name_list = True
        provider = WorldProvider()
        world_list = provider.get_city_list()
    except IsNotFound:
        return api_response.not_find()
    except Exception as ex:
        print(ex)
        return api_response.handle_exception()
    finally:
        pass
    return api_response.success(world_list)


@bp.route("/city/<city_id>", methods=["GET"])
def get_city_info(city_id):
    """idに該当する都市の情報を取得

    """
    try:
        provider = WorldProvider()
        city_info = provider.get_city_info(city_id)
    except IsNotFound:
        return api_response.not_find()
    except Exception as ex:
        print(ex)
        return api_response.handle_exception()
    finally:
        pass
    return api_response.success(city_info)
