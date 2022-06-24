from sqlalchemy import create_engine


class DBConecctionHandler:
    """SQLAlchemy database connection"""

    def __init__(self):
        self.__connection_string = "sqlite:///storage.db"
        self.session = None

    def get_engine(self):
        """
        Return connection Engine
        :parram - None
        :return - engine connection database
        """

        engine = create_engine(self.__connection_string)
        return engine
