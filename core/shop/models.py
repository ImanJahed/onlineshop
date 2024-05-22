from datetime import datetime
from tabnanny import verbose

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField


# Create your models here.
def image_path(instance, filename):
    ext = filename.split(".")[-1]
    path = f"{instance.product.user.username}/{datetime.now().strftime('%Y-%m-%d')}/{filename}"
    return path


class ProductStatus(models.IntegerChoices):
    available = 1, _("موجود")
    unavailable = 2, _("ناموجود")


class ProductDisplayStatus(models.IntegerChoices):
    display = 1, _("نمایش")
    no_display = 2, _("عدم نمایش")


class ProductImageModel(models.Model):
    product = models.ForeignKey(
        "ProductModel",
        verbose_name=_("Product"),
        on_delete=models.CASCADE,
        related_name="images",
    )
    file = models.ImageField(_("Image"), upload_to="product/extra-img/", default='default/img4.jpg')


    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"

    def __str__(self):
        return self.product.title



class ProductCategoryModel(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    slug = models.SlugField(_("Slug"), allow_unicode=True)

    created_date = models.DateField(_("Created Date"), auto_now_add=True)
    modified_date = models.DateField(_("Modified Date"), auto_now=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)

        return super().save(*args, **kwargs)

    def clean(self):
        self.title = self.title.title()


class ProductModel(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        verbose_name=_("User"),
        on_delete=models.CASCADE,
        related_name="products",
    )

    title = models.CharField(_("Title"), max_length=50)
    slug = models.SlugField(_("Slug"), allow_unicode=True)
    # description = models.TextField(_("Description"), null=True, blank=True)
    description = RichTextField(_("description"), blank=True, null=True)
    brief_description = models.CharField(
        _("Brief Description"), max_length=150, null=True, blank=True
    )

    categories = models.ManyToManyField(ProductCategoryModel, verbose_name=_("Categories"), related_name='category', blank=True)
    image = models.ImageField(default="/default/img4.jpg",upload_to="product/img/")
    stock = models.PositiveIntegerField(_("Stock"), default=0)
    price = models.DecimalField(_("Price"), max_digits=9, decimal_places=0)
    discount_percent = models.PositiveIntegerField(_("Discount Percent"), default=0)

    status = models.PositiveSmallIntegerField(
        _("Status"), choices=ProductStatus.choices, default=ProductStatus.available
    )
    display_status = models.PositiveSmallIntegerField(
        _("Display Status"),
        choices=ProductDisplayStatus.choices,
        default=ProductDisplayStatus.display,
    )
    avg_rate = models.FloatField(default=0.0)

    created_date = models.DateTimeField(_("Created Date"), auto_now_add=True)
    modified_date = models.DateTimeField(_("Modified Date"), auto_now=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.title

    @property
    def discount_price(self):
        if self.discount_percent:
            price_after_discount_percent = (
                self.price * (100 - self.discount_percent)
            ) / 100
            return round(price_after_discount_percent)
        
        return self.price

    def show_price(self):
        """Showing price with separate by , in template"""

        # if self.discount_percent:
        price_after_discount_percent = (
            self.price * (100 - self.discount_percent)
        ) / 100
        return {
            "price_discount": "{:,}".format(round(price_after_discount_percent)),
            "price": "{:,}".format(self.price),
        }

        # return "{:,}".format(self.price)

    def is_discount(self):
        return self.discount_percent != 0

    def is_published(self):
        return True if self.display_status==1 else False
    
    def save(self, *args, **kwargs) -> None:
        if self.stock == 0:
            self.status = 2
            self.display_status = 2
        else:
            self.status = 1
            self.display_status = 1

        if not self.slug:
            self.slug = slugify(self.title)

        return super().save(*args, **kwargs)

    def clean(self):
        self.title = self.title.title()

        if self.description:
            self.description = self.description.title()

        if self.brief_description:
            self.brief_description = self.brief_description.title()

    def thumbnail(self):
        if self.image:
            image = self.image.url

            return mark_safe(
                f'<img src={image} width=50px height=50px object-fit="cover" \
                    style="border-radius: 5px;" />'
            )
        return mark_safe(
            '<img src=/static/img2.jpg width=50px height=50px object-fit="cover" \
                    style="border-radius: 5px;" />'
        )




class WishlistProductModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'WishList'
        verbose_name_plural = 'WishLists'

    def __str__(self) -> str:
        return self.product.title