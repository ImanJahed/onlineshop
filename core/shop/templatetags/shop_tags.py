from django.template import Library

from shop.models import ProductModel, WishlistProductModel

register = Library()


@register.inclusion_tag("includes/latest-products.html",takes_context=True)
def show_latest_products(context):
    request = context.get("request")
    latest_products = ProductModel.objects.filter(
        status=1, display_status=1).distinct().order_by("-created_date")[:8]
    wishlist_items = WishlistProductModel.objects.filter(user=request.user).values_list("product__id",flat=True) if request.user.is_authenticated else []
    return {"latest_products": latest_products,"request":request,"wishlist_items":wishlist_items}


@register.inclusion_tag("includes/similar-products.html",takes_context=True)
def show_similar_products(context, product):
    request = context.get("request")
    product_categories= product.categories.all()
    similar_products = ProductModel.objects.filter(
        status=1, display_status=1, categories__in=product_categories).distinct().exclude(id=product.id).order_by("-created_date")[:4]
    wishlist_items =  WishlistProductModel.objects.filter(user=request.user).values_list("product__id",flat=True) if request.user.is_authenticated else []
    return {"similar_products": similar_products,"request":request,"wishlist_items":wishlist_items}
