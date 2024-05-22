from django.contrib import admin
from .models import ReviewModel

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id','user_id', 'product_id', 'rate', 'status']
admin.site.register(ReviewModel, ReviewAdmin)