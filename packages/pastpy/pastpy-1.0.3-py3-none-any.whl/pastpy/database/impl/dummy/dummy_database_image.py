from pastpy.database.database_image import DatabaseImage


class DummyDatabaseImage(DatabaseImage):
    def __init__(self, *, image_index, object_index):
        self.__image_index = image_index
        self.__object_index = object_index

    @property
    def full_size_url(self):
        return "http://placehold.it/510x670"

    @property
    def thumbnail_url(self):
        return "http://placehold.it/210x210"

    @property
    def title(self):
        return "Dummy object %d image %d" % (self.__object_index, self.__image_index)
