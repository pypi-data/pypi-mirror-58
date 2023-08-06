from pastpy.database.database_object import DatabaseObject
from pastpy.database.impl.dummy.dummy_database_image import DummyDatabaseImage
import datetime


class DummyDatabaseObject(DatabaseObject):
    def __init__(self, *, configuration, index):
        self.__configuration = configuration
        self.__date = datetime.date.today().isoformat()
        self.__description = "Dummy object " + str(index)
        self.__id = "dummy" + str(index)
        self.__index = index
        self.__name = "Dummy object " + str(index)

    @property
    def date(self):
        return self.__date

    @property
    def description(self):
        return self.__description

    @property
    def images(self):
        for i in range(self.__configuration.images_per_object):
            yield DummyDatabaseImage(image_index=i, object_index=self.__index)

    @property
    def impl_attributes(self):
        return {}

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def othername(self):
        return None

    @property
    def title(self):
        return self.__name
