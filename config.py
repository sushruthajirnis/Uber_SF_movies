#!flask/bin/python
import os
import sys
API_SERVER="AIzaSyCOOMf8w1z4LCFJGR0alfIhNovE8U2vN1Y"
USERNAME="sfuser"
PASSWORD="Sfuser"
HOST="localhost"
DATABASE="Sfmovies"
basedir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(basedir)
SQLALCHEMY_DATABASE_URI ="postgresql://"+USERNAME +":"+ PASSWORD +"@"+ HOST+"/"+DATABASE
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
