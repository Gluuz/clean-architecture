from src.infra.config import DBConecctionHandler
from src.infra.entities.users import Users


class FakeRepository:
    """A simple fake repository"""

    @classmethod
    def insert_user(cls):

        with DBConecctionHandler() as db_connection:
            try:
                new_user = Users(name="Coder", password="secret")
                db_connection.session.add(new_user)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
