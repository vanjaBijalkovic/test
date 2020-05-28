from playhouse.flask_utils import FlaskDB
import os 

class SQL(FlaskDB):
    def connect_db(self):
        if self.database.is_closed():
            super(SQL, self).connect_db()

database = os.environ.get('db','postgresql://postgres:docker@localhost:5432/postgres')
db = SQL(database=database)
