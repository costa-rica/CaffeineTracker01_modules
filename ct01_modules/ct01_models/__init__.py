from .modelsMain import login_manager, sess, engine, text, Base, \
    Users, CaffeineLog

import os


############################################################################
## This is one of the first files to execute so make dirs here

if not os.path.exists(os.environ.get('DB_ROOT')):
    os.makedirs(os.environ.get('DB_ROOT'))

##########################################################

#Build db
if os.path.exists(os.path.join(os.environ.get('DB_ROOT'),os.environ.get('DB_NAME'))):
    print(f"db already exists: {os.path.join(os.environ.get('DB_ROOT'),os.environ.get('DB_NAME'))}")
else:
    Base.metadata.create_all(engine)
    print(f"NEW db created: {os.path.join(os.environ.get('DB_ROOT'),os.environ.get('DB_NAME'))}")