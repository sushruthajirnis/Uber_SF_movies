import os
USERNAME="sfuser"
PASSWORD="Sfuser"
HOST="localhost"
DATABASE="Sfmovies"
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI ="postgresql://"+USERNAME +":"+ PASSWORD +"@"+ HOST+"/"+DATABASE
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
