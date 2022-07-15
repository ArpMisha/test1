class Configuration(object):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:2RTY4356@localhost/ktl_db' # подключаем базу данных
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SECURITY_PASSWORD_SALT = 'fthydn'
	SECURITY_PASSWORD_HASH = 'sha256_crypt'
	SECRET_KEY = 'randomtext'
	