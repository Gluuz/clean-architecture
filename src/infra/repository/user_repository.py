from collections import namedtuple
from src.infra.config import DBConecctionHandler
from src.infra.entities import Users


class UserRepository:
    """Class to manage User Repository"""

    @classmethod
    def insert_user(cls, name: str, password: str) -> Users:
        """Set data in user entity
        :param - name: Person name
               - password: Person password
        :return
        """

        insert_data = namedtuple("Users", "id name, password")

        with DBConecctionHandler() as db_connection:
            try:
                new_user = Users(name=name, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()

                return insert_data(
                    id=new_user.id, name=new_user.name, password=new_user.password
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
