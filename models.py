from pydantic import BaseModel
class Category(BaseModel):
    id: int | None = None
    name: str | None = None
class Product(BaseModel):
    id: int | None = None
    name: str | None = None
    price: int | None = None
    description: str | None = None
    category_id: int | None = None

    # category: Category | None = None

class ProductResponse(BaseModel):
    id: int | None = None
    name: str | None = None
    price: int | None = None
    description: str | None = None
    category_id: int | None = None

    category: Category | None = None