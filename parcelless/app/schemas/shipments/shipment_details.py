from pydantic import BaseModel

from parcelless.app.schemas.shipments.address import Address
from parcelless.app.schemas.shipments.package import Package


class ShipmentDetails(BaseModel):
    to_address: Address
    from_address: Address
    package: Package
    order_reference: str


class TrackingDetails(BaseModel):
    tracking_number: str
    external_reference: str | None = None


class ShipmentResult(TrackingDetails):
    label: str
