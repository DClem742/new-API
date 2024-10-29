from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

class CategoryBase(SQLModel):
    name: str = Field(index=True)
    description: Optional[str] = None

class Category(CategoryBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    
