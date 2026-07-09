from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List


class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True, min_length=2, max_length=50)

    books: List["Book"] = Relationship(back_populates="category")