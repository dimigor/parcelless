from abc import ABC

from httpx import Response

from parcelless.infra.utils.request import request
from parcelless.platforms.base.resource.resource import BaseAbstractResource


class CarrierBaseResource(BaseAbstractResource, ABC):
    async def request(self, data) -> Response:
        return await request(
            method="POST",
            data=data.to_xml(),
            headers={"Content-Type": "text/xml;charset=utf-8"},
            auth=(),
        )
