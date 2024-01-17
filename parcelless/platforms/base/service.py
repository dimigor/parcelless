from abc import ABC, abstractmethod

from parcelless.app.schemas.shipments.shipment_details import ShipmentDetails, ShipmentResult


class BaseAbstractPlatformService(ABC):
    @abstractmethod
    async def validate_shipment(self, shipment_details: ShipmentDetails):
        ...

    @abstractmethod
    async def get_rates_for_shipment(self, shipment_details: ShipmentDetails):
        ...

    @abstractmethod
    async def announce_shipment(self, shipment_details: ShipmentDetails) -> ShipmentResult:
        ...
