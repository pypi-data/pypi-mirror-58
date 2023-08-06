from abc import ABC, abstractproperty
from typing import Union


class DatabaseImage(ABC):
    @abstractproperty
    def full_size_url(self) -> Union[str, None]:
        """
        @return full size URL of the image
        """
        pass

    @abstractproperty
    def thumbnail_url(self) -> Union[str, None]:
        """
        @return thumbnail URL of the image
        """
        pass

    @abstractproperty
    def title(self) -> Union[str, None]:
        """
        @return title of the image
        """
        pass
