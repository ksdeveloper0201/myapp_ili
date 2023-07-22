from flaskr.database.db_operation import DbOperation
from flaskr.models.world import City
from flaskr.responses import api_response


class WorldService(DbOperation):
    def __init__(self) -> None:
        super().__init__()

    def fetch_city(self):
        try:
            self.set_session()
            return (self.session.query(City).all())

        except Exception as e:
            print(e)
            return api_response.handle_exception("error発生")
        finally:
            self.close_session()

    def fetch_city_info(self, city_id):
        try:
            self.set_session()
            city_data = self.session.query(
                City).filter_by(id=city_id).first()
            return city_data
        except Exception as e:
            print(e)
            return api_response.handle_exception("error発生")
        finally:
            self.close_session()
