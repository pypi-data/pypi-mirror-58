from abc import ABC, abstractproperty
from pastpy.database.database_image import DatabaseImage
from typing import Dict, Iterable, Union


class DatabaseObject(ABC):
    @abstractproperty
    def date(self) -> Union[object, None]:
        """
        @return date of the object
        """
        pass

    @abstractproperty
    def description(self) -> Union[str, None]:
        """
        @return description of the object
        """
        pass

    @abstractproperty
    def id(self) -> str:
        """
        @return id of the object
        """
        pass

    @abstractproperty
    def impl_attributes(self) -> Dict[str, object]:
        """
        @return dict of implementation-defined attributes where neither keys nor values is None
        """
        pass

    @abstractproperty
    def images(self) -> Iterable[DatabaseImage]:
        """
        @return iterable of DatabaseImage instances
        """
        pass

    @abstractproperty
    def name(self) -> Union[str, None]:
        """
        @return name of object
        """
        pass

    @abstractproperty
    def othername(self) -> Union[str, None]:
        """
        @return alternative name of object
        """
        pass

    @abstractproperty
    def title(self) -> Union[str, None]:
        """
        @return title of object
        """
        pass
