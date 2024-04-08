from django.template import Library

from shop.models import ProductModel

register = Library()


@register.inclusion_tag("includes/latest_products.html")
def show_latest_products():
    latest_products = ProductModel.objects.filter(status=1, display_status=1).order_by(
        "-created_date"
    )[:8]
    return {"latest_products": latest_products}


@register.inclusion_tag("includes/similar_product.html")
def show_similar_products(product):
    categories_id = product.categories.all()
    similar_products = ProductModel.objects.filter(status=1, display_status=1).filter(
        categories__in=categories_id
    ).exclude(id=product.id)[:4]

    return {"similar_products": similar_products}
