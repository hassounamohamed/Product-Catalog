from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ---------------------- DATABASE CONFIG ----------------------
DATABASE_URL = "postgresql+psycopg2://postgres:mohamed123@localhost:5432/product_catalog"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


# ---------------------- MODEL ----------------------
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)


Base.metadata.create_all(bind=engine)


# ---------------------- SCHEMA ----------------------
class ProductCreate(BaseModel):
    name: str
    price: float

class ProductResponse(ProductCreate):
    id: int
    class Config:
        orm_mode = True


# ---------------------- APP ----------------------
app = FastAPI(title="Product Catalog API")


@app.get("/products", response_model=List[ProductResponse])
def get_products():
    """Retourne tous les produits de la base de données"""
    db = SessionLocal()
    products = db.query(Product).all()
    db.close()
    return products


@app.post("/products", response_model=ProductResponse)
def create_product(product: ProductCreate):
    """⚠️ Cet endpoint NE sera PAS exposé dans MCP"""
    db = SessionLocal()
    new_product = Product(name=product.name, price=product.price)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    db.close()
    return new_product
