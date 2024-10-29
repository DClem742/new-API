from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from decimal import Decimal

class ProductBase(SQLModel):
    name: str = Field(index=True)
    description: Optional[str] = None
    price: Decimal = Field(max_digits=10, decimal_places=2)
    stock: int = Field(default=0)
    category_id: Optional[int] = Field(default=None, foreign_key="category.id")

class Product(ProductBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    category: Optional["Category"] = Relationship(back_populates="products")
