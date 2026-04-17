from pydantic import BaseModel

class Category(BaseModel):
    id: int | None = None
    name: str | None = None

class InputCategory(BaseModel):
    name : str

class Product(BaseModel):
    name: str | None = None
    price: int | None = None
    description: str | None = None
    category_id: int | None = None

    # category: Category | None = None

class InputProduct(BaseModel):
    name: str
    price: int
    description: str
    category_id: int

class ProductResponse(BaseModel):
    id: int | None = None
    name: str | None = None
    price: int | None = None
    description: str | None = None
    category_id: int | None = None

    category: Category | None = None