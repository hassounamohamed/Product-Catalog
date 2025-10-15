import sys
from pathlib import Path
from typing import List
from fastmcp import FastMCP

# Ajouter le chemin du projet
sys.path.append(str(Path(__file__).parent))

from main import SessionLocal, Product

# ---------------------- MCP SERVER ----------------------
mcp = FastMCP(name="Product Catalog MCP Server")


@mcp.tool()
def list_products() -> List[dict]:
    """Liste tous les produits du catalogue"""
    db = SessionLocal()
    products = db.query(Product).all()
    result = [{"id": p.id, "name": p.name, "price": p.price} for p in products]
    db.close()
    return result


@mcp.tool()
def get_product(product_id: int) -> dict:
    """Retourne un produit spécifique par son ID"""
    db = SessionLocal()
    product = db.query(Product).filter(Product.id == product_id).first()
    db.close()
    if product:
        return {"id": product.id, "name": product.name, "price": product.price}
    return {"error": "Product not found"}


if __name__ == "__main__":
    mcp.run()
