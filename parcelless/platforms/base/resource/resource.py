from abc import ABC, abstractmethod
from typing import Any

from httpx import Response


class BaseAbstractResource(ABC):
    async def process(self) -> Any:
        data = self.prepare_request()
        response = await self.request(data)
        return self.parse_response(response)

    @abstractmethod
    def prepare_request(self) -> Any:
        pass

    @abstractmethod
    async def request(self, data: Any) -> Response:
        pass

    @abstractmethod
    def parse_response(self, response: Response) -> Any:
        pass
