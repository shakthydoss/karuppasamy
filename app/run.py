from flask import Flask
import rest.controller.authenticator as authenticator

import logging
from logging.handlers import RotatingFileHandler


#creating flask object
app = Flask(__name__)
app.debug = True
app.secret_key = 'my_app_secret_key'
formatter = logging.Formatter("%(levelname)s | %(asctime)s | %(filename)s:%(lineno)d | %(funcName)s | %(message)s")
handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)
app.logger.addHandler(handler)


#registering blueprint objects to flask 
app.register_blueprint(authenticator.blueprint, url_prefix='/auth')



if __name__ == '__main__':
    app.run(debug=True, threaded=True)
