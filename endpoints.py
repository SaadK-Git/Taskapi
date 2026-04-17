from models import Product, Category, ProductResponse,InputCategory,InputProduct
from database import get_db
from sqlalchemy.orm import Session, joinedload
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from database_models import Category as DBCategory, Product as DBProduct
router = APIRouter()

# Category Endpoints
@router.get("/categories/{category_id}", response_model=Category)
def get_category_by_id(category_id: int, db: Session = Depends(get_db)):
    category = db.query(DBCategory).filter(DBCategory.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.get("/categories", response_model=list[Category])
def get_category(page : int,db: Session = Depends(get_db)):
    if page < 1:
        page = 1
    category = db.query(DBCategory).offset((page-1)*5).limit(5).all() #considering 5 items per page
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.post("/categories")
def create_category(category: InputCategory, db: Session = Depends(get_db)):
    if db.query(DBCategory).filter(DBCategory.name == category.name).first():
        raise HTTPException(status_code=400, detail="Category with this name already exists")
    db.add(DBCategory(**category.model_dump()))
    db.commit()
    return JSONResponse(status_code=201, content={"message": "Category created successfully"})

@router.put("/categories/{category_id}")
def update_category(category_id: int, category: Category, db: Session = Depends(get_db)):
    db_category = db.query(DBCategory).filter(DBCategory.id == category_id).first()
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")
    db_category.name = category.name
    db.commit()
    return JSONResponse(status_code=200, content={"message": "Category updated successfully"})

@router.delete("/categories/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    db_category = db.query(DBCategory).filter(DBCategory.id == category_id).first()
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")
    db.query(DBProduct).filter(DBProduct.category_id == category_id).delete()
    db.delete(db_category)
    db.commit()
    return JSONResponse(status_code=200, content={"message": "Category deleted successfully"})

# Product Endpoints
@router.get("/products/{product_id}", response_model=ProductResponse)
def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    product = db.query(DBProduct).options(joinedload(DBProduct.category)).filter(DBProduct.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.get("/products", response_model=list[ProductResponse])
def get_product(page : int,db: Session = Depends(get_db)):
    if page < 1:
        page = 1
    product = db.query(DBProduct).options(joinedload(DBProduct.category)).offset((page-1)*5).limit(5).all() #considering 5 items per page
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/products")
def create_product(product: InputProduct, db: Session = Depends(get_db)):
    category = db.query(DBCategory).filter(DBCategory.id == product.category_id)
    if not category:
        raise HTTPException(status_code=400, detail="Category with this ID does not exist")
    if db.query(DBProduct).filter(DBProduct.name == product.name).first():
        raise HTTPException(status_code=400, detail="Product with this name already exists")
    db.add(DBProduct(**product.model_dump()))
    db.commit()
    return JSONResponse(status_code=201, content={"message": "Product created successfully"})

@router.put("/products/{product_id}")
def update_product(product_id: int, product: Product, db: Session = Depends(get_db)):
    db_product = db.query(DBProduct).filter(DBProduct.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    if product.name is not None:
        db_product.name = product.name

    if product.price is not None:
        db_product.price = product.price

    if product.description is not None:
        db_product.description = product.description

    if product.category_id is not None:
        db_product.category_id = product.category_id
    db.commit()
    return JSONResponse(status_code=200, content={"message": "Product updated successfully"})

@router.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = db.query(DBProduct).filter(DBProduct.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(db_product)
    db.commit()
    return JSONResponse(status_code=200, content={"message": "Product deleted successfully"})