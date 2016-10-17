from flask import current_app
import rest.dao.mysqldb as connection_manager
import rest.util.util as util


def add_user(data):
    current_app.logger.debug("Entering method add_user of authenticator_dao")
    db = connection_manager.get_connection()
    cursor = db.cursor()
    try:
        sql = "select * from secret where username = %s"
        values = (data["username"],)
        cursor.execute(sql, values)
        results = cursor.fetchall()
        if (results):
            # user already exit.
            return_value = 1
        else:
            uid = util.get_key()
            sql = "insert into secret (uid, username, password_enc, updated_by) values (%s, %s, %s, %s)"
            values = (str(uid), data["username"], data["password"], data["updated_by"])
            cursor.execute(sql, values)
            db.commit()
            return_value = uid
    except Exception, e:
        current_app.logger.error("Exception : %s", str(e))
        db.rollback()
        return_value = -1
    finally:
        connection_manager.close_db(db)
    return return_value
    current_app.logger.debug("Exit method add_user of authenticator_dao")


def authenticate_user(data):
    current_app.logger.debug("Entering method authenticate of authenticator_dao.")
    db = connection_manager.get_connection()
    cursor = db.cursor()
    try:
        sql = "select uid from secret where username = %s and password_enc = %s"
        values = (data['username'], data['password'])
        cursor.execute(sql, values)
        results = cursor.fetchone()
        if (results):
            # valid user.
            # deleting if any token exists for the user.
            sql = "delete from usr_token where uid = %s"
            values = (results[0],)
            cursor.execute(sql, values)
            # adding new token for the user.
            sql = "insert into usr_token (uid,token) values (%s, %s)"
            token = util.get_key()
            values = (results[0], token)
            cursor.execute(sql, values)
            db.commit()
            return_value = dict()
            return_value["access_token"] = token
            return_value["uid"] = results[0]
        else:
            # authentication failed or not exit.
            return_value = 0
    except Exception, e:
        current_app.logger.error("Exception : %s", str(e))
        db.rollback()
        return_value = -1
    finally:
        connection_manager.close_db(db)
    current_app.logger.debug("Exit method authenticate of authenticator_dao.")
    return return_value


def authenticate_token(data):
    current_app.logger.debug("Entering method authenticate_token of authenticator_dao")
    db = connection_manager.get_connection()
    cursor = db.cursor()
    try:
        sql = "select token from usr_token where token = %s and uid = %s"
        values = (data["access_token"], data["uid"])
        cursor.execute(sql, values)
        results = cursor.fetchall()
        if (results):
            # token exit valid request.
            return_value = 1
        else:
            return_value = 0
    except Exception, e:
        current_app.logger.error("Exception : %s", str(e))
        db.rollback()
        return_value = -1
    finally:
        connection_manager.close_db(db)
    current_app.logger.debug("Exiting method authenticate_token of authenticator_dao")
    return return_value


def update_email(data):
    current_app.logger.debug("Entering method update_email of authenticator_dao")
    db = connection_manager.get_connection()
    cursor = db.cursor()
    try:
        sql = "update secret set email=%s where uid = %s"
        values = (data["email"], data["uid"])
        cursor.execute(sql, values)
        db.commit()
        return_value = 1
    except Exception, e:
        current_app.logger.error("Exception : %s", str(e))
        db.rollback()
        return_value = -1
    finally:
        connection_manager.close_db(db)
    return return_value
    current_app.logger.debug("Exiting method update_email of authenticator_dao")
    return ""


def update_username(data):
    current_app.logger.debug("Entering method update_username of authenticator_dao")
    db = connection_manager.get_connection()
    cursor = db.cursor()
    try:
        sql = "update secret set username=%s where uid = %s"
        values = (data["new_username"], data["uid"])
        print values
        cursor.execute(sql, values)
        db.commit()
        return_value = 1
    except Exception, e:
        current_app.logger.error("Exception : %s", str(e))
        db.rollback()
        return_value = -1
    finally:
        connection_manager.close_db(db)
    current_app.logger.debug("Exiting method update_username of authenticator_dao")
    return return_value


def update_password(data):
    current_app.logger.debug("Entering method update_password of authenticator_dao")
    db = connection_manager.get_connection()
    cursor = db.cursor()
    try:
        sql = "update secret set password_enc=%s where uid = %s"
        values = (data["password"], data["uid"])
        cursor.execute(sql, values)
        db.commit()
        return_value = 1
    except Exception, e:
        current_app.logger.error("Exception : %s", str(e))
        db.rollback()
        return_value = -1
    finally:
        connection_manager.close_db(db)
    current_app.logger.debug("Exiting method update_password of authenticator_dao")
    return return_value


def logout(data):
    current_app.logger.debug("Entering method logout of authenticator_dao")
    db = connection_manager.get_connection()
    cursor = db.cursor()
    try:
        sql = "delete from usr_token where uid = %s"
        value = (data["uid"],)
        cursor.execute(sql, value)
        db.commit()
        return_value = 1
    except Exception, e:
        current_app.logger.error("Exception : %s", str(e))
        db.rollback()
        return_value = -1
    finally:
        connection_manager.close_db(db)
    current_app.logger.debug("Exiting method logout of authenticator_dao")
    return return_value
