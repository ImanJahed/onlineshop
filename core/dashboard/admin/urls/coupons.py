from django.urls import path
from .. import views


urlpatterns = [
    path("coupon/list/",views.AdminCouponListView.as_view(),name="coupon-list"),
    path("coupon/create/",views.AdminCouponCreateView.as_view(),name="coupon-create"),
    path("coupon/<int:pk>/edit/",views.AdminCouponEditView.as_view(),name="coupon-edit"),
    path("coupon/<int:pk>/delete/",views.AdminCouponDeleteView.as_view(),name="coupon-delete"),
#     path("product/<int:pk>/add-image/",views.AdminProductAddImageView.as_view(),name="product-add-image"),
#     path("product/<int:pk>/image/<int:image_id>/remove/",views.AdminProductRemoveImageView.as_view(),name="product-remove-image"),
]