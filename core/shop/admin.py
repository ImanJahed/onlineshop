from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from .models import ProductCategoryModel, ProductImageModel, ProductModel


# Register your models here.

@admin.register(ProductCategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ('title', )

    prepopulated_fields = {'slug': ('title', )}

@admin.register(ProductImageModel)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['product']
    search_fields = ['product__title']


class ImageTabularInline(admin.TabularInline):
    model = ProductImageModel
    extra = 1

# Filter by product discount percent
class ProductDiscountFilter(admin.SimpleListFilter):
    title = 'Discount'
    parameter_name = 'Discount'

    def lookups(self, request: Any, model_admin: Any) -> list[tuple[Any, str]]:
        return [
            ('more_20', 'More Than 20 Percent'),
            ('lees_20', 'Less Than 20 percent')
        ]

    def queryset(self, request: Any, queryset: QuerySet[Any]) -> QuerySet[Any] | None:
        if self.value() == 'more_20':
            return queryset.filter(discount_percent__gt=20)

        if self.value() == 'lees_20':
            return queryset.filter(discount_percent__lt=20)


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['thumbnail', 'user', 'title', 'stock', 'display_status', 'price', 'discount_percent', 'discount_price']
    list_filter = ('status', 'display_status', ProductDiscountFilter)
    search_fields = ('title',)

    prepopulated_fields = {'slug': ('title', )}
    inlines = [ImageTabularInline]
