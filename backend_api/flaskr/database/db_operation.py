from flaskr.database.database import db


class DbOperation:

    def __init__(self):
        self.session = None

    def set_session(self):
        if self.session is None:
            self.session = db.session()

    def close_session(self):
        if self.session is not None:
            self.session.close()
