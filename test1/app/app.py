from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_security import SQLAlchemySessionUserDatastore, Security



app = Flask(__name__)
app.config.from_object(Configuration) # аналог режима дебаг
db = SQLAlchemy(app) # передаем экземпляр класса app в db

# миграция db app и менеджер миграции
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


from models import *
# flask_security
user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
security = Security(app, user_datastore)

