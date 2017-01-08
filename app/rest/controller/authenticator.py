import rest.dao.authenticator_dao as authenticator_dao
import rest.util.http_status_codes as http_status_codes
import rest.util.util as util
import rest.validator.authenticator_validator as validator
from flask import Blueprint, request, current_app

blueprint = Blueprint('auth_controller', __name__)


@blueprint.route('/addUser/', methods=['POST'])
def add_user():
    current_app.logger.debug("Entering method add_user of authenticator.")
    if hasattr(request, 'json'):
        data = request.json
        print data
        current_app.logger.debug(data)
        is_valid, error = validator.add_user(data)
        if not is_valid:
            return util.to_json(http_status_codes.BAD_REQUEST, error)
    else:
        return util.to_json(http_status_codes.BAD_REQUEST, None)
    return_value = authenticator_dao.add_user(data)
    if return_value == 1:
        return util.to_json(http_status_codes.CONFLICT, http_status_codes.MESSAGE_CONFLICT)
    elif return_value == -1:
        return util.to_json(http_status_codes.SERVER_ERROR, http_status_codes.MESSAGE_SERVER_ERROR)
    else:
        temp = dict()
        temp["uid"] = return_value
    return util.to_json(http_status_codes.SUCCESSFULLY_CREATED, temp)


@blueprint.route('/updateEmail/', methods=['POST'])
def update_email():
    current_app.logger.debug("Entering method update_user of authenticator.")
    if hasattr(request, 'json'):
        data = request.json
        is_valid, error = validator.update_email(data)
        if not (is_valid):
            return util.to_json(http_status_codes.BAD_REQUEST, error)
    else:
        return util.to_json(http_status_codes.BAD_REQUEST, None)
    return_value = authenticator_dao.update_email(data)
    if return_value == -1:
        return util.to_json(http_status_codes.SERVER_ERROR, http_status_codes.MESSAGE_SERVER_ERROR)
    return util.to_json(http_status_codes.SUCCESS, http_status_codes.MESSAGE_SUCCESS)


@blueprint.route('/updateUsername/', methods=['POST'])
def update_username():
    current_app.logger.debug("Entering method username of authenticator")
    if hasattr(request, 'json'):
        data = request.json
        is_valid, error = validator.update_username(data)
        print is_valid
        print error
        if not (is_valid):
            return util.to_json(http_status_codes.BAD_REQUEST, error)
    else:
        return util.to_json(http_status_codes.BAD_REQUEST, None)
    return_value = authenticator_dao.update_username(data)
    if return_value == -1:
        return util.to_json(http_status_codes.SERVER_ERROR, http_status_codes.MESSAGE_SERVER_ERROR)
    return util.to_json(http_status_codes.SUCCESS, http_status_codes.MESSAGE_SUCCESS)


@blueprint.route('/updatePassword/', methods=['POST'])
def update_password():
    current_app.logger.debug("Entering method update_password of authenticator")
    if hasattr(request, 'json'):
        data = request.json
        is_valid, error = validator.update_password(data)
        if not (is_valid):
            return util.to_json(http_status_codes.BAD_REQUEST, error)
    else:
        return util.to_json(http_status_codes.BAD_REQUEST, None)
    return_value = authenticator_dao.update_password(data)
    if return_value == -1:
        return util.to_json(http_status_codes.SERVER_ERROR, http_status_codes.MESSAGE_SERVER_ERROR)
    return util.to_json(http_status_codes.SUCCESS, http_status_codes.MESSAGE_SUCCESS)


@blueprint.route('/authenticateUser/', methods=['POST'])
def authenticate_user():
    current_app.logger.debug("Entering method authenticate_user of authenticator.")
    if hasattr(request, 'json'):
        data = request.json
        is_valid, error = validator.authenticate_user(data)
        if not (is_valid):
            return util.to_json(http_status_codes.BAD_REQUEST, error)
    else:
        return util.to_json(http_status_codes.BAD_REQUEST, None)
    return_value = authenticator_dao.authenticate_user(data)
    if return_value == 0:
        return util.to_json(http_status_codes.UNAUTHORIZED, http_status_codes.MESSAGE_UNAUTHORIZED)
    elif return_value == -1:
        return util.to_json(http_status_codes.SERVER_ERROR, http_status_codes.MESSAGE_SERVER_ERROR)
    return util.to_json(http_status_codes.SUCCESS, return_value)


@blueprint.route('/authenticateToken/', methods=['POST'])
def authenticate_token():
    current_app.logger.debug("Entering method authenticate_token of authenticator.")
    if hasattr(request, 'json'):
        data = request.json
        is_valid, error = validator.authenticate_token(data)
        if not is_valid:
            return util.to_json(http_status_codes.BAD_REQUEST, error)
    else:
        return util.to_json(http_status_codes.BAD_REQUEST, None)
    return_value = authenticator_dao.authenticate_token(data)
    if return_value == 1:
        # token is vaild.
        temp = dict()
        temp["valid"] = True
        return util.to_json(http_status_codes.SUCCESS, temp)
    elif return_value == 0:
        return util.to_json(http_status_codes.UNAUTHORIZED, http_status_codes.MESSAGE_UNAUTHORIZED)
    return util.to_json(http_status_codes.SERVER_ERROR, http_status_codes.MESSAGE_SERVER_ERROR)


@blueprint.route('/logout/', methods=['POST'])
def logout():
    current_app.logger.debug("Entering method logout of authenticator.")
    if hasattr(request, 'json'):
        data = request.json
        is_valid, error = validator.logout(data)
        if not is_valid:
            return util.to_json(http_status_codes.BAD_REQUEST, error)
    else:
        return util.to_json(http_status_codes.BAD_REQUEST, None)
    return_value = authenticator_dao.logout(data)
    print return_value
    if return_value == -1:
        return util.to_json(http_status_codes.SERVER_ERROR, http_status_codes.MESSAGE_SERVER_ERROR)
    return util.to_json(http_status_codes.SUCCESS, http_status_codes.MESSAGE_SUCCESS)
