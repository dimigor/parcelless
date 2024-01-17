from abc import ABC

from pydantic import BaseModel, ConfigDict


class BaseResourceModel(BaseModel, ABC):
    model_config = ConfigDict(populate_by_name=True)
