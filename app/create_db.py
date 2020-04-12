from modules import models
# from modules import db
# from migrate.versioning import api
# from modules.default_config import SQLALCHEMY_DATABASE_URI , SQLALCHEMY_MIGRATE_REPO
# import os.path

db.create_all()
# db.session.commit()
# if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
#     api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
#     api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
# else:
#     api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))
