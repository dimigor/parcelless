from pydantic import BaseModel, Field, PositiveFloat, PositiveInt


class Dimension(BaseModel):
    length: PositiveInt | None = Field(default=None, ge=0)
    width: PositiveInt | None = Field(default=None, ge=0)
    height: PositiveInt | None = Field(default=None, ge=0)


class PackageItem(BaseModel):
    hs_code: str
    sku: str | None
    weight: float = Field(ge=0)
    quantity: PositiveInt = Field(ge=1)
    description: str
    price: PositiveFloat


class Package(BaseModel):
    dimensions: Dimension | None = None
    weight: PositiveFloat
    items: list[PackageItem] | None = None
