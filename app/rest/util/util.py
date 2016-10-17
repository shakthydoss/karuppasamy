from flask import jsonify

import random
import string
import time
import uuid


# this method create genarates random alpha numeric key
def get_key():
    uid = uuid.uuid4()
    return str(uid.hex)


def get_current_ts_in_ms():
    return str(int(round(time.time() * 1000)))


# used for mysql tables.
def get_current_ts():
    return time.strftime('%Y-%m-%d %H:%M:%S')


def to_json(status_code, data):
    return jsonify({'status': status_code, 'data': data}), status_code


if __name__ == '__main__':
    get_key()
