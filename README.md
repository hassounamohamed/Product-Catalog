# 🛍️ Product Catalog Lab

## 📘 Description

Ce projet est une application **FastAPI** permettant de gérer un catalogue de produits.  
Elle expose des endpoints REST pour :
- Lister tous les produits disponibles (`GET /products`)
- Ajouter un nouveau produit (`POST /products`)

Le projet inclut également une intégration **MCP (Model Context Protocol)** pour permettre à des outils externes (comme Claude Desktop) d’interagir avec l’application via des *tools* (par exemple : `list_products_tool` et `get_product_tool`).

---



