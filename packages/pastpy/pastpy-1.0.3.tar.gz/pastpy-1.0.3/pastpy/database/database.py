from abc import abstractmethod
import logging
from pastpy.database.database_object import DatabaseObject
from pastpy.gen.database.database_configuration import DatabaseConfiguration
from pastpy.gen.database.impl.dbf.dbf_database_configuration import DbfDatabaseConfiguration
from pastpy.gen.database.impl.dummy.dummy_database_configuration import DummyDatabaseConfiguration
from pastpy.gen.database.impl.online.online_database_configuration import OnlineDatabaseConfiguration
from typing import Iterable


class Database(object):
    def __init__(self):
        self._logger = logging.getLogger(self.__class__.__name__)

    @classmethod
    def create(cls, configuration):
        if isinstance(configuration, DatabaseConfiguration):
            if configuration.dbf:
                return cls.create(configuration.dbf)
            elif configuration.dummy:
                return cls.create(configuration.dummy)
            elif configuration.online:
                return cls.create(configuration.online)
            else:
                raise NotImplementedError
        elif isinstance(configuration, DbfDatabaseConfiguration):
            from pastpy.database.impl.dbf.dbf_database import DbfDatabase
            return DbfDatabase(configuration=configuration)
        elif isinstance(configuration, DummyDatabaseConfiguration):
            from pastpy.database.impl.dummy.dummy_database import DummyDatabase
            return DummyDatabase(configuration=configuration)
        elif isinstance(configuration, OnlineDatabaseConfiguration):
            from pastpy.database.impl.online.online_database import OnlineDatabase
            return OnlineDatabase(configuration=configuration)
        else:
            raise NotImplementedError

    @abstractmethod
    def objects(self) -> Iterable[DatabaseObject]:
        """
        Iterate over the objects in the database.
        @return an iterable of objects
        """
        pass
