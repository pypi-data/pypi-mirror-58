from pastpy.database.database import Database
from pastpy.database.impl.dummy.dummy_database_object import DummyDatabaseObject
from pastpy.gen.database.impl.dummy.dummy_database_configuration import DummyDatabaseConfiguration


class DummyDatabase(Database):
    def __init__(self, *, configuration: DummyDatabaseConfiguration):
        Database.__init__(self)

        self.__configuration = configuration

    def objects(self):
        for i in range(self.__configuration.objects):
            yield DummyDatabaseObject(configuration=self.__configuration, index=i)
