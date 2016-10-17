from flask import current_app


def add_user(data):
    current_app.logger.debug("Entering method add_user of authenticator_validator.")
    is_valid = True
    error = ""
    if 'username' not in data:
        error = "username field is missing."
        is_valid = False
    if 'username' in data:
        if not data['username']:
            error = "username cannot be empty."
            is_valid = False
    if not 'password' in data:
        error = "password field is missing."
        is_valid = False
    if 'password' in data:
        if not data['password']:
            error = "password cannot be empty."
            is_valid = False
    if not 'updated_by' in data:
        error = "updated_by field is missing."
        is_valid = False
    if 'updated_by' in data:
        if not data['updated_by']:
            error = "updated_by cannot be empty."
            is_valid = False
    current_app.logger.debug("Exiting method add_user of authenticator_validator.")
    return is_valid, error


def authenticate_user(data):
    current_app.logger.debug("Entering method authenticate_user of authenticator_validator.")
    is_valid = True
    error = ""
    if not 'username' in data:
        error = "username field is missing."
        is_valid = False
    if 'username' in data:
        if not data['username']:
            error = "username cannot be empty."
            is_valid = False
    if not 'password' in data:
        error = "password field is missing."
        is_valid = False
    if 'password' in data:
        if not data['password']:
            error = "password cannot be empty."
            is_valid = False
    if not 'password' in data:
        error = "password field is missing."
        is_valid = False
    current_app.logger.debug("Exiting method authenticate_user of authenticator_validator.")
    return is_valid, error


def authenticate_token(data):
    current_app.logger.debug("Entering method authenticate_token of authenticator_validator.")
    is_valid = True
    error = ""
    if not 'access_token' in data:
        error = "access_token field is missing."
        is_valid = False
    if 'access_token' in data:
        if not data['access_token']:
            error = "access_token cannot be empty."
            is_valid = False
    if 'uid' in data:
        if not data['uid']:
            error = "uid cannot be empty."
            is_valid = False
    current_app.logger.debug("Exiting method authenticate_token of authenticator_validator.")
    return is_valid, error


def update_email(data):
    current_app.logger.debug("Entering method update_email of authenticator_validator.")
    is_valid = True
    error = ""
    if not 'uid' in data:
        error = "uid field is missing."
        is_valid = False
    if 'uid' in data:
        if not data['uid']:
            error = "uid cannot be empty."
            is_valid = False
    if not 'email' in data:
        error = "email field is missing."
        is_valid = False
    if 'email' in data:
        if not data['email']:
            error = "email cannot be empty."
            is_valid = False
    current_app.logger.debug("Exiting method update_email of authenticator_validator.")
    return is_valid, error


def update_username(data):
    current_app.logger.debug("Entering method update_username of authenticator_validator.")
    is_valid = True
    error = ""
    if not 'uid' in data:
        error = "uid field is missing."
        is_valid = False
    if 'uid' in data:
        if not data['uid']:
            error = "uid cannot be empty."
            is_valid = False
    if not 'access_token' in data:
        error = "access_token field is missing."
        is_valid = False
    if 'access_token' in data:
        if not data['access_token']:
            error = "access_token cannot be empty."
            is_valid = False
    if not 'updated_by' in data:
        error = "updated_by field is missing."
        is_valid = False
    if 'updated_by' in data:
        if not data['updated_by']:
            error = "updated_by cannot be empty."
            is_valid = False
    if not 'new_username' in data:
        error = "new_username field is missing."
        is_valid = False
    if 'new_username' in data:
        if not data['new_username']:
            error = "new_username cannot be empty."
            is_valid = False
    current_app.logger.debug("Exiting method update_username of authenticator_validator.")
    return is_valid, error


def update_password(data):
    current_app.logger.debug("Entering method update_password of authenticator_validator")
    is_valid = True
    error = ""
    if not 'uid' in data:
        error = "uid field is missing."
        is_valid = False
    if 'uid' in data:
        if not data['uid']:
            error = "uid cannot be empty."
            is_valid = False
    if not 'password' in data:
        error = "password field is missing."
        is_valid = False
    if 'password' in data:
        if not data['password']:
            error = "password cannot be empty."
            is_valid = False
    current_app.logger.debug("Exiting method update_password of authenticator_validator.")
    return is_valid, error


def logout(data):
    current_app.logger.debug("Entering method logout of authenticator_validator.")
    is_valid = True
    error = ""
    if not 'uid' in data:
        error = "uid field is missing."
        is_valid = False
    if 'uid' in data:
        if not data['uid']:
            error = "uid cannot be empty."
            is_valid = False
    return is_valid, error
