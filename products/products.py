from flask import Blueprint, render_template
from API.api import GetAllProducts, GetSingleProducts , GetAllProductsCategory
products_bp = Blueprint('products_bp', __name__,
    template_folder='templates',
    static_folder='static')

@products_bp.route('/products')
def index():
    data = GetAllProducts()
    l = len(data)
    categories = set(product["category"] for product in data)
    
    return render_template('products/products.html', length = l, products = data)

@products_bp.route('/products/<int:id>')
def detailOfProduct(id):
    data = GetSingleProducts(id)
    category = data['category']
    allProducts = GetAllProductsCategory()
    productCategory = [product for product in allProducts if product ['category'] == category]
    i = len(productCategory)
    if i > 5:
        i = 5
    productFiltr = [product for product in productCategory if product['id'] != id]
    fourProducts = productFiltr[:i]


    return render_template('products/detail.html', length = i, detailOfProduct=data,  features = fourProducts)