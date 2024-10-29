from sqlmodel import Field
from .base import Base

class Product(Base, table=True):
    __tablename__ = "products"

    name: str
    price: float
    description: str = None
    image: str = None
    category_id: int = Field(foreign_key="categories.id")