from flask import Flask, make_response, Response


def api_response(response: Response, status_code: int):
    response.status_code = status_code
    response.headers["Content-Type"] = "application/json;charset=UTF8"
    return response


def success(body: dict):
    response = make_response(body)
    return api_response(response=response, status_code=200)


def handle_exception(message="Bad Request"):
    """exception発生

    Args:
        error (_type_): _description_

    Returns:
        _type_: _description_
    """
    error_response = make_response({"message": message})
    return api_response(error_response, response=404)


def not_find(message="not find"):
    """exception発生

    Args:
        error (_type_): _description_

    Returns:
        _type_: _description_
    """
    error_response = make_response({"message": message})
    return api_response(error_response, response=403)
