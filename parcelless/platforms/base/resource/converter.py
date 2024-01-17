from abc import ABC, abstractmethod
from typing import Type

from parcelless.platforms.base.resource.models import BaseResourceModel


class BaseResourceConverter(ABC):
    @abstractmethod
    def convert(self) -> Type[BaseResourceModel]:
        pass
